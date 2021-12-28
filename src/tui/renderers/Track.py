class Track:
    def __init__(self, metadata):
        self.id = metadata["id"]
        self.artist = metadata["user"]["handle"]
        self.title = metadata["title"]
        self.reposts = metadata["repost_count"]
        self.genre = metadata["genre"]
        self.mood = metadata["mood"]
        self.favs = metadata["favorite_count"]
        self.plays = metadata["play_count"]
        self.duration = int(metadata["duration"] // 60)

    def __str__(self):
        return f"{self.artist} / {self.title} / {self.genre} / {self.mood} / 🔁 {self.reposts} / 💖 {self.favs} / 🎧 {self.plays} / ⌛ {self.duration}"
