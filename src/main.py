#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          : Viacheslav Zamaraev
#   email           : zamaraev@gmail.com
#   Script Name     : main.py
#   Created         : 02.06.2022
#   Last Modified	: 02.06.2022
#   Version		    : 1.0
#   PIP             :
#   RESULT          :
# Modifications	: 1.1 -
# Description   : load data from Excel file and send to users by list pdf attachements
# @echo off

# C:\Glory\Projects\Python\Kvartplata24mail\data\Севастопольская

import tkinter as tk
from tkinter import filedialog, Text
import os
from datetime import datetime

from core.logger import get_logger

logger = get_logger()

global root

root = tk.Tk()
apps = []

# the new
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("Excel", "*.xlsx"), ("all files", "*.*")))
    apps.append(filename)
    print(apps)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def run_apps():
    for app in apps:
        os.startfile(app)



def make_gui():
    canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    openFile = tk.Button(root, text="Open File", padx=25,
                         pady=10, fg='white', bg="#263D42", command=addApp)
    openFile.pack()

    btn_run_apps = tk.Button(root, text="Run Apps", padx=25,
                        pady=10, fg='white', bg="#263D42", command=run_apps)
    btn_run_apps.pack()

    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()


# class Root(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.label = tk.Label(self, text="Hello World", padx=5, pady=5)
#         self.label.pack()



def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    make_gui()
    # root = Root()
    root.mainloop()

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == "__main__":
    main()