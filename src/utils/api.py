import requests
import random
import shutil
import tempfile

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
    return body["data"]


def get_api_endpoint():
    r = requests.get(AUDIUS_API_ENDPOINT)
    body = r.json()
    endpoints = body["data"]
    return get_random_element_from_list(endpoints)


def get_random_element_from_list(list):
    return random.choice(list)
