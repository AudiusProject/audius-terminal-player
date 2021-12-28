import py_cui
from datetime import date
from src.libs import api, playback
from src.tui.components.NowPlaying import NowPlaying
from src.tui.components.Table import Table


def render(title, rows, columns, elements, select_callback, exit_callback):

    root = py_cui.PyCUI(rows, columns)
    root.set_title(app_title)
    t = Table(root, title, elements, select_callback)
    root.add_key_command(py_cui.keys.KEY_CTRL_C, exit_callback)
    root.start()
    #
    trending_tracks = api.get("tracks/trending")
    trending_tracks_formatted = [Track(track) for track in trending_tracks]
    render(
        "🌋 Trending Tracks 🚀", 8, 8, trending_tracks_formatted, playtrack, playback.stop
    )


DISPLAY_TO_SHIT = {
    "Trending": {
        api_endpoint: "tracks/trending",
        renderer: Track,
        title: "🌋 Trending Tracks 🚀",
        select_callback: playtrack,
    },
    "Search Tracks": {
        api_endpoint: "tracks/search",
        renderer: Track,
        title: "🔎 Search Tracks",
        select_callback: 
    },
    "Menu": {
        # connect API methods to stuff hydrating views
    },
}


class Player:
    def __init__(self):
        root = py_cui.PyCUI(8, 8)
        current_year = date.today().year
        app_title = f"🎵 Audius Terminal Music Player 🎵 ©️ {current_year}"
        root.set_title(app_title)
        self.root = root
        self.current_display = "Trending"

    def render(self):
        now_playing = NowPlaying(self.root)

        self.root.start()

    def playtrack(selection, buffer_callback, finish_loading_callback):
        playback.stream(selection.id, buffer_callback, finish_loading_callback)
        self.current_track = selection


class NowPlaying:
    def __init__(self, root: py_cui.PyCUI):
        self.master = root
        print(root)
        self.label = self.master.add_button(
            "Now playing: {root.selected_track}",
            6,
            0,
            row_span=1,
            column_span=8,
            padx=0,
            pady=0,
            command=self.control_playback,
        )

    # def handle_select(self):
    #     """handle selection"""

    #     selection = self.table_rows.get()
    #     if selection is None:
    #         self.master.show_error_popup(
    #             "No Item", "There is no item in the list to select"
    #         )
    #         return
    #     self.select_callback(selection)

    def control_playback(self):
        """control playback"""
        playback.stop()
