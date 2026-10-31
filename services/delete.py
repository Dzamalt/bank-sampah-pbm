import extensions
from models import CategoryPrice, Nasabah, Transaction, WasteCategory, WeighingSession


def _delete(model, record_id):
    with extensions.open_session() as session:
        record = session.get(model, record_id)
        if record is None:
            return False
        session.delete(record)
        session.commit()
        return True


def delete_nasabah_by_id(id): return _delete(Nasabah, id)
def delete_waste_category_by_id(id): return _delete(WasteCategory, id)
def delete_weighing_session_by_id(id): return _delete(WeighingSession, id)
def delete_category_price_by_id(id): return _delete(CategoryPrice, id)
def delete_transaction_by_id(id): return _delete(Transaction, id)
