import PySimpleGUI as sg


class Sidebar:
    def __init__(self) -> None:
        self.color = "gray"

    def get_layout(self):
        return [
            [sg.Button("Containers")],
            [sg.Button("Images")],
            [sg.Button("Volumes")],
            [
                sg.Text(
                    "Testing click...",
                    enable_events=True,
                    background_color="gray",
                )
            ],
        ]
