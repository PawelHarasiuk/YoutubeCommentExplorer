from yt_scraper import YTScraper
from analize import predict_sentiment


scraper = YTScraper()
comments_scraped = scraper.get_comments("3ao7DdYiwx0")

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


for sent, comments in comment_analise.items():
    for comment in comments:
        print(f"{sent}: {comment}")
