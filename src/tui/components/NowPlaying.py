import py_cui
from src.utils import playback


class NowPlaying:
    def __init__(self, root: py_cui.PyCUI):
        self.master = root
        self.label = self.master.add_button(
            "Now playing",
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


# def render(title, rows, columns, elements, select_callback):
root = py_cui.PyCUI(8, 8)
root.set_title("Audius Terminal Player")
t = NowPlaying(root)
root.start()
