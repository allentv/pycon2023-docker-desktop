import PySimpleGUI as sg

from datasources.docker_client import DockerManager
from ui.base import LayoutBase


class Info(LayoutBase):
    def __init__(self) -> None:
        self.color = "white"
        self.docker_manager = DockerManager()
        self.table = sg.Table(values=[], headings=[])

    def get_layout(self) -> list[list]:
        # TODO: Populate table data when available
        return [[self.table]]

    def update_table_content(self, headings: list[str], content: list[list]):
        # TODO: Update the table component with the new data
        self.table.ColumnHeadings = headings
        self.table.update(content)

    def load(self, target: str) -> None:
        match target:
            case "container":
                table_data = self.docker_manager.get_containers()
                headings = []
            case "image":
                table_data = self.docker_manager.get_images()
                headings = []
            case "volume":
                table_data = self.docker_manager.get_volumes()
                headings = []

        self.update_table_content(headings, table_data)
