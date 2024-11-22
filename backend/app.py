from flask import Flask, request, jsonify
from services.yt_service import evaluate_comments

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def home():
    url = request.json.get('url')
    evaluated_comments = evaluate_comments(url)
    return jsonify(evaluated_comments)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

