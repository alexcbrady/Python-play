import PySimpleGUI as sg
import csv
import pandas as pd

df = pd.read_csv("C:\\Users\\alexc\\Downloads\\airtravel.csv")


#sg.Window(title="Hello World", layout = [[]], margins = (100, 50)).read()
sg.theme("darkGrey1")
layout = [  [sg.Text("Airplane data", font = ("Arial", 20, "bold"), expand_x = True, justification = "left center", pad = (70, 0))],
            [sg.Text(df, justification = "center", font = ("Arial", 15), expand_x = False)],
            [sg.Text("(in amounts of passengers)", justification = "center", expand_x = False, text_color = "yellow", pad = (80, 0))],
            [sg.Text(" ")],
            [sg.Text("This is my second row of my first GUI", font = ("Arial", 14)), sg.InputText()],
            [sg.Button("Ok", size = 20, border_width=4, tooltip = "click me", button_color = "black on lightBlue", mouseover_colors = "purple"), sg.Button("Click me to close window", size = 20, border_width=4, button_color = "black on lightBlue", mouseover_colors = "red")]   
        ]
window = sg.Window("GUI fun test", layout, size = (1000, 600))

while True:
    event, values = window.read()

    if event == "Click me to close window" or event == sg.WIN_CLOSED:
        break
    print("You entered ", values[0])
    
    if values[0] == "":
        print("You forgot to type the message!")

window.close()

