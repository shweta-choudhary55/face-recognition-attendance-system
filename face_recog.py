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
import face_recognition




class face_recognition:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system") 

        title_lbl=Label(self.root,text="FACE RECOGNITION ",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=70)

        imgbackg=Image.open(r"D:\AMS-FR\images\facere.webp")
        imgbackg=imgbackg.resize((1530,720),Image.Resampling.LANCZOS)
    
        
        self.photoimgbg=ImageTk.PhotoImage(imgbackg)

        f_lbl=Label(self.root,image=self.photoimgbg)
        f_lbl.place(x=0,y=70,width=1530,height=720)

        save_td=Button(self.root,text="FACE RECOGNITION ",cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_td.place(x=220,y=600,width=380,height=70)

        ##########attendence
        def mark_att(self,sid,r,i,d):
            with open("shweta.csv","r+",newline="\n") as f:
                my_datalist=f.readlines()
                name_list=[]

                for line in my_datalist:
                    entry = line.split((","))
                    name_list.append(entry[0])
                if ((sid not in name_list)and (r not in name_list) and (i not in name_list)and ( d not in name_list)):
                    now= datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString= now.strftime("%H:%M:%S")
                    f.writelines(f"\n{sid},{r},{i},{d},{dtString},{d1},present")






    
    def refa(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):

            gray_image=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="qwertyuioP1@",database="face_attendence")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student_database where id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select roll from student_database where id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Department from student_database where id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select id from student_database where id="+str(id))
                sid=my_cursor.fetchone()
                sid="+".join(sid)



                if confidence >77:
                    cv2.putText(img,f"id:{sid}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    self.mark_att(sid,r,i,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
                    
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord[x,y,w,h]
            return coord
        def recognise(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)

        while True:
            ret ,img=video_cap.read()
            img=recognise(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()



            
            






if __name__=="__main__":
    root=Tk()
    obj=face_recognition(root)
    root.mainloop()





