from src.libs import utils


class Playlist:
    def __init__(self, metadata):
        self.id = metadata["id"]
        self.creator = metadata["user"]["handle"]
        self.name = metadata["playlist_name"]
        self.reposts = metadata["repost_count"]
        self.description = metadata["description"] or "No description"
        self.favs = metadata["favorite_count"]
        self.plays = metadata["total_play_count"]

    def __repr__(self):
        return " ".join(
            (
                f"💖  {utils.numerize(self.favs):5} |",
                f"🔁  {utils.numerize(self.reposts):5} |",
                f"💽  {self.name}",
                f"📝  {self.description}",
                f"👤  {self.creator}",
            )
        )
