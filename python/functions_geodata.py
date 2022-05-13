from geopy.geocoders import Nominatim
import geocoder
from shapely.geometry import Point
import pandas as pd
import geopandas as gpd


def extract_geoname_coordinates_from_strings(geonames: list[str]) -> pd.DataFrame:
    data_to_save = {"name": [], "longitude": [], "latitude": []}

    for geoname in geonames:
        try:
            coordinates = get_geoname_coordinate_from_geoname(geoname)
            place_found = coordinates != (None, None)
            if place_found:
                data_to_save["name"].append(geoname)
                data_to_save["longitude"].append(float(coordinates[0]))
                data_to_save["latitude"].append(float(coordinates[1]))
            else:
                #try:
                #    coordinates = get_coordinate_from_geoname(geoname)
                #    data_to_save["name"].append(geoname)
                #    data_to_save["longitude"].append(float(coordinates[0]))
                #    data_to_save["latitude"].append(float(coordinates[1]))
                #except:
                print(f"coordinate for {geoname} could not be found")
        except:
            print(f"coordinate for {geoname} could not be found")



    dataframe = pd.DataFrame(data_to_save)

    return dataframe


def create_geodataframe_from_points(df: pd.DataFrame):
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]

    gdf = gpd.GeoDataFrame(df, geometry=geometry)

    return gdf


def get_coordinate_from_geoname(geoname: str):
    geolocator = Nominatim(user_agent="Savoirs")

    location = geolocator.geocode(geoname)
    return location.longitude, location.latitude


def get_geoname_coordinate_from_geoname(geoname: str):
    geolocator = geocoder.geonames(geoname, key='syrdak')

    longitude, latitude = geolocator.lng, geolocator.lat

    return longitude, latitude
