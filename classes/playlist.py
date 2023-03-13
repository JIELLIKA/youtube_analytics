import datetime
import isodate
from classes.channel import Channel


class PlayList(Channel):

    def __init__(self, playlist_id: str):
        """Инициализация экземпляра класса PlayList по id
        плейлиста с получением названия плейлиста и ссылки на него """
        self.playlist_id = playlist_id
        playlist_info = self.get_service().playlists().list(id=playlist_id,
                                                            part='snippet, contentDetails, status').execute()
        self.title = playlist_info['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    @property
    def get_video_id_list(self) -> list:
        """Получение списка id видео, входящих в текущий плейлист"""
        playlist_videos = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                                  part='contentDetails',
                                                                  maxResults=50,
                                                                  ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    @property
    def total_duration(self) -> datetime:
        """Расчет суммарной продолжительности видеороликов в текущем плейлисте"""
        total_duration = datetime.timedelta()
        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                          id=','.join(self.get_video_id_list)
                                                          ).execute()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self) -> None:
        """Вывод ссылки на самое популярное(по количеству лайков) видео"""
        most_likes = []
        for video_id in self.get_video_id_list:
            video_info = self.get_service().videos().list(id=video_id, part='snippet, statistics').execute()
            like_count = video_info['items'][0]['statistics']['likeCount']
            most_likes.append(int(like_count))
        best_video_likes = max(most_likes)
        i = 0
        while i < len(most_likes):
            if most_likes[i] == best_video_likes:
                print(f'https://youtu.be/{self.get_video_id_list[i]}')
            i += 1


pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(pl.title)
print(pl.url)
print(pl.total_duration)
print(type(pl.total_duration))
print(pl.total_duration.total_seconds())
pl.show_best_video()
