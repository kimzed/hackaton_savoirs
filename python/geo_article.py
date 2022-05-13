import python.functions_geodata as functions_geodata
import geopandas as gpd
import numpy as np
from shapely.geometry import Point
import python.functions as functions


class GeoArticle():
    def __init__(self, path_geo_file: str):
        self.points_article = gpd.read_file(path_geo_file)
        # key will be name of the other article
        self.distances_to_articles = {}

    def save_distance_to_article(self, other_geo_article, name_article: str):
        point_distances_to_article = []
        number_points = len(self.points_article)
        for i_point in range(number_points):
            point = self.get_point(i_point)
            minimum_distance_to_article = self.get_minimum_distance_to_article(point, other_geo_article)

            point_distances_to_article.append(minimum_distance_to_article)

        mean_distance = np.array(point_distances_to_article).mean()
        name_article = functions.get_file_name_from_path(name_article)
        self.distances_to_articles[name_article] = mean_distance

    @staticmethod
    def get_minimum_distance_to_article(point, other_geo_article):
        """ the distance is made with WGS84, so not in meters """
        distances = []
        number_points = len(other_geo_article.points_article)
        for i_point_other in range(number_points):
            point_other = other_geo_article.get_point(i_point_other)
            distance = point_other.distance(point)
            distances.append(distance)

        minimum_distance = np.array(distances).min()

        return minimum_distance

    def get_point(self, i_point: int) -> Point:

        point = self.points_article.iloc[i_point]["geometry"]

        return point
