from src.base_api import BaseAPI
import requests

class AeroplanesAPI(BaseAPI):
    '''Класс, для выхова данных страны и координат самолета через URL'''

    def __init__(self, url_nominatim, url_opensky):
        super().__init__(url_nominatim)
        self.url_opensky = url_opensky

    def get_info_about_country(self, country):
        '''Метод запрашивает расположение страны'''
        url_country = f"https://nominatim.openstreetmap.org/search?q={country}&format=json"
        response_about_country = requests.get(url_country, headers={"User-Agent": "my-app"})
        if response_about_country.status_code != 200:
            return None
        else:
            data = response_about_country.json()
            return data[0]["boundingbox"]


    def get_info_about_plane(self, country):
        '''Метод запрашивает координаты самолета'''
        coordinates = self.get_info_about_country(country)
        if coordinates == None:
            return None
        else:
            url_coordinates = f"https://opensky-network.org/api/states/all?lamin={coordinates[0]}&lomin={coordinates[2]}&lamax={coordinates[1]}&lomax={coordinates[3]}"
            response_about_coordinates = requests.get(url_coordinates)
            if response_about_coordinates.status_code != 200:
                return None
            else:
                data = response_about_coordinates.json()
                return data.get("states")




