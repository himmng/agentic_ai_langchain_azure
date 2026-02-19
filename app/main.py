from app.data.json_loader import load_json
from app.data.transformer import extract_relevant_fields
from app.services.sentiment_service import analyze_batch

def run_pipeline(filepath: str):

    raw = load_json(filepath)
    df = extract_relevant_fields(raw)

    results = analyze_batch(df.to_dict(orient="records"))

    df["sentiment"] = [r["sentiment"] for r in results]
    df["confidence"] = [r["confidence"] for r in results]

    df.to_csv("output_sentiment.csv", index=False)


if __name__ == "__main__":
    run_pipeline("data/synergy.json")
