from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Claim(Base):
    __tablename__ = "claims"

    id = Column(String, primary_key=True, index=True)
    payer = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    procedure_code = Column(String, nullable=False)
    status = Column(String, default="received")
