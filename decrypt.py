from action import Action as act
import tkinter as tk
from tkinter import ttk, simpledialog
from tkinter import Menu
from PIL import Image, ImageTk, ImageDraw
from tkinter import filedialog
from tkinter import messagebox
import os
from subprocess import Popen, PIPE
import random
import numpy as np
from io import StringIO, BytesIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import sys, getopt
import cv2,os, string
from random import *
import Crypto
from Crypto.Cipher import AES
from io import BytesIO
import base64, pyperclip
from zipfile import ZipFile
class Decrypt(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('400x300')
        self.title('cryptIt')
        self.values=[]
        self.efile=self.browse2()
    
     
    def browse2(self):
        file=""
        lab,butt, labb=self.encFile2()
        file = filedialog.askopenfilename(filetypes = (("Zip files","*.zip"),("all files","*.*")))
        self.lb= tk.Label(lab,text=file)
        self.lb.place(x=50, y=100)
        butt.config(state='active')
        labb.configure(text="Now click continue and then choose a file called\n '\'filename_\'key.zip' and hurray!.Your file is decrypted")
        return file
    
    
    def encFile2(self):  
        self.labelframe = tk.LabelFrame(self,width=400, height=300, text="Decrypt file", padx=10, pady=10)
        self.labelframe.place(x=0, y=0)
        self.resizable(width=False, height=False)
        self.label = tk.Label( self.labelframe,text="Browse a file called 'encrypted.zip' \nwhich contains the file to be decrypted", justify=tk.LEFT)
        self.label.place(x=10,y=0)
        self.btn = tk.Button(self.labelframe,text="Browse file", command=self.browse2)
        self.btn.place(x=40, y=70)
        self.lab=tk.Label(self.labelframe, text="")
        self.lab.place(x=10, y=120)
        
        self.butn=tk.Button(self.labelframe, text="Continue", state='disabled', command=self.decryptIt)
        self.butn.place(x=30, y=150)
        
        self.butc=tk.Button(self.labelframe, text="Cancel", command=self.confirm)
        self.butc.place(x=200, y=150)
        
    
        return (self.labelframe, self.butn, self.lab)
    
    def decryptIt(self):
        os.chdir("encrypted")
        with ZipFile(self.efile) as ef:
            ef.extractall()
        files=list(os.listdir())
        print(files)
        for i in files:
            if i.startswith('encrypted-'):
                encfile=i
        if not encfile.startswith('encrypted-'):
            tk.messagebox.showerror("File error", "Make sure the file to be decryped is prefixed with 'encrypted' ")
        content=open(encfile, 'rb')
        cont=content.read()
        content.close()
        
        ivf=open('iv.txt','r')
        iv=ivf.read()
        ivf.close()
        os.remove('iv.txt')
        os.remove(encfile)
        os.chdir("../")
        file = tk.filedialog.askopenfilename(filetypes = (("Zip files","*.zip"),("all files","*.*")))
        password=simpledialog.askstring("Input password", "Enter your password\n. Make sure your password is correct else youll have to begin the process again!!!", show="*")
        with ZipFile(file) as f:
            f.extractall(pwd=password.encode())

        keyname=file.split(".")[0]+".txt"
        if not keyname:
            messagebox.showerror("Key Error", "Please select the correct key. For this file select "+keyname)
            self.destroy()
        keytext=open(keyname, 'r')
        key=keytext.read()
        print(key)
        print(len(key))
        os.remove(keyname)        
        
        print(len(cont))       
        aes = AES.new(key, AES.MODE_CBC, iv)
        name=encfile.split("-")[-1]
        decd = aes.decrypt(cont)
        #encrypted= encd.decode('utf-16')
        allfiles=os.listdir()
        if "decrypted" not in allfiles:
            os.mkdir("decrypted")
        os.chdir("decrypted")
        outfile=open('decrypted-'+name, 'wb')#write bytes
        with outfile as f:
            f.write(decd)
        outfile.close()
        os.chdir("../")

        print("The key used is :{0} of length :{1}".format(key, len(key)))
        print(decd[:50])
        messagebox.showinfo("File decrypted!!!", "You can now find your decrypted file in\n "+os.path.abspath("decrypted/"+outfile.name))
        self.quit()
        #os.path.abspath give the absolute path of a file
    def confirm(self):
        con = messagebox.askokcancel('Confirm quit', 'Do you really want to quit cryptIt?')
        if con==True:
            exit()
        
