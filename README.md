# Hackathon Savoirs

Spatial analysis and reading recommendation system for the Savoirs digital humanities corpus.

## Overview

Analyzes the [Savoirs](https://savoirs.app/) French academic corpus by extracting geographic references from TEI/XML-encoded articles, geocoding place names, and computing spatial similarity between articles. Articles that discuss geographically related topics are surfaced as reading recommendations.

## Tech Stack

- **Geospatial:** GeoPandas, Shapely, Geopy (Nominatim), Geocoder (GeoNames API)
- **XML Processing:** BeautifulSoup with lxml parser
- **Data Processing:** Pandas
- **Data Format:** GeoPackage (GPKG)

## Pipeline

```
TEI/XML Corpus (~100 articles)
    ↓
Extract place names from <placename> tags
    ↓
Geocode locations (GeoNames API + Nominatim fallback)
    ↓
Save as GeoPackage (one per article)
    ↓
Compute pairwise spatial distances between articles
    ↓
Export similarity rankings as CSV
```

## Project Structure

```
hackaton_savoirs/
├── python/
│   ├── pre_processing.py        # Geocoding pipeline (TEI → GeoPackage)
│   ├── main.py                  # Pairwise distance computation
│   ├── functions_xml.py         # TEI/XML extraction (titles, authors, places)
│   ├── functions_geodata.py     # Geocoding and GeoDataFrame creation
│   ├── geo_article.py           # GeoArticle class for spatial similarity
│   ├── functions.py             # General utilities
│   └── tests/                   # Unit tests
├── CorpusTEI/                   # Input: TEI-encoded articles (ANABASES journal)
└── data/
    ├── article_locations/       # Output: GeoPackage files per article
    └── distances/               # Output: CSV distance matrices
```

## Usage

```bash
# Stage 1: Geocode place names from TEI corpus
python python/pre_processing.py

# Stage 2: Compute pairwise article distances
python python/main.py
```

## Context

Built during the **Hackathon Savoirs** for challenges on the Savoirs corpus: extracting knowledge through text mining, spatial analysis, and data visualization, and designing reading recommendation strategies based on geographic and thematic similarity.
