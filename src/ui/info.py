import PySimpleGUI as sg

from datasources.docker_client import DockerManager
from ui.base import LayoutBase
from ui.models import process_image_info


class Info(LayoutBase):
    def __init__(self) -> None:
        self.color = "white"
        self.docker_manager = DockerManager()

        # Table headings cannot be changed dynamically. So create beforehand and hide them
        self.table_container = sg.Table(
            values=[],
            headings=["1", "2", "3"],
            expand_x=True,
            visible=False,
        )
        self.table_images = sg.Table(
            values={},
            headings=["Image", "Commit", "Tag", "Size", "Created"],
            expand_x=True,
            visible=False,
        )
        self.table_volumes = sg.Table(
            values={},
            headings=["Name", "Created", "Size"],
            expand_x=True,
            visible=False,
        )

    def get_layout(self) -> list[list]:
        # Keeping all tables in the same line so that they will always appear in the first row
        # when the visibility is toggled
        return [
            [self.table_container, self.table_images, self.table_volumes],
        ]

    def load(self, target: str) -> None:
        match target:
            case "container":
                table_data = self.docker_manager.get_containers()
            case "image":
                table_data = process_image_info(self.docker_manager.get_images())
            case "volume":
                table_data = self.docker_manager.get_volumes()

        self.table_container.update(values=table_data, visible=(target == "container"))
        self.table_images.update(values=table_data, visible=(target == "image"))
        self.table_volumes.update(values=table_data, visible=(target == "volume"))
