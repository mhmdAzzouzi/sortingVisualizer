import tkinter as tk

from tkinter import ttk
from tkinter.constants import CENTER, NW, SW, W

import os
import tkinter.font as tkFont
import sys
from tkinter import *
import pyperclip


class Screen(tk.Tk):
    main_color = "#3c026b"
    def __init__(self, controller):
        super().__init__()
        super().title("License Key Generator")
        super().geometry("600x300")
        super().config(bg=self.main_color)
        self.controller = controller
        self._main_frame_1()
        

    def quit(self):
        super().destroy()

    def main(self):
        self.mainloop()
    
    def _main_frame_1(self):
        self.frm = tk.Frame(self, width=20, bg=self.main_color)
        self.frm.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.buttons = tk.Frame(self, width=15, bg=self.main_color)
        self.buttons.place(relx=0.5, rely=0.75, anchor=CENTER)
        self.errors = tk.StringVar()
        self.success = tk.StringVar()
        self.licenseKey = tk.StringVar()
        self.serial = tk.StringVar()
        # tkimage = ImageTk. PhotoImage(file="main\key.png")
        # self._image_label(tkimage , 1, 0, self.frm )

        self._message_label("", 0, 1, self.frm, self.success, "green")
        self._message_label("", 0, 1, self.frm, self.errors, "red")

        self._create_label("Serial Number", 2, 0, self.frm)
        self._create_label("Key Generated", 3, 0, self.frm)
        self._create_entry_active(2, 1)
        self._create_entry(3, 1)
        self._generate_button("Generate", 0, 0)
        self._save_button("Save And Exit ", 0, 1)
        self._copy_button("Copy Key", 1, 0, 2)

    def _create_entry(self, row, column):
        entry = tk.Entry(self.frm, textvariable=self.licenseKey,
                         width=40, state="disabled")
        entry.grid(row=row, column=column, columnspan=1, padx=5, pady=10)

    def _create_entry_active(self, row, column):
        entry = tk.Entry(self.frm, textvariable=self.serial, width=40)
        entry.grid(row=row, column=column, columnspan=1, padx=5, pady=10)

    def _message_label(self, text, row, column, frame, variable, color):
        fontStyle = tkFont.Font(family="Times", size=10)
        label = tk.Label(frame,  textvariable=variable,
                         font=fontStyle, fg=color,background=self.main_color)
        label.grid(row=row, column=column, columnspan=2, pady=5)
        return label

    def _create_label(self, text, row, column, frame):
        fontStyle = tkFont.Font(family="Times", size=12)
        label = tk.Label(frame, text=text, font=fontStyle,background=self.main_color,foreground="white")
        label.grid(row=row, column=column, columnspan=1, pady=5)

    def _generate_button(self, text, row, column):
        fontStyle = tkFont.Font(family="Times", size=9)
        button = tk.Button(self.buttons, fg='green', text=text, width=15,
                           command=lambda: self.controller.generate(self.licenseKey, self.serial,self.errors), font=fontStyle,background="green",foreground="white")
        button.grid(row=row, column=column, padx=30, pady=5)
        return button

    def _save_button(self, text, row, column):
        fontStyle = tkFont.Font(family="Times", size=9)
        button = tk.Button(self.buttons, fg='black', text=text,
                           width=15, command=lambda: self.controller.save_key(self.licenseKey.get()), font=fontStyle)
        button.grid(row=row, column=column, padx=30, pady=5)

    def _copy_button(self, text, row, column, span):
        fontStyle = tkFont.Font(family="Times", size=9)
        button = tk.Button(self.buttons, width=15, text=text, command=lambda: self.controller.copy_to_clipbaord(
            self.licenseKey.get(), self.errors, self.success), font=fontStyle)
        button.grid(row=row, column=column, columnspan=span, padx=30, pady=10)

    def _image_label(self, image , row , column , frame):
           label = tk.Label(frame, image=image)
           label.grid(row=row, column=column, columnspan=2)
