import pandas as pd
from typing import List, Dict, Any

def extract_relevant_fields(records: List[Dict[str, Any]]) -> pd.DataFrame:
    processed = []

    for record in records:

        # Extract answers
        answers_text = " ".join(
            a.get("text", "") for a in record.get("answers", [])
        )

        # Extract incidents
        incident_text = " ".join(
            i.get("description", "") for i in record.get("incidents", [])
        )

        # Extract scores
        scores = record.get("scores", [])
        score_dict = {s["name"]: s["value"] for s in scores}

        # Extract tags
        tags = record.get("tags", [])
        tag_dict = {}
        for t in tags:
            tag_dict.update(t)

        # Extract social review
        social_review = ""
        if record.get("socialReview"):
            social_review = record["socialReview"].get("text", "")

        # Metadata
        metadata = record.get("end_user_properties", {})

        processed.append({
            "id": record.get("customer_id"),
            "externalId": record.get("externalId"),
            "survey_id": record.get("surveyId"),
            "overall_score": score_dict.get("overall_satisfaction"),
            "answers": answers_text,
            "tags": tag_dict,
            "scores_by_category": score_dict,
            "incidents": incident_text,
            "social_review": social_review,
            "metadata": metadata
        })

    return pd.DataFrame(processed)
