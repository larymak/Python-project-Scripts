import json
import httpx
from urllib.parse import quote
from typing import Dict
import jmespath

client = httpx.Client(
    headers={
        "x-ig-app-id": "936619743392459",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
    }
)

def scrape_user_id(username: str):
    """Scrape Instagram user's data"""
    result = client.get(
        f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}",
    )
    data = json.loads(result.content)
    user_data = data["data"]["user"]
    user_id = user_data.get("id")
    return user_id

def parse_post(data: Dict) -> Dict:
    result = jmespath.search("""{
        shortcode: shortcode,
        likes: edge_media_preview_like.count,
        comments: edge_media_to_comment.count
    }""", data)
    return result

def scrape_user_posts(user_id: str, session: httpx.Client, page_size=12):
    base_url = "https://www.instagram.com/graphql/query/?query_hash=e769aa130647d2354c40ea6a439bfc08&variables="
    variables = {
        "id": user_id,
        "first": page_size,
        "after": None,
    }
    _page_number = 1
    while True:
        resp = session.get(base_url + quote(json.dumps(variables)))
        all_posts_data = resp.json()
        posts = all_posts_data["data"]["user"]["edge_owner_to_timeline_media"]
        for post in posts.get("edges"):
            yield parse_post(post.get("node"))  # note: we're using parse_post function from previous chapter
        page_info = posts.get("page_info")
        if _page_number == 1:
            print(f"scraping total {posts['count']} posts of {user_id}")
        else:
            print(f"scraping page {_page_number}")
        if not page_info["has_next_page"]:
            break
        if variables["after"] == page_info["end_cursor"]:
            break
        variables["after"] = page_info["end_cursor"]
        _page_number += 1


def get_all_posts(user_id):
    with httpx.Client(timeout=None) as session:
        posts = list(scrape_user_posts(str(user_id), session))
        return posts