Amazon Web Scraper

A Python-based web scraper that tracks and visualizes the price history of any Amazon product using Selenium.

FEATURES
	•	Scrape the current price of an Amazon product via its URL
	•	Store daily price data to a CSV file
	•	Visualize price trends over time (supports up to 1 year)
	•	Easy to extend with automation (e.g., GitHub Actions or cron)
	•	Modular, clean codebase with separate files for scraping, saving, and plotting

PROJECT STRUCTURE

Amazon-web-scraper/
├── scraper.py            - Scrapes price using Selenium
├── price_tracker.py      - Saves and loads price history
├── plot_price.py         - Plots the price trend
├── data/                 - Stores product-specific CSVs and plots
│   └── B0XXXXXXX.csv
├── requirements.txt      - All Python dependencies
└── README.md             - This file

GETTING STARTED
	1.	Clone the repository

git clone https://github.com/jake-armstrong07/Amazon-web-scraper.git
cd Amazon-web-scraper
	2.	Install dependencies

Make sure you have Python 3.8+ and ChromeDriver installed.
Run the following command:

pip install -r requirements.txt
	3.	Scrape a price

In scraper.py, use the get_price(url) function:

from scraper import get_price
url = “https://www.amazon.com/dp/B0XXXXXXX”
price = get_price(url)
print(“Current Price:”, price)
	4.	Save the price

from price_tracker import save_price
product_id = “B0XXXXXXX”
save_price(product_id, price)
	5.	Plot the trend

Run:

python plot_price.py

SAMPLE OUTPUT

A line plot showing the price history over time is saved to:
data/B0XXXXXXX_plot.png

NOTES
	•	Works on Amazon.com, .co.uk, and other domains (as long as the price selectors match)
	•	Scraper uses Selenium with headless Chrome — avoid overusing to prevent being blocked
	•	For persistent use, consider automating the script with a daily scheduler

DISCLAIMER

This project is for educational purposes only. Scraping Amazon violates their Terms of Service. Use responsibly and consider the Amazon Product Advertising API for production use.

CONTACT

Built by Jake Armstrong (https://github.com/jake-armstrong07)
Have questions or want to contribute? Open an issue or fork the repo!
