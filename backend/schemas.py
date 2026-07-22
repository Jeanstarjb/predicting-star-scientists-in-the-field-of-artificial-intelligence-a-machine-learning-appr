from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional

class ResearcherBase(BaseModel):
    name: str
    institution: str
    start_year: int
    citation_count: int = 0
    publications_count: int = 0
    h_index: int = 0

class ResearcherCreate(ResearcherBase):
    pass

class Researcher(ResearcherBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class PublicationBase(BaseModel):
    title: str
    publication_date: date
    citation_count: int = 0
    journal: str

class PublicationCreate(PublicationBase):
    researcher_id: int

class Publication(PublicationBase):
    id: int
    researcher_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class PredictionBase(BaseModel):
    researcher_id: int
    prediction_score: float

class Prediction(PredictionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True