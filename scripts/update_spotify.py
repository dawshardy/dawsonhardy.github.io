import json
import os
import time
import requests

CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
REFRESH_TOKEN = os.environ["SPOTIFY_REFRESH_TOKEN"]

def get_access_token():
    r = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["access_token"]

def api_get(url, token):
    r = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=30)
    if r.status_code == 204:
        return None
    r.raise_for_status()
    return r.json()

def main():
    token = get_access_token()

    now = api_get("https://api.spotify.com/v1/me/player/currently-playing", token)

    data = {
        "updated_at": int(time.time()),
        "is_playing": False,
        "title": None,
        "artist": None,
        "album": None,
        "track_url": None,
        "image": None,
    }

    if now and now.get("item"):
        item = now["item"]
        artists = ", ".join(a["name"] for a in item.get("artists", []))
        images = item.get("album", {}).get("images") or []
        image = images[1]["url"] if len(images) > 1 else (images[0]["url"] if images else None)

        data.update({
            "is_playing": bool(now.get("is_playing")),
            "title": item.get("name"),
            "artist": artists,
            "album": item.get("album", {}).get("name"),
            "track_url": item.get("external_urls", {}).get("spotify"),
            "image": image,
        })
    else:
        recent = api_get("https://api.spotify.com/v1/me/player/recently-played?limit=1", token)
        items = (recent or {}).get("items") or []
        if items:
            item = items[0]["track"]
            artists = ", ".join(a["name"] for a in item.get("artists", []))
            images = item.get("album", {}).get("images") or []
            image = images[1]["url"] if len(images) > 1 else (images[0]["url"] if images else None)

            data.update({
                "is_playing": False,
                "title": item.get("name"),
                "artist": artists,
                "album": item.get("album", {}).get("name"),
                "track_url": item.get("external_urls", {}).get("spotify"),
                "image": image,
            })

    os.makedirs("assets/data", exist_ok=True)
    with open("assets/data/spotify.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
