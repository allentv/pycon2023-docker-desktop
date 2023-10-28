import PySimpleGUI as sg

from datasources.docker_client import DockerManager
from ui.base import LayoutBase
from ui.models import process_container_info, process_image_info, process_volume_info


class Info(LayoutBase):
    def __init__(self) -> None:
        self.color = "white"
        self.docker_manager = DockerManager()

        # Table headings cannot be changed dynamically. So create beforehand and hide them
        self.table_container = sg.Table(
            values=[],
            headings=["Name", "Image", "Status"],
            expand_x=True,
            visible=False,
            row_height=24,
            justification="left",
            key="-CONTAINER_TABLE-",
        )
        self.table_images = sg.Table(
            values={},
            headings=["Image", "Commit", "Tag", "Size", "Created"],
            expand_x=True,
            visible=False,
            row_height=24,
            justification="left",
            enable_events=True,
            key="-IMAGES_TABLE-",
        )
        self.table_volumes = sg.Table(
            values={},
            headings=["Name", "Created"],
            expand_x=True,
            visible=False,
            row_height=24,
            justification="center",
            key="-VOLUMES_TABLE-",
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
                table_data = process_container_info(self.docker_manager.get_containers())
            case "image":
                table_data = process_image_info(self.docker_manager.get_images())
            case "volume":
                table_data = process_volume_info(self.docker_manager.get_volumes())

        # Toggle visibilty of the tables based on the user choice
        self.table_container.update(values=table_data, visible=(target == "container"))
        self.table_images.update(values=table_data, visible=(target == "image"))
        self.table_volumes.update(values=table_data, visible=(target == "volume"))
