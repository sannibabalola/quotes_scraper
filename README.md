# 🕸️ Quote Scraper (BeautifulSoup + Python)

## Overview  
Web scraping is a valuable skill that helps automate and streamline data collection tasks. From extracting job listings to gathering news articles or quotes, web scraping enables you to focus on only the most relevant data — avoiding noise and manual effort.  

This project is a **static web scraping Python script** built using the **BeautifulSoup** library. It extracts data (quotes, authors, and source links) from a quote website and stores the results in a structured CSV file.

---

## Features  
- Extracts **quotes, authors, and links** from each page of the website  
- Uses **BeautifulSoup** for parsing and extracting HTML content  
- Saves extracted data using **pandas** into CSV format  
- Implements **time delays** between requests to mimic human browsing and avoid server overload  
- Utilizes the **datetime** library to timestamp each output file, preventing overwriting of existing data  
- Supports **pagination** — automatically continues to the next page until no more quotes are found  

---

## Technologies Used  
- **Python 3**  
- **BeautifulSoup (bs4)**  
- **Requests**  
- **Pandas**  
- **Time & Datetime**

---

## How It Works  
1. The script connects to the target URL (`https://quotes.toscrape.com/`).  
2. It scrapes all quotes, authors, and links on the page.  
3. Automatically continues to the next page until no more data is found.  
4. Saves results in a timestamped `.csv` file for easy reference.  

---

## Output Example  
Each CSV file contains columns for:  
| Quote | Author | Link |
|--------|---------|------|
| "The world as we have created it..." | Albert Einstein | /author/Albert-Einstein |

---

## Key Takeaways  
This project demonstrates:  
- How to use **BeautifulSoup** to parse HTML content  
- How to **handle pagination** effectively  
- How to **structure scraped data** with pandas  
- How to implement **ethical scraping practices** using delays  

---

## How to Run the Script

### Clone This Repository
```bash
# Clone the repository
git clone https://github.com/sannibabalola/quotes_scraper.git

# Navigate into the project folder
cd quotes_scraper
