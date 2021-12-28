import py_cui
from datetime import date
from src.libs import api, playback
from src.tui.renderers.Track import Track
from src.tui.components.NowPlaying import NowPlaying
from src.tui.components.Table import Table

DISPLAY_MENU_PAGES = {
    "Trending": {
        "api_endpoint": "tracks/trending",
        "renderer": Track,
        "title": "🌋 Trending Tracks 🚀",
        # "select_callback": playtrack,
    },
    "Search Tracks": {
        "api_endpoint": "tracks/search",
        "renderer": Track,
        "title": "🔎 Search Tracks",
        # "select_callback": playtrack
    },
    "Search Users": {
        "api_endpoint": "users/search",
        "renderer": Track,  # TODO
        "title": "🔎 Search Users",
        # "select_callback": playtrack
    },
    "Search Playlists": {
        "api_endpoint": "playlists/search",
        "renderer": Track,  # TODO
        "title": "🔎 Search Playlists",
        # "select_callback": playtrack
    },
}

NAV_MENU_CONFIG = {
    "options": DISPLAY_MENU_PAGES.keys(),
    "title": "🧭 Navigation 🔭",
}


class Player:
    def __init__(self):
        root = py_cui.PyCUI(6, 6)
        current_year = date.today().year
        app_title = f"🎵 Audius Terminal Music Player 🎵 ©️ {current_year}"
        root.set_title(app_title)
        self.root = root
        self.current_display = "Trending"
        self.current_track = {}
        root.add_key_command(py_cui.keys.KEY_CTRL_C, playback.stop)
        self.render()

    def render(self):
        self.nav_menu = self.render_nav_menu()
        self.display_menu = self.render_display(self.current_display)
        self.now_playing = self.render_now_playing()
        self.root.start()

    def render_now_playing(self):
        return NowPlaying(self, 0, 0, 3, 2, 0, 0, self.stop_track)

    def render_nav_menu(self):
        options = NAV_MENU_CONFIG["options"]
        title = NAV_MENU_CONFIG["title"]
        t = Table(self, title, 0, 3, 3, 2, options, self.select_display)
        return t

    def select_display(self, selection):
        print(f"DISPLAY SELECTED! {selection}")

    def render_display(self, type):
        details = DISPLAY_MENU_PAGES[type]
        items = api.get(details["api_endpoint"])
        items_formatted = [details["renderer"](item) for item in items]
        t = Table(
            self,
            details["title"],
            2,
            0,
            6,
            4,
            items_formatted,
            self.playtrack,
        )
        return t

    def playtrack(self, selection, buffer_callback, finish_loading_callback):
        self.current_track = selection
        playback.stream(self.current_track.id, buffer_callback, finish_loading_callback)
        self.render_now_playing()

    def stop_track(self):
        playback.stop()
        self.current_track = {}
        self.render_now_playing()
