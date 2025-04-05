# api/routes_claims.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.claim_schema import ClaimCreate, ClaimResponse
from app.queries.queries_helper import (
    create_claim,
    get_all_claims,
    get_claim,
    update_claim_status,
    delete_claim,
)
from app.core.auth import verify_api_key
from app.db.db_config import get_db

router = APIRouter(prefix="/claims", tags=["Claims"])


@router.post("/", response_model=ClaimResponse)
def submit_claim(
    claim: ClaimCreate, db: Session = Depends(get_db), _: str = Depends(verify_api_key)
):
    return create_claim(db, claim)


@router.get("/", response_model=list[ClaimResponse])
def list_claims(db: Session = Depends(get_db), _: str = Depends(verify_api_key)):
    return get_all_claims(db)


@router.get("/{claim_id}", response_model=ClaimResponse)
def fetch_claim(
    claim_id: str, db: Session = Depends(get_db), _: str = Depends(verify_api_key)
):
    claim = get_claim(db, claim_id)
    if not claim:
        raise HTTPException(404, detail="Claim not found")
    return claim


@router.get("/status/{claim_id}")
def claim_status(
    claim_id: str, db: Session = Depends(get_db), _: str = Depends(verify_api_key)
):
    claim = get_claim(db, claim_id)
    if not claim:
        raise HTTPException(404, detail="Claim not found")
    return {"id": claim.id, "status": claim.status}


@router.put("/{claim_id}/status")
def update_status(
    claim_id: str,
    status: str,
    db: Session = Depends(get_db),
    _: str = Depends(verify_api_key),
):
    updated = update_claim_status(db, claim_id, status)
    if not updated:
        raise HTTPException(404, detail="Claim not found")
    return {"message": "Status updated", "id": claim_id, "new_status": status}


@router.delete("/{claim_id}")
def delete_claim_endpoint(
    claim_id: str, db: Session = Depends(get_db), _: str = Depends(verify_api_key)
):
    deleted = delete_claim(db, claim_id)
    if not deleted:
        raise HTTPException(404, detail="Claim not found")
    return {"message": "Claim deleted", "id": claim_id}
