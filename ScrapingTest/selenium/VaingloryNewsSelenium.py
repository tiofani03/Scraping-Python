import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_selenium_data():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    logging.info("Setting up the chromedriver with options.")

    service = Service(executable_path='/opt/homebrew/bin/chromedriver')

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logging.info("Successfully initialized Chrome driver.")
    except Exception as e:
        logging.error(f"Failed to initialize Chrome driver: {e}")
        return []

    try:
        driver.get("https://www.vainglorygame.com/news/")
        logging.info("Successfully navigated to the URL.")
    except Exception as e:
        logging.error(f"Error accessing the URL: {e}")
        driver.quit()
        return []

    time.sleep(5)

    articles = []
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, '.js-news-carousel .slide')
        logging.info(f"Found {len(elements)} elements.")

        for element in elements:
            title = element.find_element(By.CSS_SELECTOR, 'h1.white').text
            link = element.find_element(By.CSS_SELECTOR, 'a.button-big').get_attribute('href')
            image_url = element.find_element(By.CSS_SELECTOR, '.bg-image').get_attribute('style')

            if image_url:
                image_url = image_url.split('url(')[-1].split(')')[0]

            articles.append({
                'title': title,
                'link': link,
                'image_url': image_url
            })

        logging.info(f"Scraped {len(articles)} articles.")
    except Exception as e:
        logging.error(f"Error while scraping the articles: {e}")

    driver.quit()

    logging.info(f"Total articles scraped: {len(articles)}")

    return articles
