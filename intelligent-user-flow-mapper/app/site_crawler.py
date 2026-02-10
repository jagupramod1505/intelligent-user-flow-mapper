import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_site(start_url, max_depth=3):
    visited = set()
    result = {}

    def crawl(url, depth):
        if depth > max_depth or url in visited:
            return
        visited.add(url)

        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            links = []
            for a in soup.find_all("a", href=True):
                full_url = urljoin(url, a["href"])
                if urlparse(full_url).netloc == urlparse(start_url).netloc:
                    links.append(full_url)

            result[url] = links

            for link in links:
                crawl(link, depth + 1)

        except Exception as e:
            print(f"Error crawling {url}: {e}")

    crawl(start_url, 0)
    return result
