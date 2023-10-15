import PySimpleGUI as sg

from ui.manager import AppUIManager

ui_manager = AppUIManager()

window = ui_manager.render()

while True:
    event, values = window.read()
    ui_manager.process(event, values)

    if event == sg.WIN_CLOSED:  # always,  always give a way out!
        break
