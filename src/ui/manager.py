import PySimpleGUI as sg

from ui.info import Info
from ui.sidebar import Sidebar


class AppUIManager:
    def __init__(self) -> None:
        self.sidebar_obj = Sidebar()
        self.info_obj = Info()

    def render(self):
        layout = [
            [
                sg.Column(
                    self.sidebar_obj.get_layout(),
                    background_color=self.sidebar_obj.color,
                    expand_y=True,
                    expand_x=True,
                ),
                sg.Column(
                    self.info_obj.get_layout(),
                    background_color=self.info_obj.color,
                    expand_x=True,
                    expand_y=True,
                ),
            ]
        ]
        return sg.Window("PyDocker", layout, size=(600, 600), resizable=True)

    def process(self, event, values):
        # TODO: Handle button click events to load data
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
