# app/crud.py
from sqlalchemy.orm import Session
from uuid import uuid4
from app.db import models
from app.schemas.claim_schema import ClaimCreate


def create_claim(db: Session, claim: ClaimCreate) -> models.Claim:
    db_claim = models.Claim(
        id=str(uuid4()),
        payer=claim.payer,
        amount=claim.amount,
        procedure_code=claim.procedure_code,
        status="RECEIVED",
    )
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim


def get_claim(db: Session, claim_id: str):
    return db.query(models.Claim).filter(models.Claim.id == claim_id).first()


def get_all_claims(db: Session):
    return db.query(models.Claim).all()


def update_claim_status(db: Session, claim_id: str, new_status: str):
    claim = get_claim(db, claim_id)
    if claim:
        claim.status = new_status
        db.commit()
        db.refresh(claim)
    return claim


def delete_claim(db: Session, claim_id: str):
    claim = get_claim(db, claim_id)
    if claim:
        db.delete(claim)
        db.commit()
    return claim
