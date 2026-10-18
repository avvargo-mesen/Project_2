from src.Saver import BaseSaver
import json

class JSONSaver(BaseSaver):
    def __init__(self, filename):
        self.filename = filename

    def add_aeroplane(self, aeroplane):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        data.append(aeroplane.__dict__)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


    def get_aeroplanes(self, criteria):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return []

        result = []
        for plane in data:
            match = True
            for key, value in criteria.items():
                if plane.get(key) != value:
                    match = False
                    break
            if match:
                result.append(plane)
        return result

    def delete_aeroplane(self, aeroplane):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return

        new_data = []
        callsign  = aeroplane.callsign
        for plane in data:
            if plane["callsign"] != callsign:
                new_data.append(plane)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)