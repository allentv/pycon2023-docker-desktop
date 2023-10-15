import PySimpleGUI as sg


class Info:
    def __init__(self) -> None:
        self.color = "white"

    def get_layout(self):
        return [[sg.Text("More Info")]]
