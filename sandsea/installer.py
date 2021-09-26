from tkinter import *

class colors:
    def __init__(t):
        t.bg = "#000066"
        t.fg = "#ffffff"
        t.lime = "#006600"
        t.red = "#ff0000"

color = colors()

def font(size):
    return ("Arial", int(size))

master = Tk()
master.config(bg=color.bg)

installerLabel = Label(master, text="SANDSEA Simulation Engine Installer", bg=color.bg, fg=color.fg, font=font(36), anchor="w")
installerLabel.grid(row=1, column=1)

installerDescription = Label(master, text="This is the official installer for the SANDSEA simulation engine. Once you complete these steps, you can use SANDSEA.", bg=color.bg, fg=color.fg, font=font(14)
, anchor="w")
installerDescription.grid(row=2, column=1)

stepDescription = Label(master, text="STEP 1/3: Please select a directory ", bg=color.bg, fg=color.fg, font=font(14)
, anchor="w")
stepDescription.grid(row=3, column=1)

master.mainloop()
