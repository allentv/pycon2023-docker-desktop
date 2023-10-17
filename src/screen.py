import PySimpleGUI as sg

from ui.manager import AppUIManager

# Keep the layout of the application in a separate module
ui_manager = AppUIManager()

# Reference to the generated window and its content
window = ui_manager.render()

while True:
    # Wait on an event to be raised or an input to be filled in
    event, values = window.read()

    # Pass on the event to the UI layout manager to handle anything related
    ui_manager.process(event, values)

    # Handle window events
    if event == sg.WIN_CLOSED:
        break
