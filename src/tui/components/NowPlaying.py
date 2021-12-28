import py_cui


class NowPlaying:
    def __init__(self, root: py_cui.PyCUI):
        self.master = root
        self.label = self.master.add_block_label(
            "Now playing", 6, 6, row_span=2, column_span=2, padx=1, pady=0
        )
        self.button = self.master.add_button(
            "play/pause playback",
            7,
            7,
            row_span=1,
            column_span=1,
            padx=1,
            pady=0,
            command=self.control_playback,
        )

        # self.label.add_key_command(py_cui.keys.KEY_ENTER, self.handle_select)

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
        print("PAUSING")


# def render(title, rows, columns, elements, select_callback):
root = py_cui.PyCUI(8, 8)
root.set_title("Audius Terminal Player")
t = NowPlaying(root)
root.start()
