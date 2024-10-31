from transformers import pipeline

# Inicializar el modelo de análisis de sentimientos
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text):
    # Realiza el análisis de sentimientos
    analysis = sentiment_analyzer(text)
    sentiment = analysis[0]['label']  # Obtener la etiqueta
    intensity = analysis[0]['score']   # Obtener la puntuación (intensidad)
    
    # Mapear la etiqueta a positivo, negativo o neutro
    if sentiment == '5 stars':
        sentiment_label = 'positivo'
    elif sentiment == '1 star':
        sentiment_label = 'negativo'
    else:
        sentiment_label = 'neutro'
    
    return sentiment_label, intensity
