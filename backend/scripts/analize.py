import pickle

with open('/Users/pawel/PycharmProjects/SUML_PJATK/model_training/models/sentiment_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('/Users/pawel/PycharmProjects/SUML_PJATK/model_training/models/vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

def predict_sentiment(text):
    text_vec = vectorizer.transform([text])

    prediction = model.predict(text_vec)

    return prediction[0]