import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = "https://api.github.com/search/repositories"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def search_repositories(query: str, limit: int = 5):
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }

    response = requests.get(GITHUB_API_URL, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception("GitHub API request failed")

    data = response.json()

    results = []
    for repo in data.get("items", []):
        results.append({
            "name": repo["name"],
            "url": repo["html_url"],
            "stars": repo["stargazers_count"],
            "description": repo["description"]
        })

    return results
