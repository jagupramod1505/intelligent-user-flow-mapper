from fastapi import FastAPI
from pydantic import BaseModel
from app.site_crawler import crawl_site
from app.noise_filter import remove_global_links

app = FastAPI()

class CrawlRequest(BaseModel):
    start_url: str
    max_depth: int = 3

@app.post("/crawl")
def crawl(request: CrawlRequest):
    pages = crawl_site(request.start_url, request.max_depth)
    flow = build_user_flow(pages)
    return flow
