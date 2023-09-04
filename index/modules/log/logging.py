
import os

class Logging():
    def __init__(self):
        pass
    
    def excepting_directory(self, is_true):
        if(
            is_true == True
        ):
            return "FileIsExists"
        else:
            return None