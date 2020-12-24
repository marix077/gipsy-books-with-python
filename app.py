from sys import path
path.append("./services")

from uiService import ui
from managerService import manager

class app : 
    def __init__(self): 
        self.__ui = ui(self, "gipsy", width="800", height="600", x="100", y="100")
        self.__manager = manager()


