
import os
import sys
import random


class LicenseKey:

    def __init__(self):
        # output machine serial code: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX
        self.serial_number = self.getMachine_addr()
        print(self.serial_number)
        # correct key letters
        self.secret = self.serial_number[1] + "-" + self.serial_number[5]

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
