import PySimpleGUI as sg


class Sidebar:
    def __init__(self) -> None:
        self.color = "gray"

    def get_layout(self) -> list[list]:
        # Use a column to adding padding and background color
        return [
            [
                sg.Column(
                    [
                        [
                            sg.Image(
                                filename="./src/ui/icons/container.png",
                                background_color=self.color,
                                subsample=12,
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
                            sg.Image(
                                filename="./src/ui/icons/3d-cube.png",
                                subsample=10,
                                enable_events=True,
                            ),
                            sg.Text(
                                "Images",
                                enable_events=True,
                                background_color=self.color,
                                key="-BTN-IMAGES-",
                            ),
                        ],
                        [
                            sg.Text(
                                "Volumes",
                                enable_events=True,
                                background_color=self.color,
                                key="-BTN-VOLUMES-",
                            )
                        ],
                    ],
                    p=20,
                    background_color=self.color,
                    size=(150, 800),
                )
            ]
        ]
