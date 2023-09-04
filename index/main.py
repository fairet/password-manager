
from modules.encryption import *
from datetime import datetime as dt

import json
import os

class Main():
    def parse(self):
        #TODO: Encryption, file_to: str, what_to_parse
        with open ( 'passwords/usernames.json', 'r' ) as file_with_usernames:
            usernames_as_data = json.load(file_with_usernames)
        
        return usernames_as_data['usernames']
    
    def __init__(self, passwords):
        self.passwords = passwords

    

    def show_options(self):
        print(self.passwords)
    
    def initialize(self):
        try:
            os.makedirs(name="passwords")
        except:
        # TODO: logging

            now = dt.now().strftime("%H_%M_%S")

            try:
                
                os.makedirs(name=f"{now}")
    
                with open(f'{now}/logging.log', 'w') as file:
                    file.write(f"[{dt.now().strftime('%d/%m/%Y %H:%M:%S')}] File is exists, all is ok")
                    print(f"[INFO] Has been created file {now}/logging.log")

                return None
            
            except:
                return None
        
    def main(self):
        pass

text = "Passw0rds"

main = Main(text)

main.show_options()