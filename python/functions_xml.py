import python.functions as functions
from bs4 import BeautifulSoup
import re


def get_title(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as tei_xml:
        data_puller = BeautifulSoup(tei_xml, 'lxml')

    title_elements = data_puller.find_all('title')

    title_elements = clean_string_elements_from_xml(title_elements)

    title_elements = functions.remove_duplicates_from_list(title_elements)

    title_output = " ".join(title_elements[0:2])

    return title_output


def get_author(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as tei_xml:
        data_puller = BeautifulSoup(tei_xml, 'lxml')

    author_elements = data_puller.find_all(['forename', 'surname'])

    author_elements = clean_string_elements_from_xml(author_elements)

    first_names = ' '.join(author_elements[0:2])

    return first_names


def get_tag_elements_from_xml(xml_file_path: str, tag: str) -> list[str]:
    with open(xml_file_path, 'r', encoding='utf-8') as tei_xml:
        data_puller = BeautifulSoup(tei_xml, 'lxml')

    elements_from_tag = data_puller.find_all(tag)

    return elements_from_tag


def find_if_tag_exists_in_xml(xml_file_path: str, tag: str) -> bool:
    tags = get_list_tags_from_xml(xml_file_path)

    return tag in tags


def get_list_tags_from_xml(xml_file_path: str) -> list[str]:
    with open(xml_file_path, 'r', encoding='utf-8') as tei_xml:
        data_puller = BeautifulSoup(tei_xml, 'lxml')

    list_tags = []
    for tag in data_puller.findAll(True):
        list_tags.append(tag.name)

    list_tags = list(set(list_tags))

    return list_tags


def clean_string_elements_from_xml(elements: list[str]) -> list[str]:
    elements_cleaned = []

    for element in elements:
        text_element = element.text
        text_element = re.sub(r"\n", r" ", text_element)
        text_element = re.sub(r"\xa0", r" ", text_element)
        text_element = re.sub(r"                    ", r"", text_element)
        text_element = re.sub(r"            ", r"", text_element)
        text_element = re.sub(r"        ", r"", text_element)
        text_element_cleaned = re.sub(r"    ", r"", text_element)

        elements_cleaned.append(text_element_cleaned)

    return elements_cleaned


def get_geo_names_from_xml(xml_file_path: str):
    with open(xml_file_path, 'r', encoding='utf-8') as tei_xml:
        data_puller = BeautifulSoup(tei_xml, 'lxml')

    geonames = []
    for tag in data_puller.findAll(True):
        if tag.name == "placename":
            geonames.append(tag.text)

    # removing duplicates
    geonames = list(set(geonames))
    return geonames


def get_geo_tags_from_xml(xml_file_path: str):
    with open(xml_file_path, 'r', encoding='utf-8') as tei_xml:
        data_puller = BeautifulSoup(tei_xml, 'lxml')

    geonames = []
    for tag in data_puller.findAll(True):
        if tag.name == "placename":
            geonames.append(tag)

    # removing duplicates
    geonames = list(set(geonames))
    return geonames
