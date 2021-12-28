import subprocess
from src.utils import api


def stream(track_id, progress_callback, finish_loading_callback):
    uri = api.make_uri(f"tracks/{track_id}/stream")
    download_uri = api.get_redirect_uri(uri)
    progress_callback()
    local_filepath = api.download_file(download_uri, finish_loading_callback)
    subprocess.Popen(["afplay", local_filepath])


def stop():
    subprocess.call(
        ["killall", "afplay"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
