import re

class Cleaner:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def notify(self, message):
        cleaned_message = re.sub(r'[^a-zA-Z\s]', '', message).strip()
        print(f"[Cleaner] Mensaje limpio: '{cleaned_message}'")  # Confirmación de limpieza
        self.event_manager.publish('filtered', cleaned_message)
