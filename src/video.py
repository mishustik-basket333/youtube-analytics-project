from googleapiclient.discovery import build
import os


class Video:
    """Класс Video"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.__video_id = video_id
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=self.__video_id).execute()
        self.video_title: str = self.video_response['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/channel/" + f"{self.__video_id}"
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']

    def __str__(self):
        return self.video_title


class PLVideo(Video):
    """"""

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                                 part='contentDetails', maxResults=50, ).execute()
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
