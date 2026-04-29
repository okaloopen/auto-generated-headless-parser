import logging
from typing import List
from playwright.async_api import async_playwright

logger = logging.getLogger(__name__)

class Scraper:
    """Asynchronous headless web scraper using Playwright."""

    def __init__(self) -> None:
        self.playwright = None
        self.browser = None

    async def __aenter__(self) -> "Scraper":
        # Start Playwright and launch a headless browser
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        # Close browser and stop Playwright
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    async def extract(self, url: str, selector: str) -> List[str]:
        """Fetches the given URL and returns a list of text contents matching the CSS selector."""
        if self.browser is None:
            raise RuntimeError("Browser not initialized. Use async with Scraper() context.")
        page = await self.browser.new_page()
        try:
            await page.goto(url, wait_until="domcontentloaded")
            elements = await page.query_selector_all(selector)
            results: List[str] = []
            for element in elements:
                text = await element.inner_text()
                if text:
                    results.append(text.strip())
            logger.info("Extracted %d items from %s", len(results), url)
            return results
        finally:
            await page.close()
