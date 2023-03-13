from classes.channel import Channel


class Video(Channel):
    def __init__(self, video_id: str) -> None:
        """Инициализация экземпляра класса Video по id видео"""
        video_info = self.get_service().videos().list(id=video_id, part='snippet, statistics').execute()
        self.video_name = video_info['items'][0]['snippet']['title']
        self.video_count = video_info['items'][0]['statistics']['viewCount']
        self.like_count = video_info['items'][0]['statistics']['likeCount']


# video1 = Video('cIs7N8B300M')
# print(video1.like_count)
