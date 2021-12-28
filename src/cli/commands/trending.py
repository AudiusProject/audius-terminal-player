import click
from src.utils import api, playback
from src.tui.renderers.Track import Track
from src.tui.components.Table import render


def playtrack(selection):
    playback.stream(selection.id)


@click.command()
@click.option("--rank", default=1, help="rank of trending track to play")
def trending(rank):
    """Play any track in trending."""
    index = rank - 1
    response = api.get("tracks/trending")
    track = response[index]
    track_id = track["id"]
    playback.stream(track_id)


if __name__ == "__main__":
    # trending() # TODO should we keep this?
    trending_tracks = api.get("tracks/trending")
    trending_tracks_formatted = [Track(track) for track in trending_tracks]
    render("Trending tracks", 8, 8, trending_tracks_formatted, playtrack)
