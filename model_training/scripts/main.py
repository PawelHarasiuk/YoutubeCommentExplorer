import pickle

with open('../models/sentiment_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('../models/vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)


def predict_sentiment(text, sent):
    text_vec = vectorizer.transform([text])

    prediction = model.predict(text_vec)

    guess = 'Positive' if prediction[0] == 1 else 'Negative'
    if sent == guess:
        return 1, guess
    else:
        return 0, guess



test_texts = {
    "Positive": [
        "I absolutely love this product! It exceeded my expectations.",
        "The customer service was fantastic, very helpful and friendly.",
        "I had an amazing experience, everything was perfect!",
        "This place is my favorite, the ambiance is great, and the food is delicious.",
        "I'm so happy with my purchase, the quality is outstanding.",
        "The packaging was excellent, and delivery was right on time.",
        "Highly recommend this brand! Their attention to detail is amazing.",
        "I'm thrilled with the results, way better than I imagined.",
        "This hotel is a gem! The staff went above and beyond.",
        "The quality for the price is unbeatable, totally worth it.",
    ],
    "Negative": [
        "I'm really disappointed with this product, it broke after one use.",
        "The service was terrible, they ignored us the entire time.",
        "This was a waste of money, I regret buying it.",
        "I would never recommend this place to anyone, awful experience.",
        "The event was a disaster, poorly organized and chaotic.",
        "This is the worst product I’ve ever bought. Absolute garbage.",
        "The staff was rude and unprofessional, won't be coming back.",
        "I asked for a refund, but they never responded.",
        "This app is useless, it crashes every time I try to use it.",
        "Terrible shipping experience, package arrived damaged and late."
    ]
}


good_guess = 0
count = 0
for sent, tests in test_texts.items():
    for test in tests:
        result, guess = predict_sentiment(test, sent)
        good_guess += result
        count += 1
        print(guess, test)


print("Accuracy:", good_guess/count)
