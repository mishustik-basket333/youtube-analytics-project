import datetime
import isodate
from src.channel import Youtube


# from googleapiclient.discovery import build
# import os


class PlayList(Youtube):
    """class PlayList"""

    # api_key: str = os.getenv('YT_API_KEY')
    # youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.__url = "https://www.youtube.com/playlist?list=" + f"{self.__playlist_id}"
        # self.__playlist = self.youtube.playlists().list(
        #     id=self.__playlist_id, part='contentDetails, snippet',maxResults=50,
        # ).execute()
        self.__playlist = self.get_playlist(self.__playlist_id)
        self.__title = self.__playlist["items"][0]["snippet"]['title']

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def playlist(self):
        return self.__playlist

    def get_all_video_id_in_playlist(self):
        """Функция возвращает список с айди каналов"""
        box_id = []
        playlist = self.get_playlist_videos(self.__playlist_id)
        for video in playlist["items"]:
            box_id.append(video['contentDetails']['videoId'])
        return box_id
        # video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist['items']]
        # return video_ids

    @property
    def total_duration(self):
        """Функция возвращает сумму времени всех видео в плейлисте """
        delta = datetime.timedelta()
        video_ids = self.get_all_video_id_in_playlist()
        video_response = self._youtube.videos().list(part='contentDetails,statistics',
                                                     id=','.join(video_ids)).execute()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            delta += duration
        return delta

    def show_best_video(self):
        """Функция возвращает url канала с наибольшим колличество лайков"""
        max_likes_video = 0
        url_max_likes_video = ""
        video_ids = self.get_all_video_id_in_playlist()
        video_response = self._youtube.videos().list(part='contentDetails,statistics',
                                                     id=','.join(video_ids)).execute()
        for video in video_response["items"]:
            if max_likes_video < int(video['statistics']['likeCount']):
                max_likes_video = int(video['statistics']['likeCount'])
                url_max_likes_video = video['id']
        #     print(video)
        # return print(max_likes_video, url_max_likes_video)
        return f"https://youtu.be/{url_max_likes_video}"


# if __name__ == '__main__':
    # pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    # lalala = pl.show_best_video()
    # print(pl.title)
    # print(pl.url)
    # print(pl.get_all_video_id_in_playlist())
    # print(pl.total_duration)
    # print(lalala)
