import threading
from nlp.event_manager import EventManager
from nlp.cleaner import Cleaner
from nlp.stopwords_filter import StopwordFilter
from nlp.sentiment_analyzer import SentimentAnalyzer

def publisher(event_manager):
    while True:
        try:
            text = input("Ingrese el texto para analizar (o 'exit' para salir): ")
            if text.lower() == 'exit':
                break
            print(f"[Publisher] Mensaje original: '{text}'")  # Verificar mensaje original
            event_manager.publish('clean', text)
        except KeyboardInterrupt:
            print("\nInterrumpido por el usuario.")
            break

def main():
    event_manager = EventManager()
    cleaner = Cleaner(event_manager)
    stopword_filter = StopwordFilter(event_manager)
    sentiment_analyzer = SentimentAnalyzer(event_manager)

    # Suscripciones en el orden correcto
    event_manager.subscribe('clean', cleaner)
    event_manager.subscribe('filtered', stopword_filter)
    event_manager.subscribe('analyze', sentiment_analyzer)

    # Iniciar el hilo del publisher como un daemon
    thread = threading.Thread(target=publisher, args=(event_manager,), daemon=True)
    thread.start()

    # Espera al hilo hasta que el usuario termine el proceso
    try:
        thread.join()  # El programa puede cerrarse si se interrumpe
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")

if __name__ == '__main__':
    main()
