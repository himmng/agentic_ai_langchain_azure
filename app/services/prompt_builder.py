def build_sentiment_payload(row: dict) -> str:
    return f"""
Survey ID: {row['survey_id']}
Overall Score: {row['overall_score']}

Customer Answer:
{row['answers']}

Social Review:
{row['social_review']}

Incident:
{row['incidents']}

Tags:
{row['tags']}

Metadata:
{row['metadata']}

Task:
Provide:
1. Overall sentiment (positive/neutral/negative)
2. Emotional tone
3. Key drivers
4. Risk of churn (low/medium/high)
Return JSON only.
"""
