from Tkinter import *

import time
 
class JamDigital:
    """ Kelas Jam Digital"""
     
    def __init__(self, parent, title):
        self.parent = parent
         
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onTutup)
        self.parent.resizable(False, False)
         
        
        self.teksJam = StringVar()
         
        self.aturKomponen()
        
        self.update()
         
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
         
        self.lblJam = Label(mainFrame, textvariable=self.teksJam,
            font=('Helvetica', 40))
        self.lblJam.pack(expand=YES)
         
        self.lblInfo = Label(mainFrame, text="Ucilinside",
            fg='red')
        self.lblInfo.pack(side=TOP, pady=5)
         
    def update(self):
        
        datJam = time.strftime("%H:%M:%S", time.localtime())
         
        
        self.teksJam.set(datJam)
         
       
        self.timer = self.parent.after(1000, self.update)
         
    def onTutup(self, event=None):
        self.parent.destroy()
         
if __name__ == '__main__':
    root = Tk()
     
    app = JamDigital(root, "Jam Digital")
     
    root.mainloop()
