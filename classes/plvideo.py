from classes.video import Video


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id) -> None:
        """Инициализация экземпляра класса PLVideo с наследованием от Video"""
        super().__init__(video_id)
        playlists = self.get_service().playlists().list(id=playlist_id,
                                                        part='snippet, contentDetails, status').execute()
        self.playlist_name = playlists['items'][0]['snippet']['title']

# video1 = Video('9lO06Zxhu88')
# video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
# print(video1.video_name)
# print(f'{video2.video_name} ({video2.playlist_name})')
