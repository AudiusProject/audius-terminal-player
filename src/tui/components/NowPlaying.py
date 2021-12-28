import py_cui
from src.libs import playback


class Root(py_cui.PyCUI):
    def __init__(self, metadata=None, *args, **kwargs):
        py_cui.PyCUI.__init__(self, *args, **kwargs)
        self.metadata = metadata


class NowPlaying:
    def __init__(self, root: py_cui.PyCUI):
        self.master = root
        print(root)
        self.label = self.master.add_button(
            f"Now playing: {root.metadata}",
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
root = Root(5, 8, 8)
root.set_title("Audius Terminal Player")
t = NowPlaying(root)
root.start()
