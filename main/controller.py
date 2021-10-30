
from view import View
from model import Model
from SerialNumber import LicenseKey
class Controller:
    

    def change_frame(self, frame):
        frame.destroy()
        self.view._main_frame_2()


    def verify(self, entry, frame , generated_info):
            self.clear_text(entry)
            key = generated_info.generate_key()
            entry.set(key)
  

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