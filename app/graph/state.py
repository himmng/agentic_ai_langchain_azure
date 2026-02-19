from typing import TypedDict, Optional, Dict, List


class SentimentState(TypedDict):
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

    sentiment: Optional[str]
    emotional_tone: Optional[str]
    key_drivers: Optional[List[str]]
    churn_risk: Optional[str]
    confidence: Optional[float]
