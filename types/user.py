class user : 
    #   field
    __username = ""
    __password = ""

    ###############################


    #   constructor
    def __init__(self, username, password) : 
        self.__username = username
        self.__password = password

        
    #################################

    #   setters

    def SetUserame(self, username) : 
        self.__username = username

    def SetPassword(self, password) : 
        self.__password = password

    ################################

    #   getters

    def GetUsername(self) : 
        return self.__username
    
    def GetPassword(self) : 
        return self.__password

    #############################


    
