from sys import path
path.append("./services")

from uiService import ui

class app : 
    def __init__(self): 
        self.__ui = ui(self, "gipsy", width="800", height="600", x="100", y="100")


