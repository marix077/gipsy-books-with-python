from uuid import uuid4 # for generate id

class folder : 
    #   fields
    __name = ""
    __id = ""
    __count = 0
    __books = []
    #############################


    def __init__(self, name) : 
        self.__id = uuid4()
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

    def RemoveBook(self, id) : 
        for book in self.__books : 
            if book.GetId() == id : 
                self.__books.remove(book)
                return True
        
        return False
    
    

    