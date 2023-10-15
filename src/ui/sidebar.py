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
            [
                sg.Image(
                    filename="./src/ui/icons/container.png",
                    subsample=12,
                    background_color="gray",
                    enable_events=True,
                ),
                sg.Text(
                    "Next to image",
                    background_color="gray",
                    enable_events=True,
                ),
            ],
        ]
