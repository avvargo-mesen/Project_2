from abc import ABC, abstractmethod

class BaseAPI(ABC):
    '''Абстрактный класс, хранит URL'''
    def __init__(self, url):
        self.url= url

    @abstractmethod
    def get_info_about_country(self, country):
        pass

    @abstractmethod
    def get_info_about_plane(self, country):
        pass