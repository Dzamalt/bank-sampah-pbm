from fastapi import FastAPI
import uvicorn

from routes.category_prices import router as category_prices_router
from routes.nasabah import router as nasabah_router
from routes.transaction import router as transaction_router
from routes.waste_category import router as waste_category_router
from routes.weighing_session import router as weighing_session_router


def create_app():
    app = FastAPI(title="Bank Sampah PBM API", version="1.0.0")
    app.include_router(nasabah_router)
    app.include_router(waste_category_router)
    app.include_router(weighing_session_router)
    app.include_router(category_prices_router)
    app.include_router(transaction_router)
    return app


app = create_app()


@app.get("/")
def home():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
