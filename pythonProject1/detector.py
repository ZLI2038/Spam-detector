
from model_loader import load_model

clf = load_model()

def detect_spam(text, model):
    prediction = model.predict([text])
    return "🟥 Spam Email!" if prediction[0] == 1 else "🟩 Ham Email."

def detect_spam_batch(texts, model):
    preds = model.predict(texts)
    return ["🟥 Spam" if p == 1 else "🟩 Ham" for p in preds]
