# main.py
from fastapi import FastAPI
from app.api.routes_claims import router as claim_router
from app.db.models import Base
from app.db.db_config import engine
import app.utils.logger

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Claim Processing API")
app.include_router(claim_router)


@app.get("/")
def root():
    return {"message": "Welcome to Claim API"}
