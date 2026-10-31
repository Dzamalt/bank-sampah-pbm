from fastapi import APIRouter, HTTPException
from services import delete, get, patch, post, put

router = APIRouter(prefix="/transactions", tags=["Transactions"])


def _missing(): raise HTTPException(status_code=404, detail="Transaction not found")
@router.get("/")
def get_all(): return get.get_all_transactions()
@router.get("/{record_id}")
def get_one(record_id: int):
    record = get.get_transaction_by_id(record_id)
    return record if record else _missing()
@router.post("/", status_code=201)
def create(data: dict): return post.create_transaction(data)
@router.put("/{record_id}")
def replace(record_id: int, data: dict):
    record = put.replace_transaction(record_id, data)
    return record if record else _missing()
@router.patch("/{record_id}")
def update(record_id: int, data: dict):
    record = patch.update_transaction(record_id, data)
    return record if record else _missing()
@router.delete("/{record_id}", status_code=204)
def remove(record_id: int):
    if not delete.delete_transaction_by_id(record_id): _missing()
