from pathlib import Path

import PySimpleGUI as sg

from ui.base import LayoutBase


class Sidebar(LayoutBase):
    def __init__(self) -> None:
        self.color = "gray"

    def get_layout(self) -> list[list]:
        icons_path = Path("./src/ui/icons")

        # Container button row
        btn_container = [
            sg.Image(
                filename=icons_path / "container.png",
                background_color=self.color,
                subsample=12,
                enable_events=True,
            ),
            sg.Text("Containers", background_color=self.color, enable_events=True, key="-BTN-CONTAINER-"),
        ]

        # Images button row
        btn_images = [
            sg.Image(filename=icons_path / "images.png", subsample=10, enable_events=True),
            sg.Text("Images", enable_events=True, background_color=self.color, key="-BTN-IMAGES-"),
        ]

        # Volumes button row
        btn_volumes = [sg.Text("Volumes", enable_events=True, background_color=self.color, key="-BTN-VOLUMES-")]

        # Use a column to adding padding and background color
        return [
            [
                sg.Column(
                    [btn_container, btn_images, btn_volumes],
                    p=20,
                    background_color=self.color,
                    size=(150, 800),
                )
            ]
        ]
