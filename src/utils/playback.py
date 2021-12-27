import subprocess
from src.utils import api


def stream(track_id):
    uri = api.make_uri(f"tracks/{track_id}/stream")
    track_data = api.get(f"tracks/{track_id}")
    artist_handle = track_data["user"]["handle"]
    track_name = track_data["title"]
    download_uri = api.get_redirect_uri(uri)
    print("Track buffering... be patient ⌛")
    local_filepath = api.download_file(download_uri)
    print(f"Playing {track_name} by {artist_handle} - enjoy! ✨")
    subprocess.call(["afplay", local_filepath])
