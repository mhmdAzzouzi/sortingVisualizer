import tkinter as tk
from tkinter import READABLE, Variable, ttk
from tkinter import font
from tkinter.constants import CENTER, DISABLED, HORIZONTAL, SW, W
import pyperclip
from drawSortingAlgo import sortingAlgorithm
import os
import sys
import tkinter.font as tkFont


class View(tk.Tk):

    # constructor to initialize the view class
    def __init__(self, controller):
        super().__init__()
        super().title("Sorting Algorithm Visualizer")
        super().maxsize(900, 600)

        # "#262623"

        # Main Color theme and font styles
        self.main_color = "#3c026b"
        self.user_menu_color = "#db16ad"
        # self.security_frame_color = "#B0015B"
        self.fonts = tkFont.Font(family="Times", size=12)
        self.label_fonts = tkFont.Font(family="Times", size=12)
        self.message_fonts = tkFont.Font(family="Times", size=10)
        self.button_fonts = tkFont.Font(family="Times", size=9)
        # self.entry_fonts = tkFont.Font(family="Times", size=9)
        #####################

        self.root = super()
        self.root.config(bg=self.main_color)
        self.sortingAlgo = sortingAlgorithm(self)
        self.controller = controller
        if self.retrieve_key():
            # super().geometry("900x600")
            self.program_frame()

        else:
            self.serial_num = tk.StringVar()
            self.security_frame()

        # self.generate = sortingAlgorithm

    # main function to run the program
    def retrieve_key(self):
        try:
            with open(os.path.join("main", "LicenseKey.txt"), "r") as file:
                first_line = file.readlines(1)
                key_from_file = first_line[0].split(":")[1].strip()
                serial_from_file = first_line[0].split(":")[0].strip()
                print(key_from_file)
                if self.controller.deformat_string(key_from_file) == serial_from_file:
                    return True
                else:
                    return False
        except:
            return False

    def main(self):
        self.mainloop()

    def security_frame(self):
        super().geometry("600x300")
        self.security_frame = tk.Frame(self, bg=self.main_color)
        self.buttons = tk.Frame(self, width=20, bg=self.main_color)
        self.security_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.buttons.place(relx=0.60, rely=0.75, anchor=CENTER)
        license = self._license_entry(1, 1)
        serial = self._serial_entry(2, 1)
        self.errors = tk.StringVar()
        self.success = tk.StringVar()
        self.error_label = self.message_label(
            0, 0, self.security_frame, self.errors, "red")
        self.success_label = self.message_label(
            0, 0, self.security_frame, self.success, "green")
        self._create_label("Serial number:  ", 1, 0, self.security_frame, 1)
        self._create_label("License key:  ", 2, 0,  self.security_frame, 1)
        self.controller.get_serial_number(self.serial_num)
        self._validate_button("Check", 0, 0, license, serial)
        self._copy_button("Copy to clipboard", 0, 2)

    def program_frame(self):
        # super().geometry("900x600")
        self.program_frame = tk.Frame(self, bg=self.main_color)
        self.program_frame.grid(row=0, column=0)
        self.user_menu()
        self.draw_frame()

    def user_menu(self):
        self.frm3 = tk.Frame(self.program_frame, width=600,
                             height=200, bg=self.user_menu_color)
        self.frm3.grid(row=0, column=0, padx=10, pady=5)
        self._create_label_frame3("Algorithm : ", 0, 0, self.frm3)
        speedScale = self._speed_scale("Select Speed", 0, 4)

        self._create_combobox_frame3(
            ['Bubble Sort', 'Merge Sort'], 0, 1, self.frm3)
        self._start_button("Start Visualization", 0, 3, speedScale)
        self._create_label_frame3("Size : ", 1, 0, self.frm3)
        self._create_label_frame3("Min Value : ", 1, 2, self.frm3)
        self._create_label_frame3("Max Value : ", 1, 4, self.frm3)
        minEntry = self._create_entry_frame3(1, 3)
        maxEntry = self._create_entry_frame3(1, 5)
        size = self._create_entry_frame3(1, 1)
        self._generate_button_3("Generate", 0, 2, minEntry, maxEntry, size)

    def draw_frame(self):
        self.drawframe = tk.Frame(
            self.program_frame, width=600, height=380, bg=self.main_color)
        self.drawframe.grid(row=1, column=0, padx=10, pady=5)
        self.intro = self.intro_label(
            "Press 'Generate' button to generate randomized data", 0, 0, self.drawframe)
    # a function to create input box on frame 1

    # a function to create a labe on frame 2
    def _create_label(self, text, row, column, frame, span):
        label = ttk.Label(frame, text=text, width=15,
                          background=self.main_color, foreground="white", font=self.label_fonts)
        label.grid(row=row, column=column,  padx=5, pady=5, columnspan=span)

    def message_label(self, row, column, frame, variable, color):
        label = tk.Label(frame, textvariable=variable,
                         fg=color, background=self.main_color, font=self.message_fonts)
        label.grid(row=row, column=column, columnspan=2, pady=10)
        return label

    def _create_label_frame3(self, text, row, column, frame):
        label = tk.Label(frame, text=text,  background=self.main_color,
                         foreground="white", font=self.label_fonts)
        label.grid(row=row, column=column, padx=5, pady=5, sticky=W)
        return label

    def intro_label(self, text, row, column, frame):
        label = tk.Label(frame, text=text,  background=self.main_color,
                         foreground="white", font=self.fonts)
        label.place(relx=0.5, rely=0.5, anchor=CENTER)
        return label

    def _create_combobox_frame3(self, values, row, column, frame):
        combobox = ttk.Combobox(
            frame, values=values, font=self.label_fonts, state="readonly")
        combobox.current(1)
        # values = combobox.get()
        combobox.grid(row=row, column=column, padx=5, pady=5)
        # combobox.bind("<<ComboboxSelected>>", self.value)
        # return combobox

    def _create_entry_frame3(self, row, column):
        entry = tk.Entry(self.frm3)
        entry.grid(row=row, column=column, padx=5, pady=5, sticky=W)
        return entry

    def _generate_button_3(self, text, row, column, entry1, entry2, entry3):
        button = tk.Button(self.frm3,  background=self.main_color, foreground="white", text=text, font=self.button_fonts,
                           command=lambda: self.sortingAlgo.Generate(entry1, entry2, entry3, self.drawframe, self.intro))
        button.grid(row=row, column=column, padx=5, pady=5)

    def _start_button(self, text, row, column, speedScale):
        button = tk.Button(self.frm3, font=self.button_fonts, background=self.main_color, foreground="white",
                           text=text, command=lambda: self.sortingAlgo.start_algorithm(speedScale, self.drawframe))
        button.grid(row=row, column=column)

    def _speed_scale(self, text, row, column):
        scale = tk.Scale(self.frm3,  background=self.main_color, foreground="white",  from_=0.09,
                         to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label=text, font=self.label_fonts)
        scale.grid(row=row, column=column, columnspan=2, padx=5, pady=5)
        return scale

    def _serial_entry(self, row, column):
        entry = tk.Entry(self.security_frame, width=30)
        entry.grid(row=row, column=column, padx=5, pady=5,ipady=1)
        return entry

    def _license_entry(self, row, column):
        entry = tk.Entry(self.security_frame,
                         textvariable=self.serial_num, width=30, state=DISABLED)
        entry.grid(row=row, column=column, padx=5, pady=5,ipady=1)
        return entry

    def _validate_button(self, text, row,  column, entry, entry2):
        button = tk.Button(self.buttons, width=15, font=self.button_fonts, text=text, command=lambda: self.controller.validate(
            self.program_frame, entry, entry2, self.security_frame, self.errors, self.success, self.error_label, self.success_label),background="green",foreground="white")
        button.grid(row=row, column=column, padx=5, pady=10)

    def _copy_button(self, text, row, column):
        button = tk.Button(self.buttons, font=self.button_fonts, width=14, text=text, command=lambda: self.controller.copy_to_clipbaord(
            self.serial_num.get(), self.errors, self.success,  self.error_label, self.success_label))
        button.grid(row=row, column=column, padx=30, pady=10)

    def _paste_button(self, text, row, column):
        button = tk.Button(self.buttons, width=15, text=text,
                           command=lambda: self._serial_entry.insert(pyperclip.paste()))
        button.grid(row=row, column=column, padx=30, pady=10)
