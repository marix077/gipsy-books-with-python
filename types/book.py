class book :

    #Private fields
    __bookTitle = ""
    __author = ""
    __publisher = ""
    __language = ""
    __subject = ""
    __shabok = ""


    #The constructor receives the book information class
    def __init__ (self , bookTitle , author , publisher , language , subject , shabok):
        self.__bookTitle = bookTitle
        self.__author = author
        self.__publisher = publisher
        self.__language = language
        self.__subject = shabok
        self.__shabok = subject

    #Returns book information
    def __repr__(self):
        return f"book title:{self.__bookTitle}   author:{self.__author}   publisher:{self.__publisher}"
