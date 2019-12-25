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


from cryptIt import Application as app
import cv2,os, string
import action, encryptit
from random import *
import Crypto
from Crypto.Cipher import AES
from io import BytesIO
import base64, pyperclip, subprocess
from zipfile import ZipFile

class Action(app):
    def __init__(self):
        
        app.__init__(self,'new')
##        self.Recognize= fcrec2.Recognize
        self.geometry('400x300')
        #self.configure(bg="#333")
        self.title('cryptIt')
##        self.var=self.calling()
        self.efile= self.browse()
        self.selected=tk.IntVar()
        self.selected.set(1)
       
        
        
            
        

        
    def camm(self):
        size = 4
        webcam = cv2.VideoCapture(0) #Use camera 0

        # We load the xml file
        classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        #  Above line normalTest
        #classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml') 
        #Above line test with different calulation
        #classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
        #classifier = cv2.CascadeClassifier('lbpcascade_frontalface.xml')


        while True:
            (rval, im) = webcam.read()
            im=cv2.flip(im,1,0) #Flip to act as a mirror

            # Resize the image to speed up detection
            mini = cv2.resize(im, (0, 0), fx=0.25, fy=0.25)

            # detect MultiScale / faces 
            faces = classifier.detectMultiScale(mini)
            for f in faces:
                (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
                cv2.rectangle(im, (x, y), (x + w, y + h),(0,255,0),thickness=4)
                #Save just the rectangle faces in SubRecFaces
                sub_face = im[y:y+h, x:x+w]
                FaceFileName = "Extracted/face_" + str(y) + ".jpg"
                cv2.imwrite(FaceFileName, sub_face)

            # Show the image
            cv2.imshow('Face found',   im)
            key=cv2.waitKey(10)
         # if Esc key is press then break out of the loop 
            if key == 27: #The Esc key
                break
            
        webcam.release()
        cv2.destroyAllWindows()
        self.calling()
       
    def calling(self):
        self.encryptIt(pyperclip.paste())
    
   
        
    def encryptIt(self, file):
        print(file)
        names=file.split("/")[-1]
        name=names.split(".")[0]
        file=self.convertText(file)
        fileObj=open(str(file),'rb')
        self.content= fileObj.read()
        fileObj.close()

        #cont=max-rem
        #realcont= self.content[:cont]
        max=len(self.content)
        print (max)
        images=list(os.listdir("Extracted"));
        print(images)
        import secrets
        image=secrets.choice(images)
        
        print(image)
        key= getImkey("Extracted/"+image)
        iv = self.getkey()
        out=open(name+'_key.txt', 'wb')
        with out as txt:
            txt.write(key)
        txt.close()
        rc = subprocess.call(['7z', 'a', name+'_key.zip', '-mx9', '-p'+self.password] + [name+'_key.txt'])
        os.remove(name+'_key.txt')
        size= AES.block_size
        aes = AES.new(key, AES.MODE_CBC, iv)
        data = self.content # <- 16 bytes
        contlen=len(data)
        rem = contlen%size
        if rem!=0:
            add=size-rem
            additional=''.join(choice(self.allchars) for x in range (add))
            data+=additional.encode()
        print(iv)
        print(len(data))
        encd = aes.encrypt(data)
        #encrypted= encd.decode('utf-16')
       
        allfiles=os.listdir()
        if "encrypted" not in allfiles:
            os.mkdir("encrypted")
        os.chdir("encrypted")
        outfile=open('encrypted-'+name+'.txt', 'wb')#write bytes
        with outfile as f:
            f.write(encd)
            
        outfile.close()
        ivfile =open('iv.txt','w')
        with ivfile as ivf:
            ivf.write(iv)
        ivf.close()
        an=subprocess.call(['7z', 'a', 'encrypted_'+name+'.zip','-mx9']+['encrypted-'+name+'.txt', 'iv.txt'])
        os.remove('encrypted-'+name+'.txt')
        os.remove('iv.txt')
        os.chdir("../")
        
        
        messagebox.showinfo("File encrypted successfully", "You can now find you encrypted file in "+ os.path.abspath("encrypted/encrypted_"+name+".zip"))

        print("The key used is :{0} of length :{1}".format(key, len(key)))
        print(len(encd))
        print(encd[:50])
        self.destroy()

        # bytes("hello", encoding="ascii")
        #b = mystring.encode()

            
        
    def encFile(self):  
        self.labelframe = tk.LabelFrame(self,width=400, height=300, text="Encrypt file", padx=10, pady=10)
        self.labelframe.place(x=0, y=0)
        self.resizable(width=False, height=False)
        self.label = tk.Label( self.labelframe,text="Choose the file to encrypt below\n. You can encrypt several types of files\n. This software allows you to encrypt file using passwords\n and keys", justify=tk.LEFT)
        self.label.place(x=10,y=0)
        self.btn = tk.Button(self.labelframe,text="Browse file", command=self.browse)
        self.btn.place(x=40, y=70)
        
        self.butn=tk.Button(self.labelframe, text="Continue", state='disabled')
        self.butn.place(x=30, y=140)
        
        
        self.butc=tk.Button(self.labelframe, text="Cancel", command=self.confirm)
        self.butc.place(x=200, y=140)
        
    
        return (self.labelframe, self.butn)
        
    
        return (self.labelframe, self.butn)
        
    def confirm(self):
        con = messagebox.askokcancel('Confirm quit', 'Do you really want to quit cryptIt?')
        if con==True:
            exit()
        
    def encryptFile(self):
        
        self.labelframe = tk.LabelFrame(self,width=400, height=200, text="Encrypt Here", padx=10, pady=10)
        self.labelframe.place(x=0, y=0)
        self.label = tk.Label( self.labelframe,text="Select algorithm")
        self.label.place(x=10,y=0)
        
        self.rad1=tk.Radiobutton(self.labelframe,text="AES", value=1, variable=self.selected)
        self.rad2=tk.Radiobutton(self.labelframe,text="DES", value=2, variable=self.selected)
        
    
        self.rad1.place(x=10, y=20)
        self.rad2.place(x=70, y=20)
        
        
        self.text=tk.Entry(self.labelframe, width=20)
        self.text.place(x=10, y=50)
        self.btn=tk.Button(self.labelframe, text="Next", command=self.camm)
        
        
        self.btn.place(x=10, y=80) 
        return self.text.get()
    
    def getkey(self):
        self.allchars= string.ascii_letters+string.punctuation+string.digits
        while True:
            key1=''.join(choice(self.allchars) for x in range (16))
            return key1
        
    def clicke(self):
        self.encryptFile()
        return self.encryptFile()
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
        
    
    def browse(self):
        file=""
        lab,butt=self.encFile()
        file = filedialog.askopenfilename(filetypes = (("all files","*.*"),("Text files","*.txt")))
        self.lb= tk.Label(lab,text=file)
        self.lb.place(x=50, y=100)
        self.password=""
        self.password2=""
        while self.password=="":
             self.password=simpledialog.askstring("Password enquiry","Please input the password to use in the process", show="*")
        while len(self.password)<8:
            tk.messagebox.showerror("Password alert", "Your password must be 8 or more characters")
            self.password=simpledialog.askstring("Password enquiry","Please input the password to use in the process", show="*")
        while self.password!=self.password2:
            self.password2=simpledialog.askstring("Password confirm","Please input you password again", show="*")
            tk.messagebox.showerror("Password error", "Your passwords do not match. Please try again")
            self.password2=simpledialog.askstring("Password confirm","Please input you password again", show="*")
            
        butt.config(state='active', command=self.encryptFile)
        pyperclip.copy(file)
        return file

    def convertText(self,file):
        extension=file.split(".")[-1]
        name=file.split(".")[0]
        if extension=="pdf":
            text=self.convert(file)
            textFileName=name+".txt"
            textFile= open(textFileName,"w")
            textFile.write(text)
            textFile.close()
            filename=textFile.name
            return filename
        else:
            filename1=file
            return filename1
        


def getImkey(image):
        with open(image, "rb") as img:
            str= base64.b64encode(img.read())
            key=choice([str[-16:], str[-32:], str[-24:]])
            return key
    