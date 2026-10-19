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
    if planes == []:
        print("Самолётов не найдено")
        return
    try:
        n = int(input("Сколько самолетов показать: "))
        if n <= 0:
            print("Введите положительое число отличное от 0")
            return
        else:
            top = sorted(planes, key=lambda p: p.baro_altitude,
                         reverse=True)[:n]
    except ValueError:
        print("Нужно ввести число")
        return

    reg_country = input("Введите страну регистрации: ")
    if reg_country != "":
        filtered_list = []
        for plane in top:
            if plane.origin_country == reg_country:
                filtered_list.append(plane)
    else:
        filtered_list = top

    if not filtered_list:
        print("Самолётов с такой страной регистрации не найдено")
        return

    saver = JSONSaver("aeroplanes.json")
    for plane in filtered_list:
        print(plane)
        saver.add_aeroplane(plane)


if __name__ == "__main__":
    user_interaction()
