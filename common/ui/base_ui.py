from __future__ import annotations

# PySide fallback (your pattern 👍)
try:
    from PySide6 import QtWidgets, QtCore
    from shiboken6 import wrapInstance
except:
    from PySide2 import QtWidgets, QtCore
    from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui


# -----------------------------
# Maya Main Window
# -----------------------------
def maya_main_window():
    ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(ptr), QtWidgets.QWidget)


# -----------------------------
# Base UI Class
# -----------------------------
class BaseToolUI(QtWidgets.QDialog):

    WINDOW_TITLE = "Base Tool"
    WIDTH = 400

    def __init__(self, parent=maya_main_window()):
        super().__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setMinimumWidth(self.WIDTH)

        # Remove help button (you already do this 👍)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.build_base_ui()
        self.apply_style()

    # -----------------------------
    # Base Layout
    # -----------------------------
    def build_base_ui(self):

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        # Where tools get inserted
        self.content_widget = QtWidgets.QWidget()
        self.content_layout = QtWidgets.QVBoxLayout(self.content_widget)

        self.main_layout.addWidget(self.content_widget)

    # -----------------------------
    # Styling (global reuse)
    # -----------------------------
    def apply_style(self):

        self.setStyleSheet("""
            QPushButton {
                background-color: rgb(80,80,80);
                color: white;
                border-radius: 4px;
                padding: 6px;
            }

            QPushButton:hover {
                background-color: rgb(95,95,95);
            }

            QComboBox {
                padding: 4px;
            }

            QGroupBox {
                font-weight: bold;
                border: 1px solid rgb(90,90,90);
                border-radius: 4px;
                margin-top: 6px;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 8px;
                padding: 0 3px 0 3px;
            }
        """)

    # -----------------------------
    # Add Tool Widget
    # -----------------------------
    def add_tool(self, widget):
        self.content_layout.addWidget(widget)

try:
    from PySide6 import QtWidgets, QtCore
except:
    from PySide2 import QtWidgets, QtCore


class CollapsibleSection(QtWidgets.QWidget):

    def __init__(self, title="", parent=None):
        super().__init__(parent)

        self.toggle_button = QtWidgets.QToolButton(text=title, checkable=True, checked=True)
        self.toggle_button.setStyleSheet("font-weight: bold")
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.DownArrow)

        self.toggle_button.clicked.connect(self.toggle)

        self.content_area = QtWidgets.QWidget()
        self.content_layout = QtWidgets.QVBoxLayout(self.content_area)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.content_area)

    def toggle(self):
        visible = self.toggle_button.isChecked()
        self.content_area.setVisible(visible)

        self.toggle_button.setArrowType(
            QtCore.Qt.DownArrow if visible else QtCore.Qt.RightArrow
        )