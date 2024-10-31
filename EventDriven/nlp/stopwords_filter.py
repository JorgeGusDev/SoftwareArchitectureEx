# stopwords_filter.py

from nltk.corpus import stopwords

class StopwordFilter:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.subscribe('filtered', self)

    def notify(self, message):
        # Filtra las palabras vacías
        filtered_message = ' '.join(
            [word for word in message.split() if word.lower() not in stopwords.words('spanish')]
        )
        print(f"[StopwordFilter] Mensaje filtrado: '{filtered_message}'")
        # Publica el mensaje filtrado
        self.event_manager.publish('analyze', filtered_message)
