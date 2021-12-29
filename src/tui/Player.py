import py_cui
from datetime import date
from src.libs import api, playback
from src.tui.models.Track import Track
from src.tui.models.Playlist import Playlist
from src.tui.models.User import User
from src.tui.components.NowPlaying import NowPlaying
from src.tui.components.Table import Table

CONSTANTS = {
    "TRENDING_TRACKS": "🌋 Trending Tracks 🚀",
    "SEARCH_TRACKS": "🎼 Search Tracks 🔎",
    "SEARCH_USERS": "👥 Search Users 🔎",
    "SEARCH_PLAYLISTS": "📜 Search Playlists 🔎",
    "PLAYLIST_TRACKS": "📜 Playlist Tracks 🎵",
    "USER_TRACKS": "👤 User Tracks 🎵",
    "USER_FAVORITE_TRACKS": "👤 User Favorite Tracks 💖",
    "USER_REPOSTED_TRACKS": "👤 User Reposted Tracks 🔁",
    "MAIN_NAVIGATION": "🗺️  Navigation 🔭",
    "USER_NAVIGATION": "👤 User Navigation 🌎",
    "APP_TITLE": "🎵 Audius Terminal Music Player 🎵",
}
DEFAULT_DISPLAY = CONSTANTS["TRENDING_TRACKS"]
DISPLAY_MENU_PAGES = {
    CONSTANTS["TRENDING_TRACKS"]: {
        "api_endpoint": "tracks/trending",
        "renderer": Track,
        "action": "get",
    },
    CONSTANTS["SEARCH_TRACKS"]: {
        "api_endpoint": "tracks/search",
        "renderer": Track,
        "action": "search",
    },
    CONSTANTS["SEARCH_USERS"]: {
        "api_endpoint": "users/search",
        "renderer": User,
        "action": "search",
    },
    CONSTANTS["SEARCH_PLAYLISTS"]: {
        "api_endpoint": "playlists/search",
        "renderer": Playlist,
        "action": "search",
    },
    CONSTANTS["PLAYLIST_TRACKS"]: {
        "api_endpoint": "playlists/{id}/tracks",
        "renderer": Track,
        "action": "get",
        "has_tracks": True,
        "hide_from_nav": True,
    },
    CONSTANTS["USER_TRACKS"]: {
        "api_endpoint": "users/{id}/tracks",
        "renderer": Track,
        "action": "get",
        "has_tracks": True,
        "hide_from_nav": True,
        "is_user_nav": True,
    },
    CONSTANTS["USER_FAVORITE_TRACKS"]: {
        "api_endpoint": "users/{id}/favorites",
        "renderer": Track,
        "action": "get",
        "has_tracks": True,
        "hide_from_nav": True,
        "is_user_nav": True,
    },
    CONSTANTS["USER_REPOSTED_TRACKS"]: {
        "api_endpoint": "users/{id}/reposts",
        "renderer": Track,
        "action": "get",
        "has_tracks": True,
        "hide_from_nav": True,
        "is_user_nav": True,
    },
}

NAV_MENU_CONFIG = {
    "options": [
        key
        for key in DISPLAY_MENU_PAGES.keys()
        if not DISPLAY_MENU_PAGES[key].get("hide_from_nav", False)
    ],
    "title": CONSTANTS["MAIN_NAVIGATION"],
}

USER_MENU_CONFIG = {
    "options": [
        key
        for key in DISPLAY_MENU_PAGES.keys()
        if DISPLAY_MENU_PAGES[key].get("is_user_nav", False)
    ],
    "title": CONSTANTS["USER_NAVIGATION"],
}


class Player:
    def __init__(self):
        root = py_cui.PyCUI(6, 6)
        current_year = date.today().year
        app_title = f"{CONSTANTS['APP_TITLE']} ©️ {current_year}"
        root.set_title(app_title)
        self.root = root
        self.current_display_key = DEFAULT_DISPLAY
        self.display_item_selection_handler = None
        self.display_items = []
        self.display_menu = None
        self.track_containing_entity_id = ""
        self.nav_menu = None
        self.now_playing = None
        self.current_track = {}
        self.root.run_on_exit(playback.stop)
        self.render()

    def set_help_text(self):
        help_text = "Press - q - to exit player. Use ⬆️ ⬇️ ⬅️ ➡️ to move between menus. Enter to select a menu."
        self.root.title_bar.set_text(help_text)

    def render(self):
        self.render_nav_menu(NAV_MENU_CONFIG)
        self.select_display(self.current_display_key)
        self.render_now_playing()
        self.root.start()

    def render_now_playing(self):
        n = NowPlaying(self, 0, 0, 4, 2, 0, 0, self.stop_track)
        self.now_playing = n

    def render_nav_menu(self, menu_config):
        self.clear_widget(self.nav_menu)
        options = menu_config["options"]
        title = menu_config["title"]
        t = Table(
            self,
            title,
            0,
            4,
            2,
            2,
            options,
            self.select_display,
            False,
            py_cui.MAGENTA_ON_BLACK,
            py_cui.WHITE_ON_MAGENTA,
        )
        self.nav_menu = t

    def select_display(self, selection):
        DISPLAY_ACTION_TO_HANDLER_MAP = {
            "get": self.get_api,
            "search": self.show_search_popup,
        }
        selection_details = DISPLAY_MENU_PAGES[selection]
        self.current_display_key = selection
        display_action = selection_details["action"]
        action_handler = DISPLAY_ACTION_TO_HANDLER_MAP[display_action]
        action_handler()

    def get_api(self):
        DISPLAY_RENDERER_TO_SELECTION_HANDLER_MAP = {
            Track: self.play_track,
            Playlist: self.set_playlist,
            User: self.set_user,
        }
        details = DISPLAY_MENU_PAGES[self.current_display_key]
        endpoint = details["api_endpoint"]
        if details.get("has_tracks", False):
            endpoint = endpoint.replace("{id}", self.track_containing_entity_id)
        items = api.get(endpoint)
        items_formatted = [details["renderer"](item) for item in items]
        self.display_items = items_formatted
        self.display_item_selection_handler = DISPLAY_RENDERER_TO_SELECTION_HANDLER_MAP[
            details["renderer"]
        ]
        self.render_display()

    def clear_widget(self, menu):
        if menu is not None:
            if hasattr(menu, "widget"):
                self.root.forget_widget(menu.widget)

    def add_key_bindings(self):
        if hasattr(self, "root"):
            self.root.add_key_command(py_cui.keys.KEY_SPACE, self.stop_track)

    def render_display(self):
        old_menu = self.display_menu
        is_track_display = "Tracks" in self.current_display_key

        t = Table(
            self,
            self.current_display_key,
            2,
            0,
            6,
            4,
            self.display_items,
            self.display_item_selection_handler,
            is_track_display,
            py_cui.WHITE_ON_BLACK,
            py_cui.WHITE_ON_MAGENTA,
        )
        self.display_menu = t
        if is_track_display:
            self.display_menu.widget.add_key_command(
                py_cui.keys.KEY_SPACE, self.stop_track
            )
        self.clear_widget(old_menu)

    def show_search_popup(self):
        search_title = self.current_display_key
        self.root.show_text_box_popup(search_title, self.submit_search)

    def submit_search(self, query):
        SEARCH_TITLE_TO_HANDLER_MAP = {
            CONSTANTS["SEARCH_PLAYLISTS"]: self.set_playlist,
            CONSTANTS["SEARCH_USERS"]: self.set_user,
            CONSTANTS["SEARCH_TRACKS"]: self.play_track,
        }
        details = DISPLAY_MENU_PAGES[self.current_display_key]
        search_params = {"query": query}
        results = api.get(details["api_endpoint"], search_params)
        formatted_results = [details["renderer"](item) for item in results]
        self.display_items = formatted_results
        self.display_item_selection_handler = SEARCH_TITLE_TO_HANDLER_MAP[
            self.current_display_key
        ]
        self.render_display()

    def set_playlist(self, playlist):
        self.track_containing_entity_id = playlist.id
        self.select_display(CONSTANTS["PLAYLIST_TRACKS"])

    def set_user(self, user):
        self.track_containing_entity_id = user.id
        self.render_nav_menu(USER_MENU_CONFIG)
        self.select_display(CONSTANTS["USER_TRACKS"])

    def play_track(self, track, buffer_callback, finish_loading_callback):
        self.current_track = track
        playback.stream(self.current_track.id, buffer_callback, finish_loading_callback)
        self.render_now_playing()

    def stop_track(self):
        playback.stop()
        self.current_track = {}
        self.render_now_playing()
