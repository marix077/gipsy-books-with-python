from uuid import uuid4

class theme :
    #   fields
    __button_style = {}
    __label_style = {}
    __entry_style = {}
    __window_style = {}
    __id = ""
    #######################
    
    #   constructor 
    def __init__(self) : 
        self.__id = uuid4()
    ###############################################
    
    #   setters
    def SetButtonStyle(self, style) : 
        self.__button_style = style
    
    def SetLableStyle(self, style) : 
        self.__label_style = style

    def SetEntryStyle(self, style) : 
        self.__entry_style = style

    def SetWindowStyle(self, style) : 
        self.__window_style = style
    ###############################################

    #   getters
    def GetButtonStyle(self) : 
        return self.__button_style

    def GetLableStyle(self) : 
        return self.__label_style
    
    def GetEntryStyle(self) : 
        return self.__entry_style
    
    def GetWindowStyle(self) : 
        return self.__window_style
    ###############################################