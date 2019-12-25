from action import Action as act
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from PIL import Image, ImageTk, ImageDraw
from tkinter import filedialog
from tkinter import messagebox
import os
from subprocess import Popen, PIPE
import fcrec2
import random
import numpy as np
from io import StringIO, BytesIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import sys, getopt
import cv2,os, string
import action, encryptit
from random import *
import Crypto
from Crypto.Cipher import AES
from io import BytesIO
import base64, pyperclip
class Decrypt(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('400x300')
        self.title('cryptIt')
        self.values=[]
        self.efile=self.browse2()
    
     
    def browse2(self):
        file=""
        lab,butt=self.encFile2()
        file = filedialog.askopenfilename(filetypes = (("all files","*.*"),("Text files","*.txt")))
        self.lb= tk.Label(lab,text=file)
        self.lb.place(x=50, y=100)
        butt.config(state='active')
        pyperclip.copy(file)
        return file
    
    
    def encFile2(self):  
        self.labelframe = tk.LabelFrame(self,width=400, height=300, text="Encrypt file", padx=10, pady=10)
        self.labelframe.place(x=0, y=0)
        self.label = tk.Label( self.labelframe,text="Choose the file to decrypt below\n. You can decrypt several types of files\n. This software allows you to decrypt file using passwords\n and keys", justify=tk.LEFT)
        self.label.place(x=10,y=0)
        self.btn = tk.Button(self.labelframe,text="Browse file", command=self.browse2)
        self.btn.place(x=40, y=70)
        
        self.butn=tk.Button(self.labelframe, text="Continue", state='disabled', command=self.decryptIt)
        self.butn.place(x=30, y=140)
        
        self.butc=tk.Button(self.labelframe, text="Cancel", command=self.confirm)
        self.butc.place(x=200, y=140)
        
    
        return (self.labelframe, self.butn)
    
    def decryptIt(self):
        content=open(self.efile, 'rb')
        with content as cont:
            cont1=cont.read()
        content.close()
        key = b'cne8l0ta+p//2Q==' 
        iv = b'hello world 1234'
        aes = AES.new(key, AES.MODE_CBC, iv)
        ##data = content.encode() # <- 16 bytes


        decd = aes.decrypt(cont1)
        #encrypted= encd.decode('utf-16')
        outfile=open('outt.txt', 'wb')#write bytes
        with outfile as f:
            f.write(decd)
        outfile.close()

        print("The key used is :{0} of length :{1}".format(key, len(key)))
        print(decd[:50])
        
        self.destroy()
    def confirm(self):
        con = messagebox.askokcancel('Confirm quit', 'Do you really want to quit cryptIt?')
        if con==True:
            exit()
        
