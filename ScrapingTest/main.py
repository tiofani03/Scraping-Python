import asyncio
import threading

from fastapi import FastAPI
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from starlette.responses import JSONResponse

from ScrapingTest.selenium.VaingloryNewsSelenium import get_selenium_data
from ScrapingTest.spiders import VaingloryNewsSpider

app = FastAPI()
scraping_queue = asyncio.Queue()

def run_scrapy():
    process = CrawlerProcess(get_project_settings())
    process.crawl(VaingloryNewsSpider, queue=scraping_queue)
    process.start()


@app.get('/')
def root():
    return {'message': 'Hello World!'}


@app.get("/scrape/scrapy", response_class=JSONResponse)
async def scrape():
    thread = threading.Thread(target=run_scrapy)
    thread.start()

    return {"message": "Scraping started!"}


@app.get("/scrape/selenium", response_class=JSONResponse)
async def scrape():
    # Menjalankan scraping dengan Selenium dan mengambil hasilnya
    data = get_selenium_data()

    if not data:
        return JSONResponse(status_code=404, content={"message": "No data found"})

    return {"message": "Scraping successful", "data": data}