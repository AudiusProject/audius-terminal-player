from src.libs import utils

mood_map = {
    "Peaceful": "🕊️ ",
    "Romantic": "💘",
    "Sentimental": "😢",
    "Tender": "😌",
    "Easygoing": "🙂",
    "Yearning": "👀",
    "Sophisticated": "🤓",
    "Sensual": "😘",
    "Cool": "😎",
    "Gritty": "🙎",
    "Melancholy": "🌧️ ",
    "Serious": "😐",
    "Brooding": "🤔",
    "Fiery": "🔥",
    "Defiant": "😈",
    "Aggressive": "🤬",
    "Rowdy": "👺",
    "Excited": "🎉",
    "Energizing": "💫",
    "Empowering": "💪",
    "Stirring": "😲",
    "Upbeat": "🙌",
    "Other": "🤷",
}


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
        self.duration = metadata["duration"]

    def __repr__(self):
        plays_chunk = f"🎧  {utils.numerize(self.plays):6} | "
        fav_chunk = f"💖  {utils.numerize(self.favs):5} | "
        duration_chunk = f"⏱️  {self.duration // 60:02}:{self.duration % 60:02} || "
        other_chunk = f"{self.title} {mood_map.get(self.mood, '🐸')} {self.artist} #{self.genre.replace('&', 'and').replace(' ', '_').replace('-', '_').replace('/', '_').lower() if self.genre else ''}"
        return "".join((plays_chunk, fav_chunk, duration_chunk, other_chunk))
