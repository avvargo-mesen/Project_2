from src.Aeroplane import Aeroplane
from src.JSONSaver import JSONSaver
import pytest
from src.base_api import BaseAPI
from src.AeroplanesAPI import AeroplanesAPI
from src.Saver import BaseSaver


def test_aeroplane_init():
    plane = Aeroplane("TVF44KH", "France", 232.57, 11567.16)
    assert plane.callsign == "TVF44KH"
    assert plane.origin_country == "France"
    assert plane.velocity == 232.57
    assert plane.baro_altitude == 11567.16


def test_aeroplane_lt():
    plane1 = Aeroplane("A", "France", 100, 1000)
    plane2 = Aeroplane("B", "France", 200, 2000)
    assert plane1 < plane2


def test_aeroplane_gt():
    plane1 = Aeroplane("A", "France", 100, 1000)
    plane2 = Aeroplane("B", "France", 200, 2000)
    assert plane2 > plane1


def test_aeroplane_le():
    plane1 = Aeroplane("A", "France", 100, 1000)
    plane2 = Aeroplane("B", "France", 200, 2000)
    assert plane1 <= plane2


def test_aeroplane_ge():
    plane1 = Aeroplane("A", "France", 100, 1000)
    plane2 = Aeroplane("B", "France", 200, 2000)
    assert plane2 >= plane1


def test_cast_to_object_list():
    list_raw = [
        [None, "TVF44KH", "France", None, None, None, None, 11567.16, None, 232.57, None, None, None, None, None, None,
         None, None]]
    planes = Aeroplane.cast_to_object_list(list_raw)
    assert len(planes) == 1
    assert isinstance(planes[0], Aeroplane)
    assert planes[0].callsign == "TVF44KH"


def test_add_aeroplane():
    saver = JSONSaver("test_aeroplanes.json")
    plane = Aeroplane("TVF44KH", "France", 232.57, 11567.16)
    saver.add_aeroplane(plane)
    result = saver.get_aeroplanes({"callsign": "TVF44KH"})
    assert len(result) == 1


def test_delete_aeroplane():
    saver = JSONSaver("test_aeroplanes.json")
    plane = Aeroplane("TVF44KH", "France", 232.57, 11567.16)
    saver.add_aeroplane(plane)
    saver.delete_aeroplane(plane)
    result = saver.get_aeroplanes({"callsign": "TVF44KH"})
    assert len(result) == 0


def test_base_api_abstract():
    with pytest.raises(TypeError):
        BaseAPI("url")


def test_aeroplane_none():
    plane = Aeroplane(None, None, None, None)
    assert plane.callsign == "Unknown"
    assert plane.velocity == 0.0

def test_aeroplane_str():
    plane = Aeroplane("A", "France", 100, 1000)
    assert "A" in str(plane)

def test_aeroplane_bad_float():
    plane = Aeroplane("A", "France", "abc", "xyz")
    assert plane.velocity == 0.0
    assert plane.baro_altitude == 0.0

def test_jsonsaver_broken_json():
    with open("broken.json", "w", encoding="utf-8") as f:
        f.write("not a json")

    saver = JSONSaver("broken.json")

    plane = Aeroplane("A", "France", 100, 1000)
    saver.add_aeroplane(plane)
    result = saver.get_aeroplanes({"callsign": "A"})
    assert len(result) == 1

    saver.delete_aeroplane(plane)

def test_get_info_about_country(monkeypatch):
    class FakeResponse:
        status_code = 200

        def json(self):
            return [{"boundingbox": ["1", "2", "3", "4"]}]

    def fake_get(url_country, headers=None):
        return FakeResponse()

    monkeypatch.setattr("requests.get", fake_get)
    api = AeroplanesAPI("url1", "url2")
    result = api.get_info_about_country("Spain")
    assert result == ["1", "2", "3", "4"]

def test_get_info_about_country_empty(monkeypatch):
    class FakeResponse:
        status_code = 200

        def json(self):
            return []

    def fake_get(url, headers=None):
        return FakeResponse()

    monkeypatch.setattr("requests.get", fake_get)
    api = AeroplanesAPI("url1", "url2")
    result = api.get_info_about_country("Nowhere")
    assert result is None

def test_base_saver():
    with pytest.raises(TypeError):
        BaseSaver()

def test_top_n_desc():
    plane1 = Aeroplane("A", "France", 100, 1000)
    plane2 = Aeroplane("B", "France", 200, 3000)
    plane3 = Aeroplane("C", "France", 300, 2000)

    planes = [plane1, plane2, plane3]
    top = sorted(planes, key=lambda p: p.baro_altitude, reverse=True)
    assert top[0].baro_altitude == 3000
    assert top[1].baro_altitude == 2000
    assert top[2].baro_altitude == 1000

    top2 = top[:2]
    assert len(top2) == 2
    assert top2[0].baro_altitude == 3000

def test_filter_by_country():
    plane1 = Aeroplane("A", "France", 100, 1000)
    plane2 = Aeroplane("B", "Germany", 200, 3000)
    plane3 = Aeroplane("C", "France", 300, 2000)

    planes = [plane1, plane2, plane3]
    reg_country = "France"
    filtered = [p for p in planes if p.origin_country == reg_country]
    assert len(filtered) == 2
    assert filtered[0].origin_country == "France"
    assert filtered[1].origin_country == "France"


