import os
import json

from googleapiclient.discovery import build


class Channel:

    def __init__(self, channel_id):
        self.__channel_id = channel_id
        api_key: str = os.getenv('SKYPRO-API-KEY')
        api_key: str = "AIzaSyC1tWpJ3nJc8DrOcYF0NF5SjUsReRZ4Hd0"
        youtube = build('youtube', 'v3', developerKey=api_key)
        info = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.channel = info
        self.title = info['items'][0]['snippet']['title']
        self.discription = info['items'][0]['snippet']['description']
        self.url = info['items'][0]['snippet']['thumbnails']['default']['url']
        self.subs = info['items'][0]['statistics']['subscriberCount']
        self.video_count = info['items'][0]['statistics']['videoCount']
        self.view_count = info['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self) -> str:
        """Возвращаем channel id"""
        return self.__channel_id

    def print_info(self):
        channel_info = json.dumps(self.channel, indent=2, ensure_ascii=False)
        return channel_info

    @staticmethod
    def get_service():
        api_key: str = os.getenv('SKYPRO-API-KEY')
        api_key: str = "AIzaSyC1tWpJ3nJc8DrOcYF0NF5SjUsReRZ4Hd0"
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, filename):
        """Импортируем необходимые атрибуты в файл json"""
        data = {"attr1": self.title, "attr2": self.discription,
                "attr3": self.url, "attr4": self.subs, "attr5": self.video_count, "attr6": self.view_count}
        with open(filename, "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
Channel.print_info(vdud)

vdud.to_json('vdud.json')


