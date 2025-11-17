# day20_api_error_handling
# Use JSONPlaceholder API; show params and error handling

import requests

def fetch_posts(user_id=None):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {}
    if user_id:
        params["userId"] = user_id
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()  # raises HTTPError for 4xx/5xx
        posts = r.json()
        print(f"Fetched {len(posts)} posts (userId={user_id})")
        # print first 2 post titles
        for p in posts[:2]:
            print("-", p["title"])
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
    except Exception as e:
        print("Other error:", e)

if __name__ == "__main__":
    fetch_posts(user_id=1)
