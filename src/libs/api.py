import shutil
import tempfile
import requests
from src.libs import utils

AUDIUS_API_ENDPOINT = "https://api.audius.co"

TEMP_DIR = tempfile.gettempdir()


def make_uri(path):
    api_endpoint = get_api_endpoint()
    uri = f"{api_endpoint}/v1/{path}"
    return uri


def download_file(uri, done):
    temp = tempfile.NamedTemporaryFile(delete=False, dir=TEMP_DIR)
    with requests.get(uri, stream=True) as r:
        with open(temp.name, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    done()
    return temp.name


def get_redirect_uri(uri):
    r = requests.head(uri, allow_redirects=True)
    return r.url


def get(path, payload={}):
    payload["app_name"] = "audius-cli"
    uri = make_uri(path)
    r = requests.get(uri, params=payload)
    body = r.json()
    return body.get("data", [])


def get_api_endpoint():
    r = requests.get(AUDIUS_API_ENDPOINT)
    body = r.json()
    endpoints = body["data"]
    return utils.get_random_element_from_list(endpoints)
