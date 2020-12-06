from uuid import uuid4

class tag :
    #    fields 
    __id = ""
    __name = ""
    __is_active = True
    ################################3
    
    
    #    constructor 
    def __init__(self, name) : 
        self.__id = uuid4()
        self.__name = name
        self.__is_active = True
    ##############################################
    
    
    def remove(self) : 
        self.__is_active = False
        
        
    
        
    