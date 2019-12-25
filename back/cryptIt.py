import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from PIL import Image, ImageTk


'''
causing a widget to appear in tkinter requires use of "geometry managers".
the three managers are:
grid-for laying widgets in a grid. you can specify rows and co,umns, row and column spans etc
e.g
b = tk.Button()
b.grid(row=2, column=6, columnspan=4)

pack-uses a box metaphor, letting you pack widgets along one of the sides of a conttainer
.it is good at all-vertical or all-horizontal 
b= tk.Button()
b.pack(side="top", fill='both', expand=True, padx=4, pady=4)

place--least used . you can specify exact x/y location and exact width/height for a widget
b=tk.Button()
b.place(relx=.5, rely=.5 , anchor="c")

'''
import action

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('700x500')
        
        self.Action=action.Action
        self.configure(bg="#333")
        self.menuItems()
        if __name__ == "__main__":
            self.firstImage()
            self.buttonss()
            self.algs()
            self.clicke()
        
        
    def menuItems(self):
        menu= Menu(self)
        
        editmenu=Menu(menu, tearoff=0)
        viewmenu=Menu(menu, tearoff=0)
        toolsmenu=Menu(menu, tearoff=0)
        helpmenu=Menu(menu, tearoff=0)
        menusList=[editmenu, viewmenu, toolsmenu, helpmenu]
        menuTitles=[ 'Edit', 'View', 'Tools', 'Help']
        
        editmenus=['Import', 'Export', 'Copy key', 'Paste key', 'Algorithm','Mode', 'Preferences']
        viewmenus=['Fullscreen mode','Developer mode', 'Text encoding']
        toolsmenus=['Run crypt in terminal','Browse file with cryptIt','View Examples','Test source with cryptIt', 'Learn cryptography']
        helpmenus=['Manual','Keyboard shortcuts', 'cryptIt documentation', 'Donate', 'About']
        for x in range(len(menusList)):
            menu.add_cascade(label=menuTitles[x], menu=menusList[x], font=("Arial Normal", 10))
        
        
        for i in range(len(editmenus)):
            editmenu.add_command(label=editmenus[i],font=("Arial Normal", 10))
            if i%2!=0:
                editmenu.add_separator()
        for i in range(len(viewmenus)):
            viewmenu.add_command(label=viewmenus[i], font=("Arial Normal", 10))
        for i in range(len(toolsmenus)):
            toolsmenu.add_command(label=toolsmenus[i],font=("Arial Normal", 10))
        for i in range(len(helpmenus)):
            helpmenu.add_command(label=helpmenus[i],font=("Arial Normal", 10))
        self.config(menu=menu)
    def firstImage(self):
        load = Image.open("back.jpg")
        load= load.resize((250,600), Image.ANTIALIAS)#(height, width)
        render = ImageTk.PhotoImage(load)
        img= tk.Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)
        
    def buttonss(self):
        btnenc= tk.Button(self, text='Encrypt', width=20, height=12, command=self.Action)
        btnenc.place(x=260,y=180)
        btnenc= tk.Button(self, text='Decrypt', width=20, height=12 )
        btnenc.place(x=500,y=180)
    def clicke(self):
        btn=tk.Button(self, text='Click', command=self.algs)
        btn.place(x=300, y=70)
    def algs(self):
        self.comb= tk.Label(text="Select an algoritm")
       
        option=tk.StringVar()
        
        self.combo=ttk.Combobox(self,state='readonly', height=3, textvariable=option)
        self.combo['values']=('AES','DES','BLOWFISH')
        self.combo.bind('<<ComboboxSelected>>', self.justamethod)
        self.combo.current(0)
                   
        self.comb.place(x=300, y=20)
        self.combo.place(x=300,y=50)
        if self.combo.get()=="AES":
            return self.combo.current(1)
            
        
        
    def justamethod(self, event):
        print("method is called")
        print(self.algs())
           
        
if __name__ == "__main__":
    app = Application()
    app.title('cryptIt')
    app.mainloop()
       
    