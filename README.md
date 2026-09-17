# CodeAlpha Data Analytics Internship — Task 1: Web Scraping

## Objective

The objective of this task is to collect structured data from a publicly available web page using Python web scraping techniques.

## Source

Wikipedia — List of countries and dependencies by population

https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population

## Tools Used

- Python
- Requests
- BeautifulSoup
- Pandas

## Data Collected

The following information was extracted from the webpage:

- Country / Location
- Population
- Percentage of world population
- Date
- Source

## Output

The scraped dataset is saved as:

`data/country_population.csv`

## Method

1. Sent a request to the public webpage using Requests.
2. Retrieved the webpage HTML.
3. Used BeautifulSoup to locate the population table.
4. Extracted the table rows and relevant columns.
5. Used Pandas to organize the extracted data.
6. Saved the final dataset as a CSV file.

## Result

The web scraping process was successfully completed and the extracted population data was saved in CSV format.

## Project

This repository contains the source code and output dataset for CodeAlpha Data Analytics Internship — Task 1.
