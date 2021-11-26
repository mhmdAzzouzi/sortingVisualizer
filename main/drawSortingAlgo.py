import tkinter as tk
from tkinter import ttk
from tkinter import*
# to create a new random array
import random
from tkinter import font


from Algorithms import Algorithms
# from main.screen import View
# # function to take an array with the data to draw


class sortingAlgorithm:
    def __init__(self, View):
        self.root = View.root
        self.algorithms_class = Algorithms()
        pass

    def drawData(self, data, frame, colorArray):
        # to restart from the beginning
        Canvas = tk.Canvas(frame, width=600, height=380, bg="#db07a6")
        Canvas.delete("all")
        c_height = 380
        c_width = 600
        # width of the var graphs which it will be calculated because we need to scale it and not have it set
        x_width = c_width/(len(data)+1)
        # we don't want to start at the borders
        offset = 40
        spacing = 10
        # we need to normalize values from 0 to 1 so we have to make the exact same size
        normalizedData = [i / max(data) for i in data]
        # i is the iterator ofc
        # The enumerate() function allows you to loop over an iterable object and keep track of how many iterations have occurred.
        for i, height in enumerate(normalizedData):
            # top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 340
            # bottom right
            x1 = (i + 1) * x_width + offset
            y1 = c_height
            Canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            Canvas.create_text(x0+2, y0, anchor=SW,
                               text=str(data[i]), fill="white")

        Canvas.grid(row=1, column=0, padx=10, pady=5)
        self.root.update_idletasks()
    # function for the button

    def Generate(self, minval, maxval, sizef, frame, label):
        # here we are tryin to catch all the exceptions of our work
        label.destroy()
        try:
            minVal = int(minval.get())
        except:
            minVal = 1
        try:
            maxVal = int(maxval.get())
        except:
            maxVal = 15
        try:
            size = int(sizef.get())
        except:
            size = 13
        # if else statements for exceptions too
        if minVal < 0:
            minVal = 0
        if maxVal > 100:
            maxVal = 100
        if size > 30 or size < 3:
            size = 25
        if minVal > maxVal:
            # swap between min and max
            minVal, maxVal = maxVal, minVal

        self.data = []
        # loop for the empty array
        for _ in range(size):
            self.data.append(random.randrange(minVal,maxVal))
            # randomValues = random.sample(random.randrange(minVal, maxVal), 2)
            # self.data.append(random.sample(randomValues))
            
        self.drawData(self.data, frame, [
                      "#8f3cb5" for x in range(len(self.data))])

    def start_algorithm(self, speedScale,frame,combo): #,value
        # if value == 'Merge Sort':
            if combo.get() == "Merge Sort":
                self.algorithms_class.merge_sort(
                self.drawData, self.data, speedScale.get(), frame )
            
            elif combo.get() == 'Bubble Sort':
                self.algorithms_class.bubble_sort(
                self.drawData, self.data, speedScale.get(), frame)
            elif combo.get() == "Quick Sort":
                print(speedScale)
                self.algorithms_class.quick_sort(self.data , 0 , len(self.data) -1, self.drawData,  speedScale.get() , frame)