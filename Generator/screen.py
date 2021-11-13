import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, NW, SW, W
from PIL import Image, ImageTk
import os
import sys
class Screen(tk.Tk):


        def __init__(self, controller):
              super().__init__()
              super().title("License Key Generator")
              super().geometry("700x300")
              self.controller = controller
              self._main_frame_1()

        def quit(self):
            super().destroy()

        def main(self):
           self.mainloop()
              
        def _main_frame_1(self):
             self.frm = tk.Frame(self)
             self.frm.place(relx=0.5, rely=0.6, anchor=CENTER)
             self.licenseKey = tk.StringVar()
             self.serial = tk.StringVar()

            #  tkimage = ImageTk. PhotoImage(file="main\key.png")   
            #  self._image_label(tkimage , 1, 0, self.frm )

             self._create_label(
                 "serial_number", 2, 0, self.frm)
             self._create_label(
                 "key_generated", 3, 0, self.frm)    
             self._create_entry_active(2,1)
             self._create_entry(3, 1)
             
             self.generate_button = self._generate_button("Generate", 4, 0)
             self._save_button("Save And Exit ", 4, 1)

 

        def _create_entry(self, row, column):
             entry = tk.Entry(self.frm, textvariable=self.licenseKey,
                         width=40, state="disabled")
             entry.grid(row=row, column=column, columnspan=1, padx=5, pady=5)


        def _create_entry_active(self, row, column):
            entry = tk.Entry(self.frm , textvariable=self.serial , width=40 )
            entry.grid(row = row , column=column , columnspan= 1 , padx=5 , pady=5)
    
             

        def _create_label(self, text, row, column, frame):
            label = ttk.Label(frame, text=text)
            label.grid(row=row, column=column, columnspan=1, pady=5)


        def _generate_button(self, text, row, column):
            button = tk.Button(self.frm, fg='green', text=text, width=20 , command=lambda: self.controller.generate(self.licenseKey, self.serial ))
            button.grid(row=row, column=column, padx=5, pady=5)
            return button

    
        def _save_button(self, text, row, column):
            button = tk.Button(self.frm, fg='black', text=text,
                           width=20, command = lambda: self.controller.save_key(self.licenseKey.get()))
            button.grid(row=row, column=column, padx=2, pady=5)

        # def _image_label(self, image , row , column , frame):
        #        label = tk.Label(frame, image=image) 
        #        label.grid(row=row, column=column, columnspan=2)
               

