import json
import os
import base64
import requests

OUTPUT_FILE = "assets/data/spotify.json"


def get_access_token():

    client_id = os.environ["SPOTIFY_CLIENT_ID"]
    client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
    refresh_token = os.environ["SPOTIFY_REFRESH_TOKEN"]

    basic = base64.b64encode(
        f"{client_id}:{client_secret}".encode()
    ).decode()

    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
    )

    response.raise_for_status()

    return response.json()["access_token"]


def get_now_playing(token):

    r = requests.get(
        "https://api.spotify.com/v1/me/player/currently-playing",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    if r.status_code == 204:
        return {"is_playing": False}

    if r.status_code != 200:
        return {"is_playing": False}

    data = r.json()

    item = data["item"]

    return {
        "is_playing": data["is_playing"],
        "title": item["name"],
        "artist": item["artists"][0]["name"],
        "album": item["album"]["name"],
        "album_art": item["album"]["images"][0]["url"],
        "url": item["external_urls"]["spotify"],
    }


def main():

    token = get_access_token()

    now_playing = get_now_playing(token)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(now_playing, f, indent=2)


if __name__ == "__main__":
    main()
