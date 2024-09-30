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
import csv
from tkinter import filedialog



mydata=[]
class attendence:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendence  system")

        ####variables
        
        self.var_att_id=StringVar()
        self.var_att_roll=StringVar()
        self.var_att_name=StringVar()
        self.var_att_dep=StringVar()
        self.var_att_time=StringVar()
        self.var_att_date=StringVar()
        self.var_att_status=StringVar()



        img=Image.open(r"D:\AMS-FR\images\hello.jpg")
        img=img.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(self.root,text=" ATTENDENCE  MANAGEMENT  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=350,y=0,width=1180,height=70)
        



        # second image logo 
        img1=Image.open(r"D:\AMS-FR\images\img2.png")
        img1=img1.resize((410,200),Image.Resampling.LANCZOS)
    
        
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=410,height=200)


        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=20,y=230,width=1490,height=530)


        Left_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE,text="Student Attendence  Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=780,height=500 )


        # #LEFT FRAME IMAGE 
        imgleft=Image.open(r"D:\AMS-FR\images\lft.jpg")
        imgleft=imgleft.resize((775,475),Image.Resampling.LANCZOS)
    
        
        self.photoimglt=ImageTk.PhotoImage(imgleft)

        f_lbl=Label(Left_frame,image=self.photoimglt)
        f_lbl.place(x=0,y=0,width=775,height=475)
        ####left inside 
        lt_frame=LabelFrame(Left_frame,bd=2, bg="white", relief=RIDGE,font=("times new roman",12,"bold"))
        lt_frame.place(x=0,y=0,width=775,height=200 )

        #label and entry 
        ###attendence id 
        att_id_label=Label(lt_frame,text='Attendence ID ',font=("times new roman",12,"bold"),bg="white")
        att_id_label.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        att_id_ent=ttk.Entry(lt_frame,textvariable=self.var_att_id,width=24,font=("times new roman",12,"bold"))
        att_id_ent.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        ##roll no
        r_id_label=Label(lt_frame,text='Roll No ',font=("times new roman",12,"bold"),bg="white")
        r_id_label.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        r_id_ent=ttk.Entry(lt_frame,textvariable=self.var_att_roll,width=24,font=("times new roman",12,"bold"))
        r_id_ent.grid(row=0,column=4,padx=10,pady=5,sticky=W)

        ###name
        name_id_label=Label(lt_frame,text='Student Name ',font=("times new roman",12,"bold"),bg="white")
        name_id_label.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        name_id_ent=ttk.Entry(lt_frame,width=24,textvariable=self.var_att_name,font=("times new roman",12,"bold"))
        name_id_ent.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        #department
        dep_id_label=Label(lt_frame,text='Department ',font=("times new roman",12,"bold"),bg="white")
        dep_id_label.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        dep_id_ent=ttk.Entry(lt_frame,width=24,textvariable=self.var_att_dep,font=("times new roman",12,"bold"))
        dep_id_ent.grid(row=1,column=4,padx=10,pady=5,sticky=W)

        ######time 
        t_id_label=Label(lt_frame,text='Time ',font=("times new roman",12,"bold"),bg="white")
        t_id_label.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        t_id_ent=ttk.Entry(lt_frame,width=24,textvariable=self.var_att_time,font=("times new roman",12,"bold"))
        t_id_ent.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        ##date
        date_id_label=Label(lt_frame,text='Date ',font=("times new roman",12,"bold"),bg="white")
        date_id_label.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        date_id_ent=ttk.Entry(lt_frame,width=24,textvariable=self.var_att_date,font=("times new roman",12,"bold"))
        date_id_ent.grid(row=2,column=4,padx=10,pady=5,sticky=W)

        ##attendence status 
        atte_id_label=Label(lt_frame,text='Attendence Status ',font=("times new roman",12,"bold"),bg="white")
        atte_id_label.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        att_combo=ttk.Combobox(lt_frame,font=("times new roman",12,"bold"),textvariable=self.var_att_status,state= 'readonly',width=24)
        att_combo['values']=("Status",'PRESENT',"ABSENT")
        att_combo.current(0)
        att_combo.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        ###buttons 

        #button frame 
        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=775,height=36)

        #save button 

        save_btn=Button(btn_frame,text="Import csv",command=self.import_csv,width= 20,font=("times new roman",12,"bold"),bg="white",fg="black")
        save_btn.grid(row=0,column=0)

        # update button 
        up_btn=Button(btn_frame,text="Export csv", command=self.export_csv,width= 20,font=("times new roman",12,"bold"),bg="white",fg="black")
        up_btn.grid(row=0,column=1)

        # delet button 
        del_btn=Button(btn_frame,text="UPDATE",width= 20,font=("times new roman",12,"bold"),bg="white",fg="black")
        del_btn.grid(row=0,column=2)

        #reset button 
        re_btn=Button(btn_frame,text="RESET",command=self.reset_data,width= 21,font=("times new roman",12,"bold"),bg="white",fg="black")
        re_btn.grid(row=0,column=3)






        ####right frame 

        rt_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        rt_frame.place(x=800,y=10,width=670,height=500 )


        #back ground image 
        imgrt=Image.open(r"D:\AMS-FR\images\lft.jpg")
        imgrt=imgrt.resize((665,474),Image.Resampling.LANCZOS)
    
        
        self.photoimgrt=ImageTk.PhotoImage(imgrt)

        f_lbl=Label(rt_frame,image=self.photoimgrt)
        f_lbl.place(x=0,y=0,width=665,height=474)


        table_frame=Frame(rt_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=0,width=665,height=450)

        ####scroll bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll no","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
        self.AttendenceReportTable.heading("id",text="Attendence id")
        self.AttendenceReportTable.heading("roll no",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll no",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)


        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

#####fetch data 
    def fetchdata(self,row):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in row :
            self.AttendenceReportTable.insert("",END,values=i)
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv") , ("ALL file","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

####export csv 
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export ",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv") , ("ALL file","*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+ "successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root) 
        

    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_att_id.set(rows[0])
        self.var_att_roll.set(rows[1])
        self.var_att_name.set(rows[2])
        self.var_att_dep.set(rows[3])
        self.var_att_time.set(rows[4])
        self.var_att_date.set(rows[5])
        self.var_att_status.set(rows[6])


    def reset_data(self):
        self.var_att_id.set("")
        self.var_att_roll.set("")
        self.var_att_name.set("")
        self.var_att_dep.set("")
        self.var_att_time.set("")
        self.var_att_date.set("")
        self.var_att_status.set("")
        






if __name__=="__main__":
    root=Tk()
    obj=attendence(root)
    root.mainloop()
