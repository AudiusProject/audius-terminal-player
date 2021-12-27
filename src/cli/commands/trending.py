import click
from src.utils import api, playback


@click.command()
# @click.option("--count", default=1, help="Number of greetings.")
# @click.option("--name", prompt="Your name", help="The person to greet.")
def trending():
    """Play the first track in trending."""
    response = api.get("tracks/trending")
    first_track = response[0]
    track_id = first_track["id"]
    playback.stream(track_id)
    click.echo(track_id)


if __name__ == "__main__":
    trending()
