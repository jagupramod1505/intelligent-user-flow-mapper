# Intelligent User Flow Mapper

## Objective
Build a smart crawler that extracts meaningful user navigation flows from a website.

## Features
- Crawls internal links only  
- Avoids infinite loops  
- Supports configurable depth  
- Removes global navigation noise  
- Outputs clean JSON for UI visualization  

## How to run

Install dependencies:
pip install -r requirements.txt

Run server:
uvicorn app.main:app --reload

Call API:
POST /crawl
Body:
{
  "start_url": "https://example.com",
  "max_depth": 3
}
