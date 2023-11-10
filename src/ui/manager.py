"""
This module takes care of the UI elements to be rendered and handles the events raised by these elements
"""


import PySimpleGUI as sg

from datasources.docker_client import DockerManager

from ui.base import LayoutBase
from ui.info import Info
from ui.models import process_image_info
from ui.sidebar import Sidebar


class AppUIManager(LayoutBase):
    def __init__(self) -> None:
        self.sidebar_obj = Sidebar()
        self.docker_manager = DockerManager()
        self.info_obj = Info(self.docker_manager)

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
        return sg.Window(
            "PyDocker",
            self.get_layout(),
            size=(800, 400),
            margins=(0, 0),
            finalize=True,
            grab_anywhere_using_control=True,
            debugger_enabled=True,
            font=("Arial", 16, ""),
        )

    def run_container(self, image_idx) -> None:
        print(f"Image idx is: '{image_idx}'")
        images = process_image_info(self.docker_manager.get_images())
        image_name = images[image_idx][0]

        print(f"Image name is: '{image_name}'")
        self.docker_manager.run_container(image_name)

    def download_image(self, image_name) -> None:
        self.docker_manager.pull_images(image_name)

        # Reload the list of images
        self.info_obj.load("image")

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
            case "-IMAGES-SECTION-START-CONTAINER-":
                print("Clicked start container button!")
                self.run_container(values["-IMAGES_TABLE-"][0])
            case "-IMAGES-SECTION-DOWNLOAD-IMAGE-":
                print("Clicked download image button!")
                self.download_image(values["-IMAGES-SECTION-IMAGE-NAME-"])
