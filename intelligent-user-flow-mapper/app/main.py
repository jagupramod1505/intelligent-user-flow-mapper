from fastapi import FastAPI
from pydantic import BaseModel
from crawler import crawl_site
from flow_analyzer import build_user_flow

app = FastAPI()

class CrawlRequest(BaseModel):
    start_url: str
    max_depth: int = 3

@app.post("/crawl")
def crawl(request: CrawlRequest):
    pages = crawl_site(request.start_url, request.max_depth)
    flow = build_user_flow(pages)
    return flow
