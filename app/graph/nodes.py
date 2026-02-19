# app/graph/nodes.py

from pydantic import BaseModel, Field
from app.core.llm import get_llm
from app.services.prompt_builder import build_sentiment_payload
from app.graph.state import SentimentState

llm = get_llm()


# -----------------------------
# Structured Output Schema
# -----------------------------

class SentimentOutput(BaseModel):
    sentiment: str = Field(
        description="overall sentiment: positive, neutral, or negative"
    )
    emotional_tone: str = Field(
        description="dominant emotional tone such as frustration, satisfaction, confusion, etc."
    )
    key_drivers: list[str] = Field(
        description="main factors influencing sentiment"
    )
    churn_risk: str = Field(
        description="low, medium, or high churn risk"
    )
    confidence: float = Field(
        description="confidence score between 0 and 1"
    )


structured_llm = llm.with_structured_output(SentimentOutput)


# -----------------------------
# Nodes
# -----------------------------

def preprocess_node(state: SentimentState):
    text = state["answers"].strip()
    return {"cleaned_text": text}


def sentiment_node(state: SentimentState):

    payload = build_sentiment_payload(state)

    result = structured_llm.invoke(payload)

    return {
        "sentiment": result.sentiment,
        "emotional_tone": result.emotional_tone,
        "key_drivers": result.key_drivers,
        "churn_risk": result.churn_risk,
        "confidence": result.confidence
    }
