class book :

    #Private fields
    _bookTitle = ""
    _author = ""
    _publisher = ""
    _language = ""
    _subject = ""
    _shabok = ""


    #Book title property
    @property
    def BookTitle (self):
        return self._bookTitle

    @BookTitle.setter
    def BookTitle (self , value):
        try:
            self._bookTitle = value
        except:
            self._bookTitle = ""


    #Author property
    @property
    def Author (self):
        return self._author

    @Author.setter
    def Author (self , value):
        try:
            self._author = value
        except:
            self._author = ""


    #Publisher property
    @property
    def Publisher (self):
        return self._publisher

    @Publisher.setter
    def Publisher (self , value):
        try:
            self._publisher = value
        except:
            self._publisher = ""

    #language property
    @property
    def Language (self):
        return self._language

    @Language.setter
    def Language (self , value):
        try:
            self._language = value
        except:
            self._language = ""



    #Subject property
    @property
    def Subject (self):
        return self._subject

    @Subject.setter
    def Subject (self , value):
        try:
            self._subject = value
        except:
            self._subject = ""


    #Shabok property
    @property
    def Shabok (self):
        return self._shabok

    @Shabok.setter
    def Shabok (self , value):
        try:
            self._shabok = value
        except:
            self._shabok = ""


    #The constructor receives the book information class
    def __init__ (self , bookTitle , author , publisher , language , subject , shabok):
        self.BookTitle = bookTitle
        self.Author = author
        self.Publisher = publisher
        self.Language = language
        self.Shabok = shabok
        self.Subject = subject

    #Returns book information
    def __repr__(self):
        return f"book title:{self.BookTitle}   author:{self.Author}   publisher:{self.Publisher}"



Who_replaced_my_cheese = book("Who replaced my cheese?" , "Spencer Johnson" , "yad aref" , "farsi" , "Transformation (Psychology)" , "964 - 7667 - 48 - 5" )

print(Who_replaced_my_cheese)