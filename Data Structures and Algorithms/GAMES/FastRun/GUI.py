from PySimpleGUI.PySimpleGUI import Button
from configurer import create_config
from tkinter.constants import CENTER
import PySimpleGUI as sg

choose = [
    [
        sg.Button("Add"),
        sg.In(size=(25, 1), key="app")
    ],
    [
        sg.Text("or")
    ],
    [
        sg.FileBrowse("Choose application", enable_events=True, key="chooseApp"),
    ]
]

layout = [
    [
        sg.Text("FastRun", justification=CENTER, size=(50,2)),
    ],
    [
        sg.Text("Name"),
        sg.In(size=(25, 1), default_text="main",enable_events=True, key="name"),
    ],
    [
        sg.Text("Number of screen"),
        sg.In(size=(5, 1),enable_events=True, key="nScreen"),
    ],
    choose,
    [
        sg.Listbox(values=[], enable_events=True, size=(50, 10), key="appList")
    ],
    [
        sg.Button("Submit")
    ]
]

window = sg.Window("FastRun", layout)

Name = "main"
nScreen = 1
AppList = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Submit" :
        create_config(AppList, nScreen, Name)
        break
    
    elif event == "name":
        Name = values["name"]

    elif event == "nScreen":
        try:
            nScreen = int(values["nScreen"])
        except:
            pass

    elif event == "chooseApp":
        app = values["chooseApp"]
        if(app.strip() != ""):
            AppList.append(app)
        window["appList"].update(AppList)
    
    elif event == "Add":
        app = values["app"]
        if(app.strip() != ""):
            AppList.append(app)
        window["appList"].update(AppList)
        window["app"].update("")

window.close()