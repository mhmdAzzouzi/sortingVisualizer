
from view import View
from model import Model

class Controller:
    
    def print_world(self):
        print("hello world and hi")

    def change_frame(self, frame):
        frame.destroy()
        self.view._main_frame_2()


    def verify(self, entry, frame):
        if entry.get() == "123123":
            self.change_frame(frame) 
        else:
            self.view.message()   

    def clear_text(self , entry):
        entry.set("")


    def __init__(self) :
        self.view = View(self)
        self.model = Model()

    def main(self):
        self.view.main()

if __name__ == "__main__":
      appCont = Controller()
      appCont.main()