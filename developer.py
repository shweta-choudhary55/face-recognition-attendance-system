from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from PIL import ImageDraw ,ImageFont
from tkinter import messagebox
import mysql
from time import strftime
from datetime import datetime

import mysql.connector
import cv2
import os
import numpy as np




class developer:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system") 


        title_lbl=Label(self.root,text="DEVELOPER ",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=70)

        imgbackg=Image.open(r"D:\AMS-FR\images\dev.webp")
        imgbackg=imgbackg.resize((1530,720),Image.Resampling.LANCZOS)
    
        
        self.photoimgbg=ImageTk.PhotoImage(imgbackg)

        f_lbl=Label(self.root,image=self.photoimgbg)
        f_lbl.place(x=0,y=70,width=1530,height=720)

        d_frame=LabelFrame(self.root,bd=2, bg="white", relief=RIDGE,font=("times new roman",12,"bold"))
        d_frame.place(x=1000,y=75,width=500,height=500 )

        imgbackg1=Image.open(r"D:\AMS-FR\images\pic2.jpg")
        imgbackg1=imgbackg1.resize((500,500),Image.Resampling.LANCZOS)
    
        
        self.photoimgbg1=ImageTk.PhotoImage(imgbackg1)
        f_lbl=Label(d_frame,image=self.photoimgbg1)
        f_lbl.place(x=0,y=0,width=500,height=500)

        title_lbl=Label(d_frame,text= "Hello my name is Shweta Choudhary",font=("times new roman",15,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=5)
        title_lbl=Label(d_frame,text= "I am a full stack developer",font=("times new roman",15,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=40)











if __name__=="__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()