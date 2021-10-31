
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import CENTER, W
from SerialNumber import LicenseKey

class View(tk.Tk):

    
    #constructor to initialize the view class
    def __init__(self, controller) :
          super().__init__()
          super().title("Sorting Algorithm Visualizer")
          super().geometry("900x600")
          self.controller = controller
          self._main_frame_1()
          self.generated_info = LicenseKey()
        

   
    #main function to run the program
    def main(self): 
        self.mainloop()

    # this is to create a center frame 
    def _main_frame_1(self):
       self.frm = ttk.Frame(self)
       self.frm.place(relx=0.5, rely=0.6, anchor=CENTER)
       self.licenseKey = tk.StringVar()
       self._create_label("Generate Your license key and press save", 1 , 0 , self.frm)
       self._create_entry(2, 0)
       self._verify_button("Generate" , 3, 0)
       self._save_button("Save" , 4, 0 )
       self._clear_button("Clear" , 3 , 1)

   # this is to create a  frame 2 
    def _main_frame_2(self):
        self.frm2 = tk.Frame(self)
        self.frm2.place(relx=0.5, rely=0.6, anchor=CENTER)
        self._create_label("welcome" , 0, 0, self.frm2 )


    # def _main_frame_3():


   #this is to create frame 3 
    def user_menu(self):
        self.frm3 = tk.Frame(self, width=600, height=200, bg='grey')
        self.frm3.grid(row=0, column=0, padx=10, pady=5)
        self._create_label_frame3("Algorithm : ", 0, 0, self.frm3)
        self._create_label_frame3("Size : ", 1, 0, self.frm3)
        self._create_label_frame3("Min Value : ", 1, 2, self.frm3)
        self._create_label_frame3("Max Value : ", 1, 4, self.frm3)
        self._create_entry_frame3(1, 1)
        self._create_entry_frame3(1, 3)
        self._create_entry_frame3(1, 5)
        self._create_combobox_frame3(['Bubble Sort', 'Merge Sort'],0,1,self.frm3)
        self._generate_button_3("Generate", 0, 2)


  #message box
    def message(self):
        msg  ="the license " + self.licenseKey.get() + " that you entered is invalid"
        text = tk.Label(self.frm , text=msg , fg="red")
        text.grid(row=0, column=0, columnspan=2, padx=5, pady=5)


    # a function to create input box on frame 1
    def _create_entry(self, row , column):
        entry = tk.Entry(self.frm, textvariable=self.licenseKey , width=40, state="disabled")
        entry.grid(row= row , column=column , columnspan=2, padx=5 , pady=5)
        
    # a function to create a labe on frame 2
    def _create_label(self , text , row , column, frame):
        label = ttk.Label(frame , text=text, textvariable=self.licenseKey )
        label.grid(row=row , column = column, columnspan=2,  padx=5, pady=5 )

    #clear button in frame 1
    def _clear_button(self, text, row, column):
        button = tk.Button(self.frm, fg='red',  text=text , width= 20 , command=lambda: self.controller.clear_text(self.licenseKey))
        button.grid(row=row , column=column , padx=5, pady=5)

    #verify button in frame 1
    # , command=lambda: self.controller.verify(self.licenseKey, self.frm , self.generated_info)
    def _verify_button(self, text, row , column):
        button = tk.Button(self.frm, fg='green', text=text , width=20,  command=lambda: self.controller.verify(self.licenseKey, self.frm , self.generated_info))        
        button.grid(row=row , column=column , padx=5, pady=5)

    def _save_button(self, text, row , column):
        button = tk.Button(self.frm, fg='black', text=text , width=20 , command=lambda: print("done"))        
        button.grid(row=row , column=column , columnspan=2, padx=2, pady=5 )

    def _create_label_frame3(self, text, row, column, frame):
        label = tk.Label(frame, text=text, fg='grey')
        label.grid(row=row, column=column, padx=5, pady=5, sticky=W)
        
    def _create_combobox_frame3(self, values, row,column,frame):
        combobox = ttk.Combobox(frame, values=values)
        combobox.grid(row=row, column=column, padx=5, pady=5)

    def _create_entry_frame3(self, row, column):
        entry = tk.Entry(self.frm3)
        entry.grid(row=row, column=column, padx=5, pady=5, sticky=W)

    def _generate_button_3(self, text, row, column):
        button = tk.Button(self.frm3, fg='red', text=text, command=lambda: self.sortingAlgo.Generate())
        button.grid(row=row, column=column, padx=2, pady=5)