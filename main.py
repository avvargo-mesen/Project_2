from src.AeroplanesAPI import AeroplanesAPI
from src.Aeroplane import Aeroplane

api = AeroplanesAPI(
    "https://nominatim.openstreetmap.org",
    "https://opensky-network.org"
)

raw = api.get_info_about_plane("Spain")
planes = Aeroplane.cast_to_object_list(raw)

print(planes[0])
print(planes[0].callsign)