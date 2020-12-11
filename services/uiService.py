import tkinter

class ui(tkinter.Tk) :
    #   fields
    __menu_bar = None
    __file_menu = None
    __edit_menu = None
    __tools_menu = None

    #   constructor
    def __init__(self,app,title,**karg):
        tkinter.Tk.__init__(self)
        self.__app = app
        self.title(title)
        if 'width' in karg.keys() and 'height' in karg.keys() :
            self.__width = karg['width']
            self.__height = karg['height']
            if 'x' in karg.keys() and 'y' in karg.keys() :
                self.__x = karg['x']
                self.__y = karg['y']
                self.geometry(self.__width + "x" + self.__height + "+" + self.__x + "+" + self.__y)
            else :
                self.geometry(self.__width + "x" + self.__height)
        
        self.create_menu()
        self.mainloop()

    #   create items
    def create_menu(self) : 
        self.__menu_bar = tkinter.Menu(self)

        self.__file_menu = tkinter.Menu(self.__menu_bar, tearoff=0)
        self.__file_menu.add_command(label = "Add Book", command = self.not_implement)
        self.__file_menu.add_command(label = "Add Folder", command = self.not_implement)
        self.__file_menu.add_command(label = "Add Tag", command = self.not_implement)
        self.__file_menu.add_separator()
        self.__file_menu.add_command(label = "Exit", command = self.not_implement)
        self.__menu_bar.add_cascade(label = "File", menu = self.__file_menu)
        self.__edit_menu = tkinter.Menu(self.__menu_bar, tearoff=0)
        self.__edit_menu.add_command(label = "Edit Book", command = self.not_implement)
        self.__edit_menu.add_command(label = "Edit Folder", command = self.not_implement)
        self.__menu_bar.add_cascade(label = "Edit", menu = self.__edit_menu)

        self.__tools_menu = tkinter.Menu(self.__menu_bar, tearoff=0)
        self.__tools_menu.add_command(label = "Options", command = self.not_implement)
        self.__menu_bar.add_cascade(label = "Tools", menu = self.__tools_menu)

        self.config(menu = self.__menu_bar)

    def not_implement() : 
        pass
