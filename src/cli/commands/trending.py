import click
from src.libs import api, playback, utils


@click.command()
@click.option("--rank", default=1, help="rank of trending track to play")
def trending(rank):
    """Play any track in trending."""
    index = rank - 1
    response = api.get("tracks/trending")
    track = response[index]
    track_id = track["id"]
    playback.stream(track_id, utils.noop, utils.noop)


if __name__ == "__main__":
    trending()
