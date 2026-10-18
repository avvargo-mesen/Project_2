from abc import ABC, abstractmethod

class BaseSaver(ABC):
    '''Абстрактный класс, хранит данные о самолетах'''

    @abstractmethod
    def add_aeroplane(self, aeroplane):
        pass

    @abstractmethod
    def get_aeroplanes(self, criteria):
        pass


    @abstractmethod
    def delete_aeroplane(self, aeroplane):
        pass