from src.libs import utils

MOOD_MAP = {
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

GENRE_MAP = {
    "Electronic": "electronic",
    "Rock": "rock",
    "Metal": "metal",
    "Alternative": "alternative",
    "Hip-Hop/Rap": "hip_hop_rap",
    "Experimental": "experimental",
    "Punk": "punk",
    "Folk": "folk",
    "Pop": "pop",
    "Ambient": "ambient",
    "Soundtrack": "soundtrack",
    "World": "world",
    "Jazz": "jazz",
    "Acoustic": "acoustic",
    "Funk": "funk",
    "R&B/Soul": "r_and_b_soul",
    "Devotional": "devotional",
    "Classical": "classical",
    "Reggae": "reggae",
    "Podcasts": "podcasts",
    "Country": "country",
    "Spoken Word": "spoken_work",
    "Comedy": "comedy",
    "Blues": "blues",
    "Kids": "kids",
    "Audiobooks": "audiobooks",
    "Latin": "latin",
    "Techno": "techno",
    "Trap": "trap",
    "House": "house",
    "Tech House": "tech_house",
    "Deep House": "deep_house",
    "Disco": "disco",
    "Electro": "electro",
    "Jungle": "jungle",
    "Progressive House": "progressive_house",
    "Hardstyle": "hardstyle",
    "Glitch Hop": "glitch_hop",
    "Trance": "trance",
    "Future Bass": "future_bass",
    "Future House": "future_house",
    "Tropical House": "tropical_house",
    "Downtempo": "downtempo",
    "Drum & Bass": "drum_and_bass",
    "Dubstep": "dubstep",
    "Jersey Club": "jersey_club",
    "Vaporwave": "vaporwave",
    "Moombahton": "moombahton",
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

    def __repr__(self):  # cheran's cursed code
        return " ".join(
            (
                f"🎧  {utils.numerize(self.plays):6} |",
                f"💖  {utils.numerize(self.favs):5} |",
                f"⏱️  {self.duration // 60:02}:{self.duration % 60:02} ||",
                self.title,
                MOOD_MAP.get(self.mood, "🐸"),
                self.artist,
                f"#{GENRE_MAP.get(self.genre, 'other')}",
            )
        )  # cheran is amazing
