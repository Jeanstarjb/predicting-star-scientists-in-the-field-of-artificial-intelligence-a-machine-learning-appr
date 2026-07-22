from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey, Float, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Researcher(Base):
    __tablename__ = 'researchers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    institution = Column(String(255))
    start_year = Column(Integer)
    citation_count = Column(Integer, default=0)
    publications_count = Column(Integer, default=0)
    h_index = Column(Integer, default=0)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    publications = relationship('Publication', back_populates='researcher')
    predictions = relationship('Prediction', back_populates='researcher')

class Publication(Base):
    __tablename__ = 'publications'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    publication_date = Column(Date)
    citation_count = Column(Integer, default=0)
    journal = Column(String(255))
    researcher_id = Column(Integer, ForeignKey('researchers.id'))

    researcher = relationship('Researcher', back_populates='publications')

class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, index=True)
    researcher_id = Column(Integer, ForeignKey('researchers.id'))
    prediction_score = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    researcher = relationship('Researcher', back_populates='predictions')