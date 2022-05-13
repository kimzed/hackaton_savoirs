import python.functions_geodata as functions_geodata

def test_extract_geoname_coordinates_from_strings_fake_place_returns_error():

    geoname = ["weofijweoifj"]
    coordinates = functions_geodata.extract_geoname_coordinates_from_strings(geoname)


test_extract_geoname_coordinates_from_strings_fake_place_returns_error()