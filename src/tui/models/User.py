from src.libs import utils


class User:
    def __init__(self, metadata):
        self.id = metadata["id"]
        self.handle = metadata["handle"]
        self.bio = metadata["bio"] or ""
        self.bio = self.bio.replace("\n", " ")
        self.follower_count = metadata["follower_count"]
        self.followee_count = metadata["followee_count"]
        self.location = metadata["location"] or "Location Unknown"
        self.album_count = metadata["album_count"]
        self.playlist_count = metadata["playlist_count"]
        self.repost_count = metadata["repost_count"]
        self.track_count = metadata["track_count"]

    def __repr__(self):
        return " | ".join(
            (
                f"👤 {self.handle if len(self.handle) < 16 else self.handle[:16] + '...':^20}",
                f"📍 {self.location if len(self.location) < 20 else self.location[:20] + '...':^24}",
                f"👥 {utils.numerize(self.follower_count):6}",
                f"🎵 {utils.numerize(self.track_count):3}",
                f"💿 {utils.numerize(self.album_count):3}",
                f"📜 {utils.numerize(self.playlist_count):3}",
            )
        )
