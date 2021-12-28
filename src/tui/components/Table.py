import time
import threading

import py_cui


class Table:
    def __init__(self, root: py_cui.PyCUI, title: str, elements: list, select_callback):
        self.master = root
        self.table_rows = self.master.add_scroll_menu(
            title, 0, 0, row_span=8, column_span=8
        )
        self.table_rows.add_key_command(py_cui.keys.KEY_ENTER, self.handle_select)
        self.select_callback = select_callback
        self.table_rows.add_item_list(elements)

    def handle_load(self):
        # self.master.show_loading_bar_popup("Incrementing a counter...", 100)
        self.master.show_loading_icon_popup("Buffering", "Loading... be patient ⌛")
        operation_thread = threading.Thread(target=self.long_operation)
        operation_thread.start()

    def finish_load(self):
        print("finish_load called")
        self.master.stop_loading_popup()

    def long_operation(self):
        """A simple function that demonstrates a long callback operation performed while loading popup is open"""

        counter = 0
        for i in range(0, 100):
            time.sleep(0.1)
            counter = counter + 1
            self.master.status_bar.set_text(str(counter))
            # self.master.increment_loading_bar()
            # When using a bar indicator, we will increment the completed counter. Will be ignored for loading icon popup
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

        self.select_callback(selection, self.handle_load, self.finish_load)


def render(title, rows, columns, elements, select_callback):
    root = py_cui.PyCUI(rows, columns)
    root.set_title(title)
    t = Table(root, title, elements, select_callback)
    root.start()
