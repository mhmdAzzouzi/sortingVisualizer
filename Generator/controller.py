from screen import Screen
import os
import sys
import random
import tkinter as tk

class Controller():

        

        def __init__(self):
            self.view = Screen(self)
        # correct key letters
       
        def generate(self, licenseString , serial_text):
            self.clear_text(licenseString)
          
            self.serial_number = str(serial_text.get())
            key = self.generate_key(str(serial_text.get()))
            # self.disable_button(self.view.generate_button)
            licenseString.set(key)

        def clear_text(self, entry):
            entry.set("")

        def main(self):
                self.view.main()

        # def getMachine_addr(self):
        #     os_type = sys.platform.lower()
        #     if "win" in os_type:
        #         command = "wmic bios get serialnumber"
        #     elif "linux" in os_type:
        #         command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
        #     elif "darwin" in os_type:
        #         command = "ioreg -l | grep IOPlatformSerialNumber"
        #     return os.popen(command).read().replace("SerialNumber", "").replace("\n", "").replace("	", "").replace(" ", "")

        def validate(self, key):
                # the char to check
                print("key generated : " + key)
                check_digit = key[1]
                # divide the chunks of key into an array ["aaaa" , "bbbb" , "cccc"] etc..
                key_divided = key.split("-")
                # # main counters
                check_digit_count = 0
                # score = 0

                # loop through each chunk and check for validity
                for chunk in key_divided:
                    for letter in chunk:
                        # check for chunk sizes first
                        if len(chunk) != 4:
                            return False
                        # count the check digit
                        if check_digit == letter:
                            check_digit_count += 1
                        # # check for characters matching Serial Number characters
                        if letter not in self.serial_number:
                            print(letter)
                            return False
                        # score += ord(letter)
                # if loops ends without return then the check the rules
                if  True:
                    return True
                else:
                    return False

        def generate_key(self , serial_number):
                key = ""
                chunk = ""
                print(serial_number)
                # the key should be 24 characters long with "-" every 4 characters
                while(len(key) < 25):
                    letter = random.choice(serial_number)
                    key += letter
                    chunk += letter
                    # reset the chunk after 4 characters added to the key and place a " - " after it
                    if len(chunk) == 4:
                        key += "-"
                        chunk = ""

                # check for key validity
                try:
                    if self.validate(key[:-1]):
                        key = key[:-1]
                        print(key)
                        return key
                    else:
                        return self.generate_key()
                except:
                    print("oops :( run again ")
                    return ""
        
        
        def save_key(self, key):
            if len(key) == 0:
                pass
            else:
                with open(os.path.join("./Generator", "LicenseKey.txt" ), "w") as file:
                    file.write(self.serial_number + " : " + key)
                    self.view.quit()
          

        def disable_button(self, button):  
            if self.retrieve_key:
                button['state'] = tk.DISABLED
                pass
            else:
                button['state'] = tk.NORMAL          

        def retrieve_key(self ):
            with open(os.path.join("./Generator", "LicenseKey.txt") , "r") as file:
                first_line = file.readlines(1)
                key_from_file = first_line[0].split(":")[1].strip()
                print(self.serial_number + " : " + key_from_file)
                if len(key_from_file) > 0:
                   return True
                else:
                  return False

