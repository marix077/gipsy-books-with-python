import uuid # for generate id
class folder : 
    #   fields
    __name = ""
    __id = ""
    __count = 0
    __books = []
    #############################


    def __init__(self, name) : 
        self.__id = uuid.uuid4()
        self.__name = name

    def SetName(self, name) : 
        self.__name = name

    def GetName(self) : 
        return self.__name

    def AddBook(self, book) : 
        self.__books.append(book)
        self.__count += 1
        
    def GetId(self) : 
        return self.__id
    
    

    