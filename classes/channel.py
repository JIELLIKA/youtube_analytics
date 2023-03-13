import os
import json

from googleapiclient.discovery import build


class Channel:

    def __init__(self, channel_id):
        """Инициализация экземпляра класса по id канала"""
        self.__channel_id = channel_id
        info = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.channel = info
        self.title = info['items'][0]['snippet']['title']
        self.description = info['items'][0]['snippet']['description']
        self.url = info['items'][0]['snippet']['thumbnails']['default']['url']
        self.subs = info['items'][0]['statistics']['subscriberCount']
        self.video_count = info['items'][0]['statistics']['videoCount']
        self.view_count = info['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self) -> str:
        """Возвращаем channel id"""
        return self.__channel_id

    def print_info(self):
        """Получаем информацию о канале"""
        channel_info = json.dumps(self.channel, indent=2, ensure_ascii=False)
        return channel_info

    @staticmethod
    def get_service():
        api_key: str = os.getenv('SKYPRO-API-KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, filename):
        """Импортируем необходимые атрибуты в файл json"""
        data = {"attr1": self.title, "attr2": self.description,
                "attr3": self.url, "attr4": self.subs, "attr5": self.video_count, "attr6": self.view_count}
        with open(filename, "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def __str__(self):
        """Возвращаем информацию на печать в требуемом виде"""
        return f'Youtube-канал: {self.title}'

    def __add__(self, other) -> int:
        """Складываем подписчиков двух каналов"""
        return self.subs + other.subs

    def __gt__(self, other) -> bool:
        """Возвращает True, если количество подписчиков канала 1 больше, чем 2"""
        return len(self.subs) > len(other.subs)

    def __lt__(self, other) -> bool:
        """Возвращает True, если количество подписчиков канала 2 больше, чем 1"""
        return len(self.subs) < len(other.subs)


# vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
# print(vdud.video_count)