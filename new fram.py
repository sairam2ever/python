from tkinter import *
root = Tk()

 
class Frames(object):
 
    def newWindow(self): # new window definition
        newwin = Toplevel(root)
        newwin.title('New Window')
        newwin.geometry("300x300") 
        newwin.resizable(100, 300)
    
        canvas1 = Label(newwin, text="SAIRAM !", fg='green', font=('helvetica', 12, 'bold'))
        canvas1.pack()
    
    def mainFrame(self,root):
        root.title('Open New Window!!!')
        root.geometry("500x500") 
        root.resizable(500, 500)
        button1 = ()
        canvas1 = Label(root,text="What is your name?:", fg='blue', font=('helvetica', 12, 'bold'))
        canvas1.pack()
        button1 =Button(root, text ="Click to answer", bg='blue', fg='white', font=('helvetica', 12, 'bold'), command =self.newWindow)
        button1.place(x = 100, y = 100, width=200, height=50)
 
app = Frames()
app.mainFrame(root)
root.mainloop()