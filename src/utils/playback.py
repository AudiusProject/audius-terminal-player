import subprocess
from src.utils import api


def stream(track_id):
    uri = api.make_uri(f"tracks/{track_id}/stream")
    download_uri = api.get_redirect_uri(uri)
    local_filepath = api.download_file(download_uri)
    print(local_filepath)
    subprocess.call(["afplay", local_filepath])
