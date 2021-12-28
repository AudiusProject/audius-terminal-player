import subprocess
from src.libs import api


def stream(track_id, progress_callback, finish_loading_callback):
    progress_callback()
    uri = api.make_uri(f"tracks/{track_id}/stream")
    download_uri = api.get_redirect_uri(uri)
    local_filepath = api.download_file(download_uri, finish_loading_callback)
    stop()
    subprocess.Popen(["afplay", local_filepath])


def stop():
    subprocess.call(
        ["killall", "afplay"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
