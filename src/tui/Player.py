import py_cui
from datetime import date
from src.libs import api, playback
from src.tui.renderers.Track import Track
from src.tui.components.NowPlaying import NowPlaying
from src.tui.components.Table import Table

DISPLAY_MENU_PAGES = {
    "🌋 Trending Tracks 🚀": {
        "api_endpoint": "tracks/trending",
        "renderer": Track,
        "action": "get",
    },
    "🎼 Search Tracks 🔎": {
        "api_endpoint": "tracks/search",
        "renderer": Track,
        "action": "search",
    },
    "👥 Search Users 🔎": {
        "api_endpoint": "users/search",
        "renderer": Track,
        "action": "search",
    },
    "📜 Search Playlists 🔎": {
        "api_endpoint": "playlists/search",
        "renderer": Track,
        "action": "search",
    },
}

NAV_MENU_CONFIG = {
    "options": DISPLAY_MENU_PAGES.keys(),
    "title": "🗺️  Navigation 🔭",
}


class Player:
    def __init__(self):
        root = py_cui.PyCUI(6, 6)
        current_year = date.today().year
        app_title = f"🎵 Audius Terminal Music Player 🎵 ©️ {current_year}"
        root.set_title(app_title)
        self.root = root
        self.current_display_key = ""
        self.display_item_selection_handler = None
        self.display_items = []
        self.display_menu = None
        self.nav_menu = None
        self.now_playing = None
        self.current_track = {}
        self.root.run_on_exit(playback.stop)
        self.render()

    def render(self):
        self.nav_menu = self.render_nav_menu()
        self.select_display("🌋 Trending Tracks 🚀")
        self.now_playing = self.render_now_playing()
        self.root.start()

    def render_now_playing(self):
        return NowPlaying(self, 0, 0, 4, 2, 0, 0, self.stop_track)

    def render_nav_menu(self):
        options = NAV_MENU_CONFIG["options"]
        title = NAV_MENU_CONFIG["title"]
        t = Table(self, title, 0, 4, 2, 2, options, self.select_display, False)
        return t

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
        DISPLAY_RENDERER_TO_SELECTION_HANDLER_MAP = {Track: self.playtrack}
        details = DISPLAY_MENU_PAGES[self.current_display_key]
        items = api.get(details["api_endpoint"])
        items_formatted = [details["renderer"](item) for item in items]
        self.display_items = items_formatted
        self.display_item_selection_handler = DISPLAY_RENDERER_TO_SELECTION_HANDLER_MAP[
            details["renderer"]
        ]
        self.render_display()

    def clear_display(self):
        if self.display_menu is not None:
            self.root.forget_widget(self.display_menu.table_rows)

    def render_display(self):
        self.clear_display()
        t = Table(
            self,
            self.current_display_key,
            2,
            0,
            6,
            4,
            self.display_items,
            self.display_item_selection_handler,
            True if "Track" in self.current_display_key else False,
        )
        self.display_menu = t

    def show_search_popup(self):
        search_title = self.current_display_key
        self.root.show_text_box_popup(search_title, self.submit_search)

    def submit_search(self, query):
        details = DISPLAY_MENU_PAGES[self.current_display_key]
        search_params = {"query": query}
        results = api.get(details["api_endpoint"], search_params)
        formatted_results = [details["renderer"](item) for item in results]
        self.display_items = formatted_results
        self.display_item_selection_handler = self.playtrack
        self.render_display()

    def playtrack(self, selection, buffer_callback, finish_loading_callback):
        self.current_track = selection
        playback.stream(self.current_track.id, buffer_callback, finish_loading_callback)
        self.render_now_playing()

    def stop_track(self):
        playback.stop()
        self.current_track = {}
        self.render_now_playing()
