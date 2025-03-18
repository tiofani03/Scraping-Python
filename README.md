# FastAPI Scraping with Selenium and Scrapy

This project is a web application built with **FastAPI** that integrates **Scrapy** for performing web scraping on the [Vainglory Game News](https://www.vainglorygame.com/news/) website. The application provides an endpoint to scrape Vainglory news articles using **Scrapy** and returns the data in JSON format.

## Features

- Uses **FastAPI** to build a REST API.
- Uses **Scrapy** for scraping data from the Vainglory News page.
- Extracts article information, including:
  - Title
  - Link
  - Image URL
- Uses **Chromium** and **Chromium WebDriver** for scraping.

## Installation

### 1. Clone the Project

Clone this project into your local directory using git:

```bash
git clone https://github.com/tiofani03/Scraping-Python.git
cd Scraping-Python
```

### 2. Set Up a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required dependencies from `requirement.txt`:

```bash
pip install -r requirement.txt
```

### 4. Install Chromium and Chromedriver

To use Selenium with Chromium, you need to have **Chromium** and **Chromedriver** installed on your system.

- Install **Chromium** using your system's package manager or download it from [Chromium's official site](https://www.chromium.org/getting-involved/download-chromium).
  
- Install **Chromedriver** that corresponds to your **Chromium** version. You can get it from [Chromium WebDriver](https://sites.google.com/a/chromium.org/chromedriver/).

Ensure **Chromium** and **Chromedriver** are installed and accessible from the terminal.

### 5. Configure WebDriver Path

Make sure to set the correct path to the `chromedriver` executable in your code, for example:

```python
service = Service(executable_path='/opt/homebrew/bin/chromedriver')
```

You can use the full path to the `chromedriver` installed in your system.

## Running the Application

After setting up the environment and installing dependencies, you can start the application using **Uvicorn**:

```bash
uvicorn ScrapingTest.main:app --reload
```

This will start the FastAPI application at `http://127.0.0.1:8000`.

## Endpoints

- **GET /scrape/scrapy**: Scrapes data from Vainglory Game News using **Scrapy** and returns the result in JSON format.
- **GET /scrape/selenium**: Scrapes data from Vainglory Game News using **Selenium** and returns the result in JSON format.

Example of scraping data from Scrapy endpoint:

```bash
http://127.0.0.1:8000/scrape/scrapy
```

## Evidence
- Scraping with scrapy and save to local json
<img width="906" alt="image" src="https://github.com/user-attachments/assets/c7e39f42-6430-4c03-92fa-f6471186ac24" />
<br> <br>
- Scraping with selenium and display to json
<img width="963" alt="image" src="https://github.com/user-attachments/assets/898f4edc-374a-422b-b7d0-9971e7ad38f8" />


