from flask import Flask, request, jsonify
from services.yt_service import evaluate_comments
from scripts.yt_api import YTScraper
from scripts.analize import predict_sentiment

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def home():
    url = request.json.get('url')
    evaluated_comments = evaluate_comments(url)
    return jsonify(evaluated_comments)

if __name__ == "__main__":
    app.run(debug=True)

