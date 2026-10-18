from src.AeroplanesAPI import AeroplanesAPI
from src.Aeroplane import Aeroplane
from src.JSONSaver import JSONSaver


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
    try:
        n = int(input("Сколько самолетов показать: "))
    except ValueError:
        print("Нужно ввести число")
        return
    top = sorted(planes, key=lambda p: p.baro_altitude, reverse=True)[:n]

    saver = JSONSaver("aeroplanes.json")
    for plane in top:
        print(plane)
        saver.add_aeroplane(plane)


if __name__ == "__main__":
    user_interaction()
