import tkinter

class ui(tkinter.Tk) :
    def __init__(self,app,title,**karg):
        tkinter.Tk.__init__(self)
        self.m_app = app
        self.title(title)
        if 'width' in karg.keys() and 'height' in karg.keys() :
            self.m_width = karg['width']
            self.m_height = karg['height']
            if 'x' in karg.keys() and 'y' in karg.keys() :
                self.m_x = karg['x']
                self.m_y = karg['y']
                self.geometry(self.m_width + "x" + self.m_height + "+" + self.m_x + "+" + self.m_y)
            else :
                self.geometry(self.m_width + "x" + self.m_height)
        
        self.mainloop()


