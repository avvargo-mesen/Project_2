from src.Aeroplane import Aeroplane
from src.JSONSaver import JSONSaver
import pytest
from src.base_api import BaseAPI
from src.AeroplanesAPI import AeroplanesAPI

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
    list_raw = [[None, "TVF44KH", "France", None, None, None, None, 11567.16, None, 232.57, None, None, None, None, None, None, None, None]]
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



