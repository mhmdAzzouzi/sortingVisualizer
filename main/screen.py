import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import CENTER, DISABLED, HORIZONTAL, SW, W

import pyperclip
from sortingAlgo import sortingAlgorithm
import os
import sys
class View(tk.Tk):

    # constructor to initialize the view class
    def __init__(self, controller):
        super().__init__()
        super().title("Sorting Algorithm Visualizer")
        super().maxsize(900,600)
        
        self.root = super()
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
    def retrieve_key(self ):
        try:
            with open(os.path.join("main", "LicenseKey.txt") , "r") as file:
                    first_line = file.readlines(1)
                    key_from_file = first_line[0].split(":")[1].strip()
                    serial_from_file = first_line[0].split(":")[0].strip()
                    print(key_from_file)
                    if self.controller.deformat_string(key_from_file) ==serial_from_file :
                      return True
                    else:
                      return False
        except:
            return False
             

    def main(self):
        self.mainloop()


    def security_frame(self):
        super().geometry("600x300")
        self.security_frame = tk.Frame(self)
        self.buttons = tk.Frame(self , width=20)
        self.security_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.buttons.place(relx=0.53, rely=0.6, anchor=CENTER)
        license= self._license_entry(1,1)
        serial= self._serial_entry(2,1)
        self.errors =tk.StringVar()
        self.success = tk.StringVar()
        self.message_label(0,0,self.security_frame,self.errors, "red")
        self.message_label(0,0,self.security_frame,self.success, "green")
        self._create_label("Serial number:  " , 1, 0 , self.security_frame , 1)
        self._create_label("License key:  " , 2, 0,  self.security_frame, 1)
        self.controller.get_serial_number(self.serial_num)
        self._validate_button("Check" , 0, 0 , license, serial)
        self._copy_button("Copy to clipboard" , 0,2)
   


    def program_frame(self):
        # super().geometry("900x600")
        self.program_frame = tk.Frame(self)
        self.program_frame.grid(row=0, column=0)
        self.user_menu()
        self.draw_frame()

    def user_menu(self):
        self.frm3 = tk.Frame(self.program_frame, width=600, height=200, bg='grey')
        self.frm3.grid(row=0, column=0, padx=10, pady=5)
        self.selected_alg = tk.StringVar()
        self._create_label_frame3("Algorithm : ", 0, 0, self.frm3)
        speedScale = self._speed_scale("Select Speed" , 0,4)
        self._start_button("Start Visualization" , 0 , 3 , speedScale)
        self._create_label_frame3("Size : ", 1, 0, self.frm3)
        self._create_label_frame3("Min Value : ", 1, 2, self.frm3)
        self._create_label_frame3("Max Value : ", 1, 4, self.frm3)
        minEntry = self._create_entry_frame3(1, 3)
        maxEntry = self._create_entry_frame3(1, 5)
        size = self._create_entry_frame3(1, 1)
        self._create_combobox_frame3(
            ['Bubble Sort', 'Merge Sort'], 0, 1, self.frm3)
        self._generate_button_3( "Generate", 0, 2,minEntry,maxEntry,size)
        

    def draw_frame(self):
        self.drawframe = tk.Frame(self.program_frame, width=600, height=380)
        self.drawframe.grid(row=1, column=0, padx=10, pady=5)
        
    # a function to create input box on frame 1

    # a function to create a labe on frame 2
    def _create_label(self, text, row, column, frame , span):
        label = ttk.Label(frame, text=text , width=15)
        label.grid(row=row, column=column,  padx=5, pady=5 , columnspan=span)

    def message_label(self,row,column ,frame, variable, color):
        label= tk.Label(frame , textvariable=variable, fg=color)
        label.grid(row= row, column= column, columnspan=2 )

    def _create_label_frame3(self, text, row, column, frame):
        label = tk.Label(frame, text=text)
        label.grid(row=row, column=column, padx=5, pady=5, sticky=W)

    def _create_combobox_frame3(self, values, row, column, frame):
        combobox = ttk.Combobox(frame, values=values)
        combobox.grid(row=row, column=column, padx=5, pady=5)

    def _create_entry_frame3(self, row, column):
        entry = tk.Entry(self.frm3)
        entry.grid(row=row, column=column, padx=5, pady=5, sticky=W)
        return entry

    def _generate_button_3(self, text, row, column, entry1,entry2,entry3):
        button = tk.Button(self.frm3, fg='red', text=text,
                           command=lambda: self.sortingAlgo.Generate(entry1,entry2,entry3, self.drawframe ))
        button.grid(row=row, column=column, padx=5, pady=5)
    
    def _start_button(self, text, row, column , speedScale):
        button = tk.Button(self.frm3, fg='green', text=text , command=lambda: self.sortingAlgo.start_algorithm(speedScale, self.drawframe ))
        button.grid(row=row, column=column)

    def _speed_scale(self, text, row, column):
        scale = tk.Scale( self.frm3 ,  from_=0.09, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label=text)
        scale.grid(row=row, column=column, columnspan=2, padx=5,pady=5)
        return scale

    def _serial_entry(self, row ,column):
        entry = tk.Entry(self.security_frame  , width=40)
        entry.grid(row =row , column=column, padx=5, pady=5)
        return entry

    def _license_entry(self, row, column):
        entry = tk.Entry(self.security_frame, textvariable=self.serial_num,width=40 ,state=DISABLED)
        entry.grid(row= row  ,column=column , padx=5, pady=5)
        return entry

    def _validate_button(self, text, row,  column , entry , entry2):
        button = tk.Button(self.buttons , width=15, text=text , command= lambda: self.controller.validate(self.program_frame, entry ,entry2 , self.security_frame ))
        button.grid(row= row , column=column, padx=5, pady=10)

    def _copy_button(self, text, row, column):
        button = tk.Button(self.buttons , width=15, text=text , command=lambda: self.controller.copy_to_clipbaord(self.serial_num.get(), self.errors , self.success  ))
        button.grid(row=row,column=column,padx=30, pady=10)
        