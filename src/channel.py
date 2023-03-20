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
        self.subscriber_сount = self.channel_111["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel_111["items"][0]["statistics"]["videoCount"]
        self.view_vount = self.channel_111["items"][0]["statistics"]["viewCount"]

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

    def __str__(self):
        """Функция возвращает строку с названием и ссылку на канал по шаблону `<название_канала> (<ссылка_на_канал>)`"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Функция берет из экземпляров класса Chanel количество подписчиков и складывает их,
         возвращая и присваивая общее значение в типе данных int к первому операнду, указанному в сложении
         """
        if not isinstance(other, Channel):
            raise TypeError("Операнд справа должен иметь тип данных Chanell")
        return int(self.subscriber_сount) + int(other.subscriber_сount)

    def __sub__(self, other):
        """Функция берет из экземпляров класса Chanel количество подписчиков.
         Вычитает из первого указанного экземпляра второй экземпляр.
         Возвращает и присваивает результат в типе данных int к первому операнду, указанному в сложении
         """
        if not isinstance(other, Channel):
            raise TypeError("Операнд справа должен иметь тип данных Chanell")
        return int(self.subscriber_сount) - int(other.subscriber_сount)

    def __ge__(self, other):
        """Функция берет из экземпляров класса Chanel количество подписчиков.
         Возвращает True, если значение первого операнда больше или равно значению второго,
         иначе возвращает False
         """
        if not isinstance(other, Channel):
            raise TypeError("Операнд справа должен иметь тип данных Chanell")
        data_1, data_2 = int(self.subscriber_сount), int(other.subscriber_сount)
        if data_1 >= data_2:
            return True
        return False

# if __name__ == "__main__":
#     vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
#     redactsiya = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
#     print(vdud.print_info())
#     print(vdud.subscriber_сount)
#     print(redactsiya.subscriber_сount)
#     # Используем различные магические методы
#     print(vdud)  # 'вДудь (https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA)'
#     print(vdud + redactsiya)  # 13970000
#     print(vdud - redactsiya)  # 6630000
#     print(redactsiya - vdud)  # -6630000
#     print(vdud >= redactsiya)
#     print(redactsiya >= vdud)# True
#     vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
#     vdud.print_info()
#
#     print("test")
#     print(vdud.title)
#     print(vdud.description)
#     print(vdud.url)
#     print(vdud.subscriber_сount)
#     print(vdud.video_count)
#     print(vdud._Channel__channel_id)
#     vdud.channel_id = 'Новое название'
#     print(vdud._Channel__channel_id)
#     print(dir(vdud))
