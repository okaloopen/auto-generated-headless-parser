from pydantic import BaseModel, HttpUrl
from typing import List

class ScrapeRequest(BaseModel):
    """Request model for scraping."""
    url: HttpUrl
    selector: str

class ScrapeResponse(BaseModel):
    """Response model containing extracted data."""
    data: List[str]
