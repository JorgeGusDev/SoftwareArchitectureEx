import re

def clean_text(text):
    text = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', text)  # Remover caracteres especiales
    return text.lower()  # Convertir a minúsculas para consistencia
