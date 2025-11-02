# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time  # use for delays
from datetime import datetime  # use for timestamp


# define target url
base_url = "https://quotes.toscrape.com/"

# headers help your scraper look like a real browser
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    )
}


def find_quotes():
    quotes = []
    page = 1

    while True:
        url = f"{base_url}?page={page}"
        print(f"Scraping {url}...")
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch site {page} ({response.status_code})")
            continue

        soup = BeautifulSoup(response.text, "lxml")
        collection = soup.find_all("div", class_="quote")

        if not collection:
            print("No more pages found, scraping complete.")
            break

        # extract quote data
        for quote in collection:
            text = quote.find("span", class_="text").get_text(
                strip=True) if quote.find("span", class_="text") else None
            author = quote.find("small", class_="author").get_text(
                strip=True) if quote.find("small", class_="author") else None
            link = quote.find("a").get('href') if quote.find("a") else None

            quotes.append({
                "Quote": text,
                "Author": author,
                "Link": link
            })

        print(f"Page {page} scraped successfully ({len(collection)} quotes).")

        print("\nPress Q to quit the program or C to continue to the next page:")
        user_input = input().strip().lower()
        if user_input == "q":
            print("Exiting the script and saving results...")
            break

        page += 1
        time.sleep(1)

    # Save all quotes after scraping is done
    if quotes:
        df = pd.DataFrame(quotes)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"quotes_output_{timestamp}.csv"
        df.to_csv(filename, index=False, encoding="utf-8")
        print(f"Scraped {len(df)} quotes and saved to {filename}")
    else:
        print("No quotes scraped.")


if __name__ == '__main__':
    find_quotes()
