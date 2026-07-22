from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey, Float, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Researcher(Base):
    __tablename__ = 'researchers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    institution = Column(String(255))
    start_year = Column(Integer, nullable=False)
    citation_count = Column(Integer, default=0)
    publications_count = Column(Integer, default=0)
    h_index = Column(Integer, default=0)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    publications = relationship('Publication', backref='researcher')
    predictions = relationship('Prediction', backref='researcher')

class Publication(Base):
    __tablename__ = 'publications'

    id = Column(Integer, primary_key=True, index=True)
    researcher_id = Column(Integer, ForeignKey('researchers.id'), nullable=False)
    title = Column(String(255), nullable=False)
    publication_date = Column(Date, nullable=False)
    citation_count = Column(Integer, default=0)
    journal = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, index=True)
    researcher_id = Column(Integer, ForeignKey('researchers.id'), nullable=False)
    prediction_score = Column(Float, nullable=False)
    feature_set = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())