from screen import Screen
import os
import sys
import random
import tkinter as tk

class Controller():

        

        def __init__(self):
            self.view = Screen(self)
            self.serial_number = self.getMachine_addr()
            print(self.serial_number)
        # correct key letters
            self.secret = self.serial_number[1] + "-" + self.serial_number[5]   
        
        def generate(self, licenseString):
            self.clear_text(licenseString)
            key = self.generate_key()
            self.disable_button(self.view.generate_button)
            licenseString.set(key)

        def clear_text(self, entry):
            entry.set("")

        def main(self):
                self.view.main()

        def getMachine_addr(self):
            os_type = sys.platform.lower()
            if "win" in os_type:
                command = "wmic bios get serialnumber"
            elif "linux" in os_type:
                command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
            elif "darwin" in os_type:
                command = "ioreg -l | grep IOPlatformSerialNumber"
            return os.popen(command).read().replace("SerialNumber", "").replace("\n", "").replace("	", "").replace(" ", "")

        def validate(self, key):
                # the char to check
                check_digit = self.serial_number[1]
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
                if check_digit_count == 2 and key[5] == self.secret[0]:
                    return True
                else:
                    return False

        def generate_key(self):
                key = ""
                chunk = ""

                # the key should be 24 characters long with "-" every 4 characters
                while(len(key) < 25):
                    letter = random.choice(self.serial_number)
                    key += letter
                    chunk += letter
                    # reset the chunk after 4 characters added to the key and place a " - " after it
                    if len(chunk) == 4:
                        key += "-"
                        chunk = ""

                # check for key validity
                try:
                    if self.validate(key):
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
                with open(os.path.join("./main", "LicenseKey.txt" ), "w") as file:
                    file.write("key : " + key)
                    self.view.quit()
          

        def disable_button(self, button):  
            if self.retrieve_key:
                button['state'] = tk.DISABLED
                pass
            else:
                button['state'] = tk.NORMAL          

        def retrieve_key(self ):
            with open(os.path.join("./main", "LicenseKey.txt") , "r") as file:
                first_line = file.readlines(1)
                key_from_file = first_line[0].split(":")[1].strip()
                print("key from file : " + key_from_file)
                if len(key_from_file) > 0:
                   return True
                else:
                  return False

