import extensions
from models import CategoryPrice, Nasabah, Transaction, WasteCategory, WeighingSession


def _create(model, data, fields):
    with extensions.open_session() as session:
        record = model(**{key: value for key, value in data.items() if key in fields})
        session.add(record)
        session.commit()
        session.refresh(record)
        return record


def create_nasabah(data): return _create(Nasabah, data, {"name", "phone", "note", "is_active"})
def create_waste_category(data): return _create(WasteCategory, data, {"code", "name", "unit", "is_active"})
def create_weighing_session(data): return _create(WeighingSession, data, {"session_date", "title", "status", "notes"})
def create_category_price(data): return _create(CategoryPrice, data, {"session_id", "category_id", "price_per_unit"})
def create_transaction(data): return _create(Transaction, data, {"session_id", "nasabah_id", "category_id", "weight", "price_per_unit"})
