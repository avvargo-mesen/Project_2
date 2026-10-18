class Aeroplane:

    def __init__(
            self,
            callsign: str,
            origin_country: str,
            velocity: float,
            baro_altitude: float,
    ):
        if callsign is None:
            callsign = "Unknown"
        if origin_country is None:
            origin_country = "Unknown"
        if velocity is None:
            velocity = 0.0
        if baro_altitude is None:
            baro_altitude = 0.0

        self.callsign = str(callsign).strip()
        self.origin_country = str(origin_country)
        try:
            self.velocity = float(velocity)
        except (ValueError, TypeError):
            self.velocity = 0.0
        try:
            self.baro_altitude = float(baro_altitude)
        except (ValueError, TypeError):
            self.baro_altitude = 0.0

    def __str__(self):
        return (
            f"Позывной:{self.callsign}, страна: {self.origin_country}, "
            f"скорость: {self.velocity} м/с, высота: {self.baro_altitude} м"
        )

    def __lt__(self, other):
        result = self.velocity < other.velocity
        return result

    def __gt__(self, other):
        result = self.velocity > other.velocity
        return result

    def __le__(self, other):
        result = self.baro_altitude <= other.baro_altitude
        return result

    def __ge__(self, other):
        result = self.baro_altitude >= other.baro_altitude
        return result

    @classmethod
    def cast_to_object_list(cls, data):
        '''Метод преобразовывает базу в список'''
        planes = []
        for plane in data:
            planes.append(cls(plane[1], plane[2], plane[9], plane[7]))
        return planes
