import pytest
import example

def test_can_call_existing_endpoints_of_the_API():
    assert example.get_coordinates("lima,peru") is not None
    assert example.get_distance({"lat": "0", "lon": "0"}, {"lat": "0", "lon": "0"}) is not None

def test_cannot_call_not_existing_endpoints_of_the_API():
    try:
        ret = example.get_not_existing_endpoint()
        assert False, "Should raise an exception"
    except:
        pass

def test_get_coordinates():
    assert example.get_coordinates("lima,peru") == {'lat': '-12.0621065', 'lon': '-77.0365256'}
    
def test_get_distance():
    assert example.get_distance({"lat": "0", "lon": "0"}, {"lat": "0", "lon": "0"}) == 0.0
    assert example.get_distance({"lat": "0", "lon": "0"}, {"lat": "1", "lon": "1"}) == 1.41


def test_get_coordinates_for_bogota():
    ret = example.get_coordinates("bogota,colombia")
    lat = round(float(ret['lat']), 2)
    lon = round(float(ret['lon']), 2)

    assert (lat, lon) == (4.65, -74.08), f"Expected (4.61, -74.08) but got ({lat}, {lon})"


def test_get_coordinate_for_london():
    ret = example.get_coordinates("london,england")
    lat = round(float(ret['lat']), 2)
    lon = round(float(ret['lon']), 2)

    assert (lat, lon) == (51.49, -0.14), f"Expected (51.51, -0.13) but got ({lat}, {lon})"


def test_get_distance_between_london_and_bogota():
    london = example.get_coordinates("london,england")
    bogota = example.get_coordinates("bogota,colombia")

    distance = example.get_distance(london, bogota)

    london_real = (51.49, -0.14)
    bogota_real = (4.65, -74.08)

    expected_distance = ((london_real[0] - bogota_real[0])**2 + (london_real[1] - bogota_real[1])**2)**0.5

    expected_distance = round(expected_distance, 2)

    assert distance == expected_distance, f"Expected {expected_distance} but got {distance}"


def test_get_distance_between_london_and_lima():
    london = example.get_coordinates("london,england")
    lima = example.get_coordinates("lima,peru")

    distance = example.get_distance(london, lima)

    london_real = (51.49, -0.14)
    lima_real = (-12.06, -77.04)

    expected_distance = ((london_real[0] - lima_real[0])**2 + (london_real[1] - lima_real[1])**2)**0.5

    expected_distance = round(expected_distance, 2)

    assert distance == expected_distance, f"Expected {expected_distance} but got {distance}"


def test_get_coordinates_for_not_existing_city():
    ret = example.get_coordinates("notexistingcity,notexistingcountry")
    assert ret is None, "Expected None but got {ret}"