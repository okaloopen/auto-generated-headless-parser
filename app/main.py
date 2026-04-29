from fastapi import FastAPI, HTTPException
from pydantic import HttpUrl
import logging

from .scraper import Scraper
from .models import ScrapeRequest, ScrapeResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Headless Web Scraper API",
    description="API for scraping content from web pages using Playwright",
    version="0.1.0"
)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/scrape", response_model=ScrapeResponse)
async def scrape(request: ScrapeRequest):
    """Scrape data from a web page given a URL and CSS selector."""
    try:
        async with Scraper() as scraper:
            data = await scraper.fetch(str(request.url), request.selector)
            return ScrapeResponse(data=data)
    except Exception as e:
        logger.exception("Failed to scrape: %s", e)
        raise HTTPException(status_code=500, detail="Scraping failed")
