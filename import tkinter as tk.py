import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height =400)
canvas1.pack()

def name():
    newwin = Toplevel(root)
    newwin.title('New Window')
    newwin.geometry("200x100") 
    newwin.resizable(0, 0)
    
    
def mainFrame(self,root):
        root.title('Open New Window!!!')
        root.geometry("200x200") 
        root.resizable(0, 0)
        button1 =Button(root, text ="open new window", command =self.newWindow)
        button1.place(x = 50, y = 25, width=100, height=25)

root.mainloop()