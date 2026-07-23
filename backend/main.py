from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
import joblib
from sqlalchemy.orm import Session
import datetime
from . import models, schemas, preprocessing
from .database import get_db
from .routers import researchers, publications, predictions, auth, insights

app = FastAPI()

# ... [keep existing model loading] ...

app.include_router(auth.router)
app.include_router(researchers.router)
app.include_router(publications.router)
app.include_router(predictions.router)
app.include_router(insights.router, prefix="/api/insights")

# ... [keep existing endpoints] ...