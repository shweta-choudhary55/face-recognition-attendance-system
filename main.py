from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from PIL import ImageDraw ,ImageFont
from student import student
import os
from face_recog import face_recognition
from train import Train
from attendence import attendence
from developer import developer
from help import help




class Face_Recognition_System:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System ")

        #first image background 
        img=Image.open(r"D:\AMS-FR\images\hello.jpg")
        img=img.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=790)


        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=350,y=0,width=1180,height=70)
        



        # second image logo 
        img1=Image.open(r"D:\AMS-FR\images\img2.png")
        img1=img1.resize((410,200),Image.Resampling.LANCZOS)
    
        
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=410,height=200)

        # student button 
        st_button=Image.open(r"D:\AMS-FR\images\stbutton.png")
        st_button=st_button.resize((130,130),Image.Resampling.LANCZOS)
    
        
        self.photoimg_st=ImageTk.PhotoImage(st_button)

        b1=Button(self.root,image=self.photoimg_st ,command=self.student_details, cursor="hand2")
        b1.place(x=100,y=250,width=130,height=130)


        b1_1=Button(self.root,text="STUDENT DETAILS " ,command=self.student_details, cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=100,y=380,width=130,height=40)

        # second button for detect face 

        dtf_button=Image.open(r"D:\AMS-FR\images\fdt.jpg")
        dtf_button=dtf_button.resize((130,130),Image.Resampling.LANCZOS)
    
        
        self.photoimg_st1=ImageTk.PhotoImage(dtf_button)

        b2=Button(self.root,image=self.photoimg_st1 ,command=self.face_data, cursor="hand2")
        b2.place(x=300,y=250,width=130,height=130)


        b2_1=Button(self.root,text="FACE DETECTOR " ,command=self.face_data, cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b2_1.place(x=300,y=380,width=130,height=40)


        # third button attendence face button 
        atf_button=Image.open(r"D:\AMS-FR\images\atbutton.png")
        atf_button=atf_button.resize((130,130),Image.Resampling.LANCZOS)
    
        
        self.photoimg_st2=ImageTk.PhotoImage(atf_button)

        b3=Button(self.root,image=self.photoimg_st2 ,command=self.att_data, cursor="hand2")
        b3.place(x=500,y=250,width=130,height=130)


        b3_1=Button(self.root,text="ATTENDANCE " ,command=self.att_data, cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b3_1.place(x=500,y=380,width=130,height=40)

        # help desk 
        hd_button=Image.open(r"D:\AMS-FR\images\hd2.webp")
        hd_button=hd_button.resize((130,130),Image.Resampling.LANCZOS)
    
        
        self.photoimg_st3=ImageTk.PhotoImage(hd_button)

        b4=Button(self.root,image=self.photoimg_st3 ,command=self.help_data, cursor="hand2")
        b4.place(x=700,y=250,width=130,height=130)


        b4_1=Button(self.root,text="HELP DESK" ,command=self.help_data, cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b4_1.place(x=700,y=380,width=130,height=40)


        # training dataset button
        td_button=Image.open(r"D:\AMS-FR\images\td.png")
        td_button=td_button.resize((130,130),Image.Resampling.LANCZOS)
    
        
        self.photoimg_st4=ImageTk.PhotoImage(td_button)

        b5=Button(self.root,image=self.photoimg_st4 ,command=self.train_data, cursor="hand2")
        b5.place(x=100,y=500,width=130,height=130)


        b5_1=Button(self.root,text="TRAIN DATA " ,command=self.train_data, cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b5_1.place(x=100,y=630,width=130,height=40)


        #photo face button 
        pf_button=Image.open(r"D:\AMS-FR\images\pd.jpg")
        pf_button=pf_button.resize((130,130),Image.Resampling.LANCZOS)
    
        
        self.photoimg_st5=ImageTk.PhotoImage(pf_button)

        b6=Button(self.root,image=self.photoimg_st5 , cursor="hand2",command=self.open_img)
        b6.place(x=300,y=500,width=130,height=130)


        b6_1=Button(self.root,text="PHOTOS" , cursor="hand2",command=self.open_img,font=("times new roman",10,"bold"),bg="black",fg="white")
        b6_1.place(x=300,y=630,width=130,height=40)

        # developer button
        dev_button=Image.open(r"D:\AMS-FR\images\dl.jpg")
        dev_button=dev_button.resize((130,130),Image.Resampling.LANCZOS)
    
        
        self.photoimg_st6=ImageTk.PhotoImage(dev_button)

        b7=Button(self.root,image=self.photoimg_st6 ,command=self.dev_data, cursor="hand2")
        b7.place(x=500,y=500,width=130,height=130)


        b7_1=Button(self.root,text="DEVELOPER" ,command=self.dev_data, cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b7_1.place(x=500,y=630,width=130,height=40)


         #exit face button 

        ex_button=Image.open(r"D:\AMS-FR\images\ex.png")
        ex_button=ex_button.resize((130,130),Image.Resampling.LANCZOS)
    
        
        self.photoimg_st7=ImageTk.PhotoImage(ex_button)

        b8=Button(self.root,image=self.photoimg_st7 , cursor="hand2")
        b8.place(x=700,y=500,width=130,height=130)


        b8_1=Button(self.root,text="EXIT " , cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b8_1.place(x=700,y=630,width=130,height=40)



    def open_img(self):
        os.startfile("data")
  
  #function button 

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)
    def att_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendence(self.new_window)

    def dev_data(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)

    




        








if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()