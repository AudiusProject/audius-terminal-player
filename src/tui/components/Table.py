import time
import threading

import py_cui

NO_RESULTS = "Nothing to display! Try searching for your heart's desire 😻"


class Table:
    def __init__(
        self,
        player,
        title: str,
        x_offset,
        y_offset,
        width,
        height,
        elements: list,
        select_callback,
        show_loading_progress: bool,
    ):
        self.master = player.root
        self.table_rows = self.master.add_scroll_menu(
            title, x_offset, y_offset, row_span=height, column_span=width
        )
        self.table_rows.add_key_command(py_cui.keys.KEY_ENTER, self.handle_select)
        self.select_callback = select_callback
        self.add_items(elements)
        self.table_rows.add_text_color_rule(
            "",
            py_cui.WHITE_ON_BLACK,
            "contains",
            selected_color=py_cui.BLACK_ON_WHITE,
            match_type="line",
        )
        self.show_loading_progress = show_loading_progress

    def add_items(self, elements):
        if len(elements) > 0:
            self.table_rows.add_item_list(elements)
        else:
            self.table_rows.add_item_list([NO_RESULTS])

    def handle_load(self):
        self.master.show_loading_bar_popup("Loading... be patient ⌛", 10)
        operation_thread = threading.Thread(target=self.long_operation)
        operation_thread.start()

    def finish_load(self):
        self.master.stop_loading_popup()

    def long_operation(self):
        counter = 0
        for i in range(0, 10):
            time.sleep(0.1)
            counter = counter + 1
            self.master.status_bar.set_text(str(counter))
            self.master.increment_loading_bar()
        # This is what stops the loading popup and reenters overview mode
        self.master.stop_loading_popup()

    def handle_select(self):
        """handle selection"""

        selection = self.table_rows.get()
        if selection is None:
            self.master.show_error_popup(
                "No Item", "There is no item in the list to select"
            )
            return
        elif selection != NO_RESULTS:
            if self.show_loading_progress:
                self.select_callback(selection, self.handle_load, self.finish_load)
            else:
                self.select_callback(selection)
