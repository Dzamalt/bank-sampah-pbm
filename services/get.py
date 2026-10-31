from sqlmodel import select

import extensions
from models import CategoryPrice, Nasabah, Transaction, WasteCategory, WeighingSession


def _all(model):
    with extensions.open_session() as session:
        return session.exec(select(model)).all()


def _by_id(model, record_id):
    with extensions.open_session() as session:
        return session.get(model, record_id)


def get_all_nasabah(): return _all(Nasabah)
def get_nasabah_by_id(record_id): return _by_id(Nasabah, record_id)
def get_all_waste_categories(): return _all(WasteCategory)
def get_waste_category_by_id(record_id): return _by_id(WasteCategory, record_id)
def get_all_weighing_sessions(): return _all(WeighingSession)
def get_weighing_session_by_id(record_id): return _by_id(WeighingSession, record_id)
def get_all_category_prices(): return _all(CategoryPrice)
def get_category_price_by_id(record_id): return _by_id(CategoryPrice, record_id)
def get_all_transactions(): return _all(Transaction)
def get_transaction_by_id(record_id): return _by_id(Transaction, record_id)
