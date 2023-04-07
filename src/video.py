from src.channel import Youtube
from googleapiclient.errors import HttpError


class Video(Youtube):
    """Класс Video"""
    def __init__(self, video_id):
        try:
            self.__video_id = video_id
            self.video_response = self.get_video(self.__video_id)
            self.video_title: str = self.video_response['items'][0]['snippet']['title']
            self.url = "https://www.youtube.com/channel/" + f"{self.__video_id}"
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
            self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']

        except HttpError as error_msg:
            print(error_msg, "HttpError")
            self.__video_id = video_id
            self.video_response = self.video_title = self.url = self.title = None
            self.view_count = self.like_count = self.comment_count = None

        except IndexError as error_msg:
            print(error_msg, "IndexError")
            self.__video_id = video_id
            self.video_response = self.video_title = self.url = self.title = None
            self.view_count = self.like_count = self.comment_count = None

    def __str__(self):
        return self.video_title


class PLVideo(Video, Youtube):
    """"""

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        # self.playlist_videos = self._youtube.playlistItems().list(playlistId=self.playlist_id,
        #                                                          part='contentDetails', maxResults=50, ).execute()
        self.playlist_videos = self.get_playlist_videos(playlist_id)
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]


# if __name__ == '__main__':
#     video1 = Video('9lO06Zxhu88')  # '9lO06Zxhu88' - это id видео из ютуб
#     video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
#     assert str(video1) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
#     assert str(video2) == 'Пушкин: наше все?'
#     print(str(video1))
#     print(str(video2))
#     print(video1.url)
#     print(video2.playlist_videos)
