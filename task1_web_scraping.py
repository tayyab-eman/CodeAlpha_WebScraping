"""
CodeAlpha Task 1 — Web Scraping

Public source:
https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population

The script downloads the HTML page, finds the population table,
extracts rows and saves a clean CSV file.
"""

from pathlib import Path
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
OUTPUT = Path("data/country_population.csv")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    headers = {
        "User-Agent": "CodeAlpha-DataAnalytics-Student-Project/1.0"
    }

    print("Connecting to source website...")
    response = requests.get(URL, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    target = None
    for table in soup.find_all("table"):
        first_row = table.find("tr")
        if first_row:
            text = first_row.get_text(" ", strip=True).lower()
            if "location" in text and "population" in text:
                target = table
                break

    if target is None:
        raise RuntimeError("Population table was not found.")

    rows = []
    for row in target.find_all("tr"):
        cells = row.find_all(["th", "td"])
        values = [c.get_text(" ", strip=True) for c in cells]
        if len(values) >= 5:
            rows.append(values[:5])

    if len(rows) < 2:
        raise RuntimeError("No usable records were extracted.")

    df = pd.DataFrame(
        rows[1:],
        columns=["country", "population", "world_percentage", "date", "source"]
    )

    df["country"] = df["country"].str.strip()
    df = df[df["country"].ne("")].copy()

    # Remove thousands separators and convert population to numeric where possible.
    df["population"] = (
        df["population"]
        .str.replace(",", "", regex=False)
        .str.replace(" ", "", regex=False)
    )
    df["population"] = pd.to_numeric(df["population"], errors="coerce")

    df = df.dropna(subset=["population"])
    df.to_csv(OUTPUT, index=False, encoding="utf-8-sig")

    print("\nTASK 1 COMPLETED")
    print(f"Records collected: {len(df)}")
    print(f"Saved to: {OUTPUT}")
    print("\nFirst 10 rows:")
    print(df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
