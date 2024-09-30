from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from PIL import ImageDraw ,ImageFont
from tkinter import messagebox
import mysql

import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("train dataset") 


        title_lbl=Label(self.root,text="TRAIN DATASET ",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=70)

        imgbackg=Image.open(r"D:\AMS-FR\images\dataset.webp")
        imgbackg=imgbackg.resize((1530,720),Image.Resampling.LANCZOS)
    
        
        self.photoimgbg=ImageTk.PhotoImage(imgbackg)

        f_lbl=Label(self.root,image=self.photoimgbg)
        f_lbl.place(x=0,y=70,width=1530,height=720)

        save_td=Button(self.root,text="TRAIN DATA",command=self.t_cfr,cursor="hand2",font=("times new roman",12,"bold"),bg="white",fg="black")
        save_td.place(x=0,y=77,width=1530,height=70)

    def t_cfr(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")# gray scale 
            imageNp=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split(".")[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        ######train classifier and save 

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed")






        


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()