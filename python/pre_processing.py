import python.functions_xml as functions_xml
import python.functions_geodata as functions_geodata
import python.functions as functions
import warnings

warnings.filterwarnings("ignore")


def main():
    directory_xml_files = "C:/Users/57834/Documents/savoirs/space_names/CorpusTEI/"

    files = functions.get_file_paths(directory_xml_files)


    for i_file, file in enumerate(files):


        geo_names = functions_xml.get_geo_names_from_xml(file)

        folder_coordinate = "C:/Users/57834/Documents/savoirs/HackathonSavoirs/python/data/article_locations/"
        file_coordinate = functions.get_file_name_from_path(file)
        file_path_coordinate = folder_coordinate + file_coordinate + ".gpkg"

        df_coordinates = functions_geodata.extract_geoname_coordinates_from_strings(geo_names)

        gdf_coordinates = functions_geodata.create_geodataframe_from_points(df_coordinates)
        try:
            gdf_coordinates.to_file(
                file_path_coordinate,
                layer="spacenames_article",
                driver="GPKG",
                crs="EPSG:4326",
            )
        except:
            print(f"file {file} does not have nameplaces")


if __name__ == "__main__":
    main()
