from fastapi import APIRouter, HTTPException
from services import delete, get, patch, post, put

router = APIRouter(prefix="/nasabah", tags=["Nasabah"])


def _missing():
    raise HTTPException(status_code=404, detail="Nasabah not found")


@router.get("/")
def get_all(): return get.get_all_nasabah()


@router.get("/{record_id}")
def get_one(record_id: int):
    record = get.get_nasabah_by_id(record_id)
    return record if record else _missing()


@router.post("/", status_code=201)
def create(data: dict): return post.create_nasabah(data)


@router.put("/{record_id}")
def replace(record_id: int, data: dict):
    record = put.replace_nasabah(record_id, data)
    return record if record else _missing()


@router.patch("/{record_id}")
def update(record_id: int, data: dict):
    record = patch.update_nasabah(record_id, data)
    return record if record else _missing()


@router.delete("/{record_id}", status_code=204)
def remove(record_id: int):
    if not delete.delete_nasabah_by_id(record_id):
        _missing()
