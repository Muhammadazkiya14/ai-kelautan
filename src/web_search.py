import os
import requests
from dotenv import load_dotenv

load_dotenv()

def search_web(query, max_results=3):
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        return ""

    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": api_key,
        "num": max_results,
        "hl": "id",
        "gl": "id"
    }

    try:
        resp = requests.get(url, params=params, timeout=15)
        data = resp.json()

        results = []
        for item in data.get("organic_results", [])[:max_results]:
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            link = item.get("link", "")
            results.append(f"[{title}]\n{snippet}\nSumber: {link}\n")

        return "\n".join(results) if results else ""
    except Exception as e:
        print(f"Pencarian web error: {e}")
        return ""
