from nlp.cleaner import clean_text
from nlp.filter import filter_stopwords
from nlp.sentiment import analyze_sentiment

if __name__ == "__main__":
    while True:  # Bucle continuo para solicitar texto
        user_input = input("Ingrese el texto a filtrar y analizar (o presione Enter para salir): ")
        if not user_input:  # Salir si el usuario presiona Enter
            break
        
        # Procesar el texto a través de los filtros (tuberías)
        cleaned_text = clean_text(user_input)  # Filtro 1: Limpieza
        filtered_text = filter_stopwords(cleaned_text)  # Filtro 2: Filtrado de stopwords
        sentiment, intensity = analyze_sentiment(filtered_text)  # Filtro 3: Análisis de sentimiento
        
        # Mostrar resultados
        print(f"Texto limpio: {cleaned_text}")
        print(f"Texto filtrado: {filtered_text}")
        print(f"Sentimiento: {sentiment}")
        print(f"Intensidad del sentimiento: {intensity:.2f}\n")
