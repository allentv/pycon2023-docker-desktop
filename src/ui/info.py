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
            num_rows=5,
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
            num_rows=5,
        )
        self.images_actions = sg.Frame(
            "Actions",
            [
                [
                    sg.Button(
                        "Start Container",
                        button_color=sg.GREENS[0],
                        enable_events=True,
                        key="-IMAGES-SECTION-START-CONTAINER-",
                    )
                ],
                [
                    sg.Text("Enter docker image name"),
                    sg.Input(
                        default_text="",
                        focus=True,
                        key="-IMAGES-SECTION-IMAGE-NAME-",
                    ),
                    sg.Button(
                        "Download",
                        button_color=sg.BLUES[1],
                        enable_events=True,
                        key="-IMAGES-SECTION-DOWNLOAD-IMAGE-",
                    ),
                ],
            ],
            expand_x=True,
            expand_y=True,
            p=10,
            visible=False,
            background_color="gray",
        )
        self.table_volumes = sg.Table(
            values={},
            headings=["Name", "Created"],
            expand_x=True,
            visible=False,
            row_height=24,
            justification="center",
            key="-VOLUMES_TABLE-",
            num_rows=8,
        )

    def get_layout(self) -> list[list]:
        # Keeping all tables in the same line so that they will always appear in the first row
        # when the visibility is toggled
        return [
            [self.table_container, self.table_images, self.table_volumes],
            [self.images_actions],
        ]

    def load(self, target: str) -> None:
        is_container = False
        is_image = False
        is_volume = False

        match target:
            case "container":
                table_data = process_container_info(self.docker_manager.get_containers())
                is_container = True
            case "image":
                table_data = process_image_info(self.docker_manager.get_images())
                is_image = True
            case "volume":
                table_data = process_volume_info(self.docker_manager.get_volumes())
                is_volume = True

        # Toggle visibilty of the tables based on the user choice
        self.table_container.update(values=table_data if is_container else None, visible=is_container)
        self.table_images.update(values=table_data if is_image else None, visible=is_image)
        self.images_actions.update(visible=is_image)
        self.table_volumes.update(values=table_data if is_volume else None, visible=is_volume)
