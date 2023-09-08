# Savoirs GIS-Based Text Analysis


## Description:

This repository contains code and data used for the spatial analysis of articles from the Savoirs digital library. Through the "Spatial Imaginary" approach, this project assesses the proximity of articles based on their geographical mentions, providing a unique spatial representation of the corpus.

## Repository Structure:

hackaton_savoirs/
├── CorpusTEI
│   ├── ANABASES-1437_Bonnet.xml
│   ├── ... (other XML data files)
├── python
│   ├── data (folder containing processed data)
│   ├── functions_geodata.py (functions for geo data processing)
│   ├── functions.py (general utility functions)
│   ├── functions_xml.py (functions for XML data handling)
│   ├── geo_article.py (class definition for article geo-analysis)
│   ├── main.py (main script to execute analysis)
│   ├── pre_processing.py (pre-processing functions)
│   ├── unit_test (unit tests for the project)
└── README.md (this file)


## Getting Started:

1. Clone this repository.
2. Ensure required libraries such as geopy, geocoder, shapely, pandas, and geopandas are installed.
3. Navigate to the python folder and run main.py.

