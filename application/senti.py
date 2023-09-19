from transformers import pipeline
nlp = pipeline("sentiment-analysis")


def AnalyzeSentiment(statement):
    results = nlp(statement)
    sentiment = results[0]['label']
    sentiment_score = results[0]['score']
    return {
        "csentiment_score": sentiment_score,  # Rename for clarity
        "sentiment": sentiment
    }
    