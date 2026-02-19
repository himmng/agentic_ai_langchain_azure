from app.services.sentiment_service import analyze_message

def test_positive():
    result = analyze_message("Great service!")
    assert result["sentiment"] == "positive"
