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

    def handle_select(self):
        """handle selection"""

        selection = self.table_rows.get()
        if selection is None:
            self.master.show_error_popup(
                "No Item", "There is no item in the list to select"
            )
            return
        self.select_callback(selection)


def render(title, rows, columns, elements, select_callback):
    root = py_cui.PyCUI(rows, columns)
    root.set_title(title)
    t = Table(root, title, elements, select_callback)
    root.start()
