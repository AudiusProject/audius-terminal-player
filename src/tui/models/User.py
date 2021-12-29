from src.libs import utils


class User:
    def __init__(self, metadata):
        self.id = metadata["id"]
        self.handle = metadata["handle"]
        self.bio = metadata["bio"] or ""
        self.bio = self.bio.replace("\n", " ")
        self.follower_count = metadata["follower_count"]
        self.followee_count = metadata["followee_count"]
        self.location = metadata["location"]
        self.album_count = metadata["album_count"]
        self.playlist_count = metadata["playlist_count"]
        self.repost_count = metadata["repost_count"]
        self.track_count = metadata["track_count"]

    def __repr__(self):
        return " ".join(
            (
                f"👤  {self.handle}",
                f"📍  {self.location}",
                f"👥  {self.follower_count}",
                f"🎵  {self.track_count}",
                f"💿  {self.album_count}",
                f"💬  {self.bio}",
                f"📜  {self.playlist_count}",
                f"🔁  {utils.numerize(self.repost_count):5} |",
            )
        )
