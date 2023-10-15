import PySimpleGUI as sg


class Sidebar:
    def __init__(self) -> None:
        self.color = self.color

    def get_layout(self):
        return [
            [
                sg.Image(
                    filename="./src/ui/icons/container.png",
                    subsample=12,
                    background_color=self.color,
                    enable_events=True,
                ),
                sg.Text(
                    "Containers",
                    background_color=self.color,
                    enable_events=True,
                    key="-BTN-CONTAINER-",
                ),
            ],
            [
                sg.Text(
                    "Images",
                    enable_events=True,
                    background_color=self.color,
                    key="-BTN-IMAGES-",
                )
            ],
            [
                sg.Text(
                    "Volumes",
                    enable_events=True,
                    background_color=self.color,
                    key="-BTN-VOLUMES-",
                )
            ],
        ]
