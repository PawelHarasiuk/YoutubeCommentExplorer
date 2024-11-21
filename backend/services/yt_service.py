from scripts.yt_api import YTScraper
from scripts.analize import predict_sentiment

scraper = YTScraper()

def evaluate_comments(url):
    video_id = scraper.extract_video_id(url)
    comments_scraped = scraper.get_comments(video_id)

    comment_analise = {
        "Positive": [],
        "Negative": []
    }

    for comment in comments_scraped:
        guess = predict_sentiment(comment)
        if guess == 0:
            comment_analise["Negative"].append(comment)
        else:
            comment_analise["Positive"].append(comment)

    return comment_analise