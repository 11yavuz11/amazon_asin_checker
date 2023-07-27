# Amazon ASIN Scraper with Python Scrapy

## Overview

This is a Python Scrapy scraper tool designed to retrieve ASIN (Amazon Standard Identification Number) numbers of products from a given Amazon product page. The scraper utilizes the `scraperapi.com` service to handle data retrieval and sequentially stores the results in an Excel file.

## Requirements

- Python 3.x
- `scrapy` library
- `pandas` library
- `openpyxl` library
- A valid `scraperapi.com` API key (available as a free version or with appropriate subscription plans)

## Installation

1. Download or clone the project files to your local machine.

2. Open a terminal/command prompt and navigate to the project directory.

3. Install the required Python packages using the following command:

   ```bash
   pip install scrapy pandas openpyxl


## Usage
1. Create a file named urls.txt and add the URLs of the Amazon product pages you wish to scrape. Each URL should be placed on a separate line, leading to a product listing page.

2. Configure the necessary settings in the settings.py file:

	* SCRAPER_API_KEY: Insert your scraperapi.com API key here.

	* OUTPUT_FILE: Specify the file path where you want to save the results as an Excel file.

3. To start the scraper, run the following command in the terminal:
	* python3 spider_name.py

4. The scraper will navigate between pages with random delays to avoid bot detection.

5. Once the scraping process is complete, the ASIN numbers will be sequentially saved to the Excel file specified in OUTPUT_FILE

## Important Notes:
	* The scraperapi.com service offers a free tier with usage limitations, so be mindful of your usage to stay within the provided limits.

	* When scaling this tool or adding more advanced features, consider adhering to robots.txt guidelines and Amazon's terms of use to avoid potential legal issues.

	* This scraper is intended for educational purposes only. Amazon has strict policies regarding data scraping, so use this tool responsibly and in compliance with ethical guidelines.

Feel free to reach out if you need any further assistance or have any questions!