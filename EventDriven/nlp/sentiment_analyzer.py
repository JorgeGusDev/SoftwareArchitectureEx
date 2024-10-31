from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

    def notify(self, message):
        sentiment = self.analyzer(message)[0]
        print(f"[SentimentAnalyzer] Análisis de sentimiento para: '{message}'")
        print(f"Sentimiento: {sentiment['label']}, Intensidad: {sentiment['score']:.2f}")
