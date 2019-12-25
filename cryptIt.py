import decrypt
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Menu
from PIL import Image, ImageTk
from tkinter.colorchooser import *
import action
import cv2, sys
import os,webbrowser
import pyperclip
from io import StringIO, BytesIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import subprocess

class Application(tk.Tk):
    def __init__(self, txti):
        tk.Tk.__init__(self)
        self.geometry('700x400')
        self.values=[]
        #self.configure(bg="#333")
        self.menuItems()
        if __name__ == "__main__":
            self.firstImage()
            name=self.buttonss()
        self.bind("<Z>",self.toggle)
            
    
    def onbtn(self):
        value=list(self.entry.get())
        return "Mokandu"
            
    
    def onbtn2(self):
        print(self.onbtn())
    def exitsys(self):
        exit()
    def runInTerminal(self):
        subprocess.call(['python3' ,'test.py'])
        #os.system("gnome-terminal -e 'bash -c \"python3 test.py; bash\" '")
    def copyKey(self, event=None):
        self.Action=action.Action
        file = tk.filedialog.askopenfilename(filetypes = (("All files","*.*"),("Text files","*.txt")))
        with open(file, 'r+') as key:
            text= key.read()
            key.close()
            pyperclip.copy(text)
            spam= pyperclip.paste()
            print(spam)
            
        exit()
    def openVideo(self):
        cap=cv2.VideoCapture("encryptiondecryption.mp4")
        if (cap.isOpened()==False):
            messagebox.showerror("Video error", "Failed to open video stream")
        while(cap.isOpened()):
            ret,frame=cap.read()
            if ret ==True:
                cv2.imshow('cryptIt encryption/decryption',frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
    def openWeb(self):
        webbrowser.open_new("https://cryptography.io")
    def opendoc(self):
        webbrowser.open_new("/home/brianbrix/Desktop/FLASH/Projo/s19MO.docx")
    def menuItems(self):
        menu= Menu(self)
        
        editmenu=Menu(menu, tearoff=0)
        viewmenu=Menu(menu, tearoff=0)
        toolsmenu=Menu(menu, tearoff=0)
        helpmenu=Menu(menu, tearoff=0)
        menusList=[editmenu, viewmenu, toolsmenu, helpmenu]
        menuTitles=[ 'File', 'View', 'Tools', 'Help']
        
        editmenus=['Copy key', 'Preferences', 'Exit']
        editCommands=[self.copyKey,2,self.exitsys]
        editAccs=['Shft+C',2,'Escape']
        self.bind("<Escape>",sys.exit)
        self.bind('<C>', self.copyKey)
        viewmenus=['Zoom','Developer mode', 'Change color']
        viewAccs=['Z',"",""]
        viewCommands=[self.toggle,2, self.getColor]
        toolsmenus=['Run crypt in terminal','Convert to plaintext','View Examples', 'Learn cryptography']
        toolsCommands=[self.runInTerminal,self.convertText,self.openVideo,self.openWeb]
        helpmenus=['Manual','Keyboard shortcuts', 'cryptIt documentation', 'Donate', 'About']
        helpCommands=[1,2,self.opendoc,3,4]
        for x in range(len(menusList)):
            menu.add_cascade(label=menuTitles[x], menu=menusList[x], font=("Arial Normal", 10))
        
        
        for i in range(len(editmenus)):
            editmenu.add_command(label=editmenus[i],command=editCommands[i],font=("Arial Normal", 10), accelerator=editAccs[i])
            
            if i%2!=0:
                editmenu.add_separator()
        for i in range(len(viewmenus)):
            viewmenu.add_command(label=viewmenus[i], command=viewCommands[i], font=("Arial Normal", 10), accelerator=viewAccs[i])
        for i in range(len(toolsmenus)):
            toolsmenu.add_command(label=toolsmenus[i],command=toolsCommands[i],font=("Arial Normal", 10))
        for i in range(len(helpmenus)):
            helpmenu.add_command(label=helpmenus[i],font=("Arial Normal", 10),command=helpCommands[i])
        self.config(menu=menu)
    def toggle(self, event=None):
        self.geometry('700x600')
    def firstImage(self):
        load = Image.open("back.jpg")
        load= load.resize((250,600), Image.ANTIALIAS)#(height, width)
        render = ImageTk.PhotoImage(load)
        img= tk.Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)
    def getColor(self):
        color= askcolor()
        self.configure(bg=color[1])
        return color[1]
        
    def buttonss(self):
        self.Action=action.Action
        self.decrypt=decrypt.Decrypt
        bt=tk.Button(self, text='Select color', command=self.getColor)
        btnenc= tk.Button(self, text='Encrypt', width=20, height=12, command=self.Action)
        btnenc.place(x=260,y=150)
        btnenc= tk.Button(self, text='Decrypt', width=20, height=12, command=self.decrypt)
        btnenc.place(x=500,y=150)
     
      
    def clicke(self):
        btn=tk.Button(self, text='Click', command=self.algs)
        btn.place(x=300, y=70)
    def algs(self):
        self.comb= tk.Label(text="Select an algorithm")
       
        option=tk.IntVar()
        
        self.combo=ttk.Combobox(self,state='readonly', height=3, textvariable=option)
        self.combo['values']=('AES','DES','BLOWFISH')
        self.combo.bind('<<ComboboxSelected>>', self.justamethod)
        self.combo.current(0)
                   
        self.comb.place(x=300, y=20)
        self.combo.place(x=300,y=50)
        if self.combo.get()=="AES":
            return self.combo.current(1)
        
    def convert(self,fname, pages=None):
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = open(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close
        return text 
            
    
    def convertText(self):
        file = tk.filedialog.askopenfilename(filetypes = (("all files","*.*"),("Text files","*.txt")))
        extension=file.split(".")[-1]
        if extension=="pdf":
            text=self.convert(file)
            textFileName=file+".txt"
            textFile= open(textFileName,"w")
            textFile.write(text)
            txtfile=textFile.name
            print(txtfile)
            tk.messagebox.showinfo("File converted to plain text", "The file is located in "+ txtfile)
            return txtfile
            
        else:
            file=file
            tk.messagebox.showerror("File not converted", "The file was not converted.Choose pdf file type for conversion")
            return file

           
        
if __name__ == "__main__":
    app = Application('new')
   
    app.title('cryptIt')
    app.resizable(width=False, height=False)
    app.mainloop()
       
    