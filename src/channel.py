from googleapiclient.discovery import build
import json
import os


# import isodate


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_111 = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel_111["items"][0]["snippet"]['title']
        self.description = self.channel_111["items"][0]["snippet"]['description']
        self.url = "https://www.youtube.com/channel/" + f"{channel_id}"
        self.subscriber_сount = self.channel_111["items"][0]["statistics"]["viewCount"]
        self.video_count = self.channel_111["items"][0]["statistics"]["videoCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_111)

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Класс-метод возвращающий объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, file_json):
        f"""Сохраняет данные о канале в файл {file_json}.json в формате .json"""
        data = {"api_key": Channel.api_key,
                "channel_id": self.__channel_id,
                "title:": self.title,
                "description": self.description,
                "url": self.url,
                "subscriber_сount": self.subscriber_сount,
                "video_count": self.video_count}
        data = json.dumps(data)
        my_file = open(f"{file_json}", "w+")
        my_file.write(data)
        my_file.close()

# vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
# vdud.print_info()
#
# print("test")
# print(vdud.title)
# print(vdud.description)
# print(vdud.url)
# print(vdud.subscriber_сount)
# print(vdud.video_count)
# print(vdud._Channel__channel_id)
# vdud.channel_id = 'Новое название'
# print(vdud._Channel__channel_id)
# print(dir(vdud))
