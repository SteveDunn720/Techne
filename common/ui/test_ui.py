from ui.base_ui import BaseToolUI  # your base class


class SmileyToolWindow(BaseToolUI):

    WINDOW_TITLE = "Smiley Tool"
    WIDTH = 300

    def __init__(self):
        super().__init__()

        self.tool = SmileyToolWidget()
        self.add_tool(self.tool)