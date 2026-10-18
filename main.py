from src.AeroplanesAPI import AeroplanesAPI
from src.Aeroplane import Aeroplane


def user_interaction():
    country = input("Введите страну: ")
    api = AeroplanesAPI(
        "https://nominatim.openstreetmap.org",
        "https://opensky-network.org"
    )
    raw = api.get_info_about_plane(country)
    if raw is None:
        print("Страна не найдена")
        return
    planes = Aeroplane.cast_to_object_list(raw)
    n = int(input("Сколько самолетов показать: "))
    top = sorted(planes, key=lambda p: p.baro_altitude, reverse=True)[:n]
    for p in top:
        print(p)


if __name__ == "__main__":
    user_interaction()
