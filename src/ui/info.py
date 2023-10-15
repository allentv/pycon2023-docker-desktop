import PySimpleGUI as sg

from datasources.docker_client import DockerManager


class Info:
    def __init__(self) -> None:
        self.color = "white"
        self.docker_manager = DockerManager()
        self.table_data = []

    def get_layout(self):
        # TODO: Populate table data when available
        return [
            [
                sg.Text("More Info"),
            ]
        ]

    def load(self, target: str):
        match target:
            case "container":
                self.table_data = self.docker_manager.get_containers()
            case "image":
                self.table_data = self.docker_manager.get_images()
            case "volume":
                self.table_data = self.docker_manager.get_volumes()
