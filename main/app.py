from screen import View
import os
import sys
import pyperclip

class Controller:

    def get_serial_number(self , entry):
        self.serial_number = os.popen("wmic diskdrive get SerialNumber").read().replace("SerialNumber", "").replace("\n", " ").strip().split(" ")[0]
        entry.set(self.serial_number)
        return self.serial_number


    def deformat_string(self, key):
                key = key.split("-")
                key = ''.join(key)
                key = key[::-1]

                if len(key) %2== 1:
                    s1 = key[:(len(key)+1)//2]
                    s2 = key[(len(key)+1)// 2:]
                else:
                    s1 = key[:(len(key))//2]
                    s2 = key[(len(key))// 2:]
                
                key = s2 +s1;

                array = [key[i:i + 2] for i in range(0, len(key), 2)]
                for i, pair in enumerate(array):
                        pair = pair[::-1]
                        array[i] = pair;
                deformatted = ''.join(array)
                return deformatted

    def validate(self, program_frame , serial, license, security_frame ):
        print(self.deformat_string(license.get()))
        if len(serial.get()) <=0 or len(license.get()) <=0:
            return
        elif self.deformat_string(license.get()) == serial.get():
            self.save_key(license.get() , serial.get())
            security_frame.destroy()
            self.view.root.maxsize(900,600)
            self.view.root.geometry("680x510")
            program_frame()
       
    def copy_to_clipbaord(self, licenseKey, error, success ):
                try:
                    if len(licenseKey) <= 0:
                        success.set("")
                        error.set("Please generate a key to copy")
                    else:
                        pyperclip.copy(licenseKey)
                        error.set("")
                        success.set("serial number copied to clipboard ")
                except:
                    print("failed to copy to clipboard")

    def __init__(self):
        self.view = View(self)


    def main(self):
        
        self.view.main()

    def save_key(self, key, serial):
            if len(key) == 0:
                pass
            else:
                with open(os.path.join("main", "LicenseKey.txt" ), "w") as file:
                    file.write(serial + " : " + key)
                    
                  

if __name__ == "__main__":
    appCont = Controller()
    appCont.main()
