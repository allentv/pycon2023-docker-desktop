"""
This module takes care of the UI elements to be rendered and handles the events raised by these elements
"""


import PySimpleGUI as sg

from ui.base import LayoutBase
from ui.info import Info
from ui.sidebar import Sidebar


class AppUIManager(LayoutBase):
    def __init__(self) -> None:
        self.sidebar_obj = Sidebar()
        self.info_obj = Info()

    def get_layout(self) -> list[list]:
        return [
            [
                sg.Column(
                    self.sidebar_obj.get_layout(),
                    background_color=self.sidebar_obj.color,
                    pad=(0, 0),
                    vertical_alignment="top",
                ),
                sg.Column(
                    self.info_obj.get_layout(),
                    background_color=self.info_obj.color,
                    expand_x=True,
                    expand_y=True,
                    pad=(0, 0),
                    element_justification="left",
                ),
            ]
        ]

    def render(self) -> sg.Window:
        return sg.Window("PyDocker", self.get_layout(), size=(800, 800), margins=(0, 0), finalize=True)

    def process(self, event, values) -> None:
        print(event, values)

        match event:
            case "-BTN-CONTAINER-":
                print("Clicked container button!")
                self.info_obj.load("container")
            case "-BTN-IMAGES-":
                print("Clicked images button!")
                self.info_obj.load("image")
            case "-BTN-VOLUMES-":
                print("Clicked volumes button!")
                self.info_obj.load("volume")
