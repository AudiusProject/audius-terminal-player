import shutil
import tempfile
import requests
from src.libs import utils
import concurrent.futures

AUDIUS_API_ENDPOINT = "https://api.audius.co"

TEMP_DIR = tempfile.gettempdir()


def make_uri(path):
    api_endpoint = get_api_endpoint()
    uri = f"{api_endpoint}/v1/{path}"
    return uri


def download_file(uri):
    temp = tempfile.NamedTemporaryFile(delete=False, dir=TEMP_DIR)
    with requests.get(uri, stream=True) as r:
        with open(temp.name, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    return temp.name


def get_redirect_uri(uri):
    r = requests.head(uri, allow_redirects=True)
    return r.url


def get(path, payload={}):
    payload["app_name"] = "audius-cli"
    uri = make_uri(path)
    r = requests.get(uri, params=payload)
    body = r.json()
    if not r.ok:  # not 2xx
        return None
    return body.get("data", [])


def search_entity(entity_type):
    def search(query):
        search_params = {"query": query}
        path = f"{entity_type}/search"
        return get(path, search_params)

    return search


def get_api_endpoint():
    r = requests.get(AUDIUS_API_ENDPOINT)
    body = r.json()
    endpoints = body["data"]
    return utils.get_random_element_from_list(endpoints)


def get_playlist_tracks(playlist_id):
    path = f"playlists/{playlist_id}/tracks"
    return get(path)


def get_user_tracks(user_id):
    path = f"users/{user_id}/tracks"
    return get(path)


def get_favorite_tracks(user_id):
    path = f"/users/{user_id}/favorites"
    favorite_pointers = get(path)
    favorite_track_ids = [
        fav["favorite_item_id"]
        for fav in favorite_pointers
        if fav["favorite_type"] == "SaveType.track"
    ]
    favs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        track_fetch_futures = {
            executor.submit(get, f"tracks/{id}"): id for id in favorite_track_ids
        }
        for future in concurrent.futures.as_completed(track_fetch_futures, timeout=30):
            result = future.result()
            favs.append(result)

    return [fav for fav in favs if fav]


def get_reposted_tracks(user_id):
    path = f"/users/{user_id}/reposts"
    all_reposts = get(path)
    track_reposts = [
        repost["item"] for repost in all_reposts if repost["item_type"] == "track"
    ]
    return track_reposts


def get_trending():
    path = "tracks/trending"
    return get(path)
