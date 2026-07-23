from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models
from ..utils import analytics
from typing import List

router = APIRouter(tags=['insights'])

@router.get('/diversity-metrics')
async def get_diversity_metrics(db: Session = Depends(database.get_db)):
    try:
        metrics = analytics.calculate_diversity_metrics(db)
        return [
            {'metric': 'Collaboration', 'value': metrics['collab_diversity']},
            {'metric': 'Institution', 'value': metrics['inst_diversity']},
            {'metric': 'Publication Venues', 'value': metrics['venue_diversity']},
            {'metric': 'Research Topics', 'value': metrics['topic_diversity']},
            {'metric': 'Citation Impact', 'value': metrics['citation_diversity']}
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))