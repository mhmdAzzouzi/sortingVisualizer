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
            licenseString.set(key)

        def clear_text(self, entry):
            entry.set("")

        def main(self):
                self.view.main()
    

        def format_str( self, serial):
                array = [serial[i:i + 2] for i in range(0, len(serial), 2)]
                for i, pair in enumerate(array):
                        pair = pair[::-1]
                        array[i] = pair;
                answer = ''.join(array)
                s1 = answer[:len(answer)//2]
                s2 = answer[len(answer)//2:]
                flippedString = s2 + s1; 
                flippedString = flippedString[::-1]  

                return flippedString

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

        def generate_key(self , serial_number):
                key = ""
                chunk = ""
                print(serial_number)
                # the key should be 24 characters long with "-" every 4 characters
                serial_number = self.format_str(serial_number)
        
                for letter in serial_number:
                    key += letter
                    chunk+=letter
                    if len(chunk) == 4:
                        key+="-"
                        chunk=""
                if len(key) <=0:
                    return ""
                if key[len(key)-1] == "-":
                    return key[:-1]
                else:
                    return key
        
        def save_key(self, key):
            if len(key) == 0:
                pass
            else:
                with open(os.path.join("./Generator", "LicenseKey.txt" ), "w") as file:
                    file.write(self.serial_number + " : " + key)
                    self.view.quit()
                  

        def retrieve_key(self ):
            with open(os.path.join("./Generator", "LicenseKey.txt") , "r") as file:
                first_line = file.readlines(1)
                key_from_file = first_line[0].split(":")[1].strip()
                print(self.serial_number + " : " + key_from_file)
                if len(key_from_file) > 0:
                   return True
                else:
                  return False

