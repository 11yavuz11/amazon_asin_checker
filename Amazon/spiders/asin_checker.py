import scrapy
import random
import time
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class AmazonSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        with open('urls.txt', 'r') as f:
            urls = f.read().splitlines()

        for url in urls:
            full_url = f"https://api.scraperapi.com/?api_key={self.settings.get('SCRAPER_API_KEY')}&url={url}"
            yield scrapy.Request(full_url)

    def parse(self, response):
        # In this section, you can perform operations with the data from the response.
        # For example, you can take action here to pull the part where the products are listed or to get other data.

        # Now let's call the "next_page" files and continue browsing the pages.
        yield from self.next_page(response)

    def next_page(self, response):
        disabled_text = response.xpath('//span[contains(@class, "s-pagination-disabled")]/text()').extract()

        # Get the value "2" from the list
        desired_value = None
        for text in disabled_text:
            if text.isdigit():
                desired_value = int(text)
                break

        # We generate new URLs by looping pages 1 through for each page
        for page_num in range(1, desired_value):
            # Let's add a random delay (from 0.5 to 1.5 seconds)
            time.sleep(random.uniform(1, 2.5))

            # Combine desired_value and response.url to create full URL
            new_url = f"{response.url}&page={page_num}"
            yield scrapy.Request(new_url, callback=self.asin_checker)

    def asin_checker(self, response):
        asin = response.css('div[data-asin]')
        asin_list = []
        for div in asin:
            data_asin_value = div.attrib['data-asin']
            if data_asin_value:
                asin_list.append(data_asin_value)

        # Let's check the current Excel file.
        output_file = self.settings.get('OUTPUT_FILE')
        try:
            existing_df = pd.read_excel(output_file, sheet_name='Sheet1')
            existing_asin_list = existing_df['ASIN'].tolist()
            asin_list = existing_asin_list + asin_list
        except (FileNotFoundError, KeyError):
            pass

        # We create a DataFrame that will write all ASIN data on separate lines
        df = pd.DataFrame({'ASIN': asin_list})

        # Let's write DataFrame to Excel file
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            try:
                # If existing Excel file, let's update the sheet
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            except ValueError:
                # If the file does not exist, let's create a new page and write the ASINs
                df.to_excel(writer, sheet_name='Sheet1', index=False)

if __name__ == "__main__":
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(AmazonSpider)
    process.start()
