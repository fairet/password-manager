
from modules.encryption import *
from datetime import datetime as dt

import json
import os

class Main():
    def parse(self, username: str):
        #TODO: Encryption, file_to: str, master_key
        
        try:
            with open('passwords/usernames.json', 'r') as file_with_usernames:
                usernames_as_data = json.load(file_with_usernames)
        
            return usernames_as_data['usernames'][username]
        except KeyError:
            print("[-] Username not found")
    def __init__(self):
        pass

    def show_options(self, username):
        return self.parse(self, username)
    
    def initialize(self):
        try:
            os.makedirs(name="passwords", exist_ok=True)
            
        except:
        # TODO: logging

            now = dt.now().strftime("%H_%M_%S")

            try:
                
                os.makedirs(name=f"{now}")
    
                with open(f'{now}/logging.log', 'w') as file:
                    file.write(f"[{dt.now().strftime('%d/%m/%Y %H:%M:%S')}] File is exists, all is ok")
                    print(f"[INFO] Has been created file {now}/logging.log")
            
            except:
                return None
        
    def main(self, master, username):
        master_parsed = "myMaster"
        if master == master_parsed:
            print(1555555555)
            # print(self.show_options(self, username=username))

        else:
            #print("[-] Your master is wrong")
        
            return "[-] Your master is wrong"