# Headless Web Scraper

## Overview

This project provides an asynchronous headless web scraper built with **FastAPI** and **Playwright**.  The service exposes a simple HTTP API for scraping web pages and extracting elements by CSS selector. It is designed for concurrent requests and can be extended to support more complex parsing logic.

## Features

- Asynchronous HTTP API using FastAPI.
- Headless browser automation with Playwright.
- Simple API endpoint to scrape a given URL and CSS selector.
- Data validation with Pydantic models.
- Structured logging for observability.
- Modular architecture with separate modules for the web server and scraping logic.

## Architecture Overview

```
app/
├── main.py       # FastAPI application and endpoints.
├── scraper.py    # Scraper class using Playwright.
├── models.py     # Pydantic models for request and response.
└── __init__.py   # Package initializer.

```

The `Scraper` class encapsulates browser management and page extraction. The FastAPI app in `main.py` creates routes to invoke the scraper and return results as JSON.

## Installation

1. Clone the repository and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Install Playwright browsers:

   ```bash
   playwright install
   ```

## Usage

Run the API service:

```bash
uvicorn app.main:app --reload
```

Then make a request to scrape a page:

```bash
curl 'http://localhost:8000/scrape?url=https://example.com&selector=h1'
```

The service returns JSON with the extracted text.

## API Documentation

| Endpoint      | Method | Description                                       | Parameters                            |
|---------------|--------|---------------------------------------------------|---------------------------------------|
| `/health`     | GET    | Health check endpoint                             | –                                     |
| `/scrape`     | GET    | Scrape a URL and extract text by CSS selector     | `url`: target page URL (str), `selector`: CSS selector (str) |

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve functionality.

## License

This project is licensed under the MIT License.
