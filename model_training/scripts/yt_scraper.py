import googleapiclient.discovery
from dotenv import load_dotenv
import re
import os

class YTScraper:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv("API_KEY")
        self.youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=self.API_KEY)

    def get_comments(self, video_id):
        comments = []
        request = self.youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            maxResults=100
        )

        while request:
            response = request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)

            request = self.youtube.commentThreads().list_next(request, response)

        return comments

    def extract_video_id(self, url):
        pattern = r'(?<=v=)([a-zA-Z0-9_-]+)'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            return None