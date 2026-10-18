from src.AeroplanesAPI import AeroplanesAPI

api = AeroplanesAPI(
    "https://nominatim.openstreetmap.org",
    "https://opensky-network.org"
)

coords = api.get_info_about_country("Spain")
print("Координаты:", coords)

planes = api.get_info_about_plane("Spain")
print("Самолёты:", planes)