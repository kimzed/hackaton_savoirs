import geopandas as gpd
import python.functions as functions
import python.functions_geodata as functions_geodata
import python.geo_article as geo_article

directory_geo_files = "C:/Users/57834/Documents/savoirs/space_names/python/data/article_locations/"
directory_distances = "C:/Users/57834/Documents/savoirs/space_names/python/data/distances/"


def main():
    files = functions.get_file_paths(directory_geo_files)

    for file in files:
        article_points = geo_article.GeoArticle(file)

        for file_to_compare in files:
            file_is_same = file_to_compare == file
            if file_is_same:
                continue
            article_points_to_compare = geo_article.GeoArticle(file_to_compare)
            article_points.save_distance_to_article(other_geo_article=article_points_to_compare,
                                                    name_article=file_to_compare)

        data_distances = functions.ordering_dict_by_values(article_points.distances_to_articles)

        file_distance = functions.get_file_name_from_path(file) + "_distances_to_articles.csv"
        file_path_distance = directory_distances + file_distance
        functions.write_dictionary_to_csv(data_distances, file_path_distance)


if __name__ == "__main__":
    main()
