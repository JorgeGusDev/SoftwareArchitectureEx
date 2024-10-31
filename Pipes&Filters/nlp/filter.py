def filter_stopwords(text):
    stopwords = set([
        "a", "al", "algo", "alguno", "alguna", "algunas", "algunos", "ante", "antes", "como", "con", "cual",
        "cuando", "de", "debe", "debido", "desde", "donde", "durante", "el", "ella", "ellas", "ello", 
        "ellos", "en", "entre", "era", "eres", "es", "esa", "ese", "eso", "está", "estoy", "y", 
        "la", "las", "lo", "los", "más", "me", "mi", "mío", "mía", "mucho", "muchos", "nada", 
        "nadie", "ni", "no", "nos", "nosotros", "nuestra", "nuestras", "nuestro", "nuestros", "otro", 
        "otra", "otras", "otros", "para", "pero", "poco", "por", "porque", "que", "quien", "quienes", 
        "si", "sin", "sobre", "su", "sus", "tanto", "tan", "te", "tu", "tuyo", "tuyos", "un", "una", 
        "uno", "unos", "ya"
    ])
    filtered_words = [word for word in text.split() if word not in stopwords]
    return ' '.join(filtered_words)
