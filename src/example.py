import PySimpleGUI as sg

sg.ChangeLookAndFeel("LightGrey")

layout = [
    [sg.Text("Persistent window")],
    [sg.Input(key="-IN-")],
    [sg.Button("Read"), sg.Exit()],
    [
        sg.Table(
            [[1, 2, 3], [11, 22, 33], [111, 222, 333]],
            headings=["c1", "c2", "c3"],
            auto_size_columns=True,
            enable_events=True,
            enable_click_events=False,
            key="-TABLE-",
        )
    ],
]

window = sg.Window("Window that stays open", layout)

while True:  # The Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()
