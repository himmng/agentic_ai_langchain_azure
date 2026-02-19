# app/data/schema.py

from pydantic import BaseModel
from typing import Optional, Dict, List


class InMomentRecord(BaseModel):
    id: int
    externalId: Optional[int]
    survey_id: Optional[str]
    overall_score: Optional[int]
    answers: Optional[str]
    tags: Optional[Dict]
    scores_by_category: Optional[Dict]
    incidents: Optional[str]
    social_review: Optional[str]
    metadata: Optional[Dict]


class SentimentResult(BaseModel):
    sentiment: str
    emotional_tone: str
    key_drivers: List[str]
    churn_risk: str
    confidence: float
