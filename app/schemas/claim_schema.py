from pydantic import BaseModel, Field


class ClaimBase(BaseModel):
    payer: str = Field(..., example="HealthCare Inc.")
    amount: float = Field(..., gt=0, example=299.99)
    procedure_code: str = Field(..., example="PROC123")


class ClaimCreate(ClaimBase):
    pass


class ClaimResponse(ClaimBase):
    id: str
    status: str

    model_config = {"from_attributes": True}
