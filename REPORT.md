# CodeAlpha Data Analytics Internship — Task 1 Report

## Task 1 — Web Scraping

### Objective

Collect structured population information from a public web page and store it as a CSV dataset.

### Source

Wikipedia — List of countries and dependencies by population

https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population

### Tools Used

- Python
- Requests
- BeautifulSoup
- Pandas

### Method

1. Send an HTTP request to the public webpage using Requests.
2. Retrieve the webpage HTML.
3. Parse the HTML using BeautifulSoup.
4. Locate the table containing Location and Population information.
5. Extract the table rows and relevant columns.
6. Organize the extracted data using Pandas.
7. Save the final dataset as a CSV file.

### Data Collected

The dataset contains:

- Country / Location
- Population
- Percentage of world population
- Date
- Source

### Output

The scraped data is saved as:

`data/country_population.csv`

### Result

The web scraping process was successfully completed. The extracted population information was converted into a structured CSV dataset.

### Conclusion

This task demonstrates the use of Python web-scraping techniques to collect structured information from a publicly available webpage and store the results in a reusable CSV format.
