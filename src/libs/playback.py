import subprocess
from src.libs import api


def stream(track_id):
    uri = api.make_uri(f"tracks/{track_id}/stream")
    download_uri = api.get_redirect_uri(uri)
    local_filepath = api.download_file(download_uri)
    stop()
    subprocess.Popen(["mpv", local_filepath])


def stop():
    subprocess.call(
        ["killall", "mpv"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
