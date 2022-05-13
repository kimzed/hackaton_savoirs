import os
import unicodedata
import random
import csv


def get_file_paths(dir_files: str) -> list[str]:
    list_files = []

    for path in os.listdir(dir_files):
        full_path = os.path.join(dir_files, path)
        if os.path.isfile(full_path):
            list_files.append(full_path)

    return list_files


def remove_duplicates_from_list(list_to_clean: list) -> list:
    clean_list = []

    for element in list_to_clean:
        if element not in clean_list:
            clean_list.append(element)

    return clean_list


def get_random_element_from_list(elements: list):
    number_elements = len(elements)
    i_random_element = random.randint(0, number_elements)
    random_element = elements[i_random_element]

    return random_element


def ordering_dict_by_values(data: dict) -> dict:
    """ every key must have only one value """
    data_out = dict(sorted(data.items(), key=lambda item: item[1]))

    return data_out


def get_file_name_from_path(path: str) -> str:
    path_items = path.split("/")
    file_name = path_items[-1]

    return file_name


def open_text_file(path: str):
    f = open(path, "w")
    f.write("")
    f.close()


def append_to_csv_file(file_path: str, elements: list):
    with open(file_path, 'a') as file:
        write = csv.writer(file)
        write.writerow(elements)


def write_elements_to_csv(elements: list, file_path: str):
    with open(file_path, 'a') as file:
        write = csv.writer(file)
        write.writerow(elements)


def write_dictionary_to_csv(data: dict, file_path: str):
    # we want to overwrite the file if it exists already
    with open(file_path, "w") as f:
        None


    for key in data:
        data_to_save = []
        data_to_save.append(key)
        # in our case there is only one value inside
        data_to_save += [str(data[key])]

        write_elements_to_csv(data_to_save, file_path)
