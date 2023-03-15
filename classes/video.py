from classes.channel import Channel


class Video(Channel):
    def __init__(self, video_id: str) -> None:
        """Инициализация экземпляра класса Video по id видео"""
        try:
            video_info = self.get_service().videos().list(id=video_id, part='snippet, statistics').execute()
            self.video_name = video_info['items'][0]['snippet']['title']
            self.video_count = video_info['items'][0]['statistics']['viewCount']
            self.like_count = video_info['items'][0]['statistics']['likeCount']
        except Exception:
            self.video_name = None
            self.video_count = None
            self.like_count = None


if __name__ == "__main__":
    # video1 = Video('cIs7N8B300M')
    # print(video1.like_count)

    broken_video = Video('broken_video_id')
    print(broken_video.video_name)
    print(broken_video.like_count)
