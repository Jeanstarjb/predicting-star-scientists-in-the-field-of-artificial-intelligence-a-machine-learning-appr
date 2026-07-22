from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database
from typing import List

router = APIRouter(
    prefix="/researchers",
    tags=["researchers"]
)

@router.post("/", response_model=schemas.Researcher)
def create_researcher(researcher: schemas.ResearcherCreate, db: Session = Depends(database.get_db)):
    db_researcher = models.Researcher(**researcher.dict())
    db.add(db_researcher)
    db.commit()
    db.refresh(db_researcher)
    return db_researcher

@router.get("/", response_model=List[schemas.Researcher])
def read_researchers(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return db.query(models.Researcher).offset(skip).limit(limit).all()

@router.get("/{researcher_id}", response_model=schemas.Researcher)
def read_researcher(researcher_id: int, db: Session = Depends(database.get_db)):
    researcher = db.query(models.Researcher).filter(models.Researcher.id == researcher_id).first()
    if not researcher:
        raise HTTPException(status_code=404, detail="Researcher not found")
    return researcher

@router.put("/{researcher_id}", response_model=schemas.Researcher)
def update_researcher(researcher_id: int, researcher: schemas.ResearcherUpdate, db: Session = Depends(database.get_db)):
    db_researcher = db.query(models.Researcher).filter(models.Researcher.id == researcher_id).first()
    if not db_researcher:
        raise HTTPException(status_code=404, detail="Researcher not found")
    
    for key, value in researcher.dict().items():
        setattr(db_researcher, key, value)
    
    db.commit()
    db.refresh(db_researcher)
    return db_researcher

@router.delete("/{researcher_id}")
def delete_researcher(researcher_id: int, db: Session = Depends(database.get_db)):
    researcher = db.query(models.Researcher).filter(models.Researcher.id == researcher_id).first()
    if not researcher:
        raise HTTPException(status_code=404, detail="Researcher not found")
    
    db.delete(researcher)
    db.commit()
    return {"message": "Researcher deleted successfully"}