from datetime import date, datetime

from sqlalchemy import CheckConstraint, Column, Computed, Float, String, UniqueConstraint
from sqlmodel import Field, SQLModel


class Nasabah(SQLModel, table=True):
    __tablename__ = "nasabahs"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, nullable=False, unique=True)
    phone: str = Field(max_length=15, nullable=False, unique=True)
    note: str | None = Field(default=None, max_length=255, nullable=True)
    is_active: bool = Field(default=True, nullable=False)
    created_at: datetime = Field(default=datetime.utcnow, nullable=False)


class WasteCategory(SQLModel, table=True):
    __tablename__ = "waste_categories"
    id: int | None = Field(default=None, primary_key=True)
    code: int = Field(nullable=False, unique=True)
    name: str = Field(max_length=100, nullable=False, unique=True)
    unit: str = Field(max_length=50, nullable=False, default="kg")
    is_active: bool = Field(default=True, nullable=False)
    created_at: datetime = Field(default=datetime.utcnow, nullable=False)


class WeighingSession(SQLModel, table=True):
    __tablename__ = "weighing_sessions"
    id: int | None = Field(default=None, primary_key=True)
    session_date: date = Field(nullable=False)
    title: str = Field(max_length=100, nullable=False)
    status: str = Field(
        sa_column=Column(String(50), nullable=False, server_default="open"),
        default="open",
    )
    notes: str | None = Field(default=None, max_length=255, nullable=True)
    created_at: datetime = Field(default=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default=datetime.utcnow, nullable=False)
    __table_args__ = (
        CheckConstraint("status IN ('open', 'completed', 'archived')", name="check_status"),
    )


class CategoryPrice(SQLModel, table=True):
    __tablename__ = "category_prices"
    __table_args__ = (
        UniqueConstraint("session_id", "category_id"),
        CheckConstraint("price_per_unit >= 0", name="check_price_non_negative"),
    )
    id: int | None = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="weighing_sessions.id", nullable=False, ondelete="CASCADE")
    category_id: int = Field(foreign_key="waste_categories.id", nullable=False, ondelete="RESTRICT")
    price_per_unit: float = Field(default=0.0, nullable=False)


class Transaction(SQLModel, table=True):
    __tablename__ = "transactions"
    __table_args__ = (
        UniqueConstraint("session_id", "nasabah_id", "category_id"),
        CheckConstraint("weight >= 0", name="check_weight_non_negative"),
        CheckConstraint("price_per_unit >= 0", name="check_price_non_negative"),
    )
    id: int | None = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="weighing_sessions.id", nullable=False, ondelete="CASCADE")
    nasabah_id: int = Field(foreign_key="nasabahs.id", nullable=False, ondelete="RESTRICT")
    category_id: int = Field(foreign_key="waste_categories.id", nullable=False, ondelete="RESTRICT")
    weight: float = Field(default=0.0, nullable=False)
    price_per_unit: float = Field(default=0.0, nullable=False)
    total_amount: float | None = Field(
        default=None,
        sa_column=Column(Float, Computed("weight * price_per_unit", persisted=True), nullable=True),
    )
    created_at: datetime = Field(default=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default=datetime.utcnow, nullable=False)