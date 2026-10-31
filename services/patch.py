from datetime import datetime

import extensions
from models import CategoryPrice, Nasabah, Transaction, WasteCategory, WeighingSession


def _update(model, record_id, data, fields):
    with extensions.open_session() as session:
        record = session.get(model, record_id)
        if record is None:
            return None
        for key, value in data.items():
            if key in fields:
                setattr(record, key, value)
        if hasattr(record, "updated_at"):
            record.updated_at = datetime.utcnow()
        session.add(record)
        session.commit()
        session.refresh(record)
        return record


def update_nasabah(id, data): return _update(Nasabah, id, data, {"name", "phone", "note", "is_active"})
def update_waste_category(id, data): return _update(WasteCategory, id, data, {"code", "name", "unit", "is_active"})
def update_weighing_session(id, data): return _update(WeighingSession, id, data, {"session_date", "title", "status", "notes"})
def update_category_price(id, data): return _update(CategoryPrice, id, data, {"session_id", "category_id", "price_per_unit"})
def update_transaction(id, data): return _update(Transaction, id, data, {"session_id", "nasabah_id", "category_id", "weight", "price_per_unit"})
