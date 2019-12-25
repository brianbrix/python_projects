import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from PIL import Image, ImageTk
from tkinter import filedialog

from cryptIt import Application as app

class Action(app):
    def __init__(self):
        app.__init__(self)
        self.geometry('400x300')
        self.configure(bg="#333")
        self.title('cryptIttt')
        
        
        
    def encFile(self):
        frame= tk.LabelFrame(width=50, height=100, text="Encrypt File")
        frame.grid(column=0, row=1)
        label = tk.Label(frame, text="This Label is packed\nwithin the LabelFrame.", width=100, justify=tk.LEFT)
        label.grid(column=0, row=2)
        btn = tk.Button(frame,text="Browse file", command=self.browse)
        btn.grid(column=0, row=4)
        
    def butt(self):
        btn = tk.Button(text="Browse file", command=self.browse)
        btn.grid(column=3, row=6)
    def browse(self):
        file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
        lb= tk.Label(self,text=file)
        lb.grid(column =5, row=4)
        
        
        
        
if __name__=="__main__":
    
    pass