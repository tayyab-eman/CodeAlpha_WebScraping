# CodeAlpha Data Analytics Internship — Web Source Project

This project contains all 4 CodeAlpha Data Analytics tasks, using public web sources.

## Tasks and sources

### Task 1 — Web Scraping
Source: Wikipedia — List of countries and dependencies by population
https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population

Tools: Requests, BeautifulSoup, Pandas

Output:
`data/country_population.csv`

### Task 2 — Exploratory Data Analysis (EDA)
Source: Our World in Data — Population, 1950 to 2023
https://ourworldindata.org/grapher/population-unwpp

Tools: Pandas, NumPy, Matplotlib

Output:
`outputs/task2_eda_summary.txt`

### Task 3 — Data Visualization
Source: Our World in Data — Population, 1950 to 2023
https://ourworldindata.org/grapher/population-unwpp

Outputs:
- `outputs/task3_top10_population_2023.png`
- `outputs/task3_population_trend.png`
- `outputs/task3_world_population_growth.png`

### Task 4 — Sentiment Analysis
Source: UCI Machine Learning Repository — Sentiment Labelled Sentences
https://archive.ics.uci.edu/dataset/331/sentiment+labelled+sentences

The UCI dataset contains 3,000 positive/negative review sentences from IMDb, Amazon and Yelp. This project uses VADER, a lexicon-based sentiment method, to produce positive/negative/neutral labels.

Output:
`outputs/task4_sentiment_results.csv`

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python task1_web_scraping.py
python task2_eda.py
python task3_visualization.py
python task4_sentiment_analysis.py
```

## Important
The scripts download/read public data when they are run. Keep the source links in the README and report so the dataset origin is clear.

Do not upload your `.venv` folder to GitHub.
