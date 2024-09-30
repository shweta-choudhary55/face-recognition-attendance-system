from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from PIL import ImageDraw ,ImageFont
from tkinter import messagebox
import mysql

import mysql.connector
import cv2




class student:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("student ")

        ######variables 
        self.var_Department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        



        #first image background 
        img=Image.open(r"D:\AMS-FR\images\hello.jpg")
        img=img.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=790)


        title_lbl=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=350,y=0,width=1180,height=70)
        



        # second image logo 
        img1=Image.open(r"D:\AMS-FR\images\img2.png")
        img1=img1.resize((410,200),Image.Resampling.LANCZOS)
    
        
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=410,height=200)


#       MAIN FRAME 

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=20,y=230,width=1490,height=530)

        # left label frame 
        Left_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=780,height=500 )


        # #LEFT FRAME IMAGE 
        imgleft=Image.open(r"D:\AMS-FR\images\lft.jpg")
        imgleft=imgleft.resize((775,475),Image.Resampling.LANCZOS)
    
        
        self.photoimglt=ImageTk.PhotoImage(imgleft)

        f_lbl=Label(Left_frame,image=self.photoimglt)
        f_lbl.place(x=0,y=0,width=775,height=475)

#       current course  TITLE 

        title_lbl=Label(Left_frame,text="CURRENT COURSE DETAILS",font=("times new roman",15,"bold"),bg="antiquewhite",fg="black")
        title_lbl.place(x=0,y=0,width=775,height=30)

   # CURRENT COURSE LABEL
        CU_frame=LabelFrame(Left_frame,bd=2, bg="white", relief=RIDGE,text="Course Information",font=("times new roman",12,"bold"))
        CU_frame.place(x=0,y=30,width=775,height=120 )

        #department  label  and combobox

        dep_label=Label(CU_frame,text='Department',font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

#       
        dep_combo=ttk.Combobox(CU_frame,textvariable=self.var_Department,font=("times new roman",12,"bold"),state= 'readonly',width=16)
        dep_combo['values']=("Select Department",'Computer Science',"IT",'Civil En.',"Mechanical En.","Electrical En")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
                       

        #courses 
        course_label=Label(CU_frame,text='Course',font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

#       
        course_combo=ttk.Combobox(CU_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state= 'readonly',width=16)
        course_combo['values']=("Select Course",'FE',"SE",'TE',"TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year 

        year_label=Label(CU_frame,text='Year',font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

#       
        year_combo=ttk.Combobox(CU_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state= 'readonly',width=16)
        year_combo['values']=("Select Year",'2018-19',"2019-20",'2020-21',"2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # semester 

        sem_label=Label(CU_frame,text='semester',font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

#       
        sem_combo=ttk.Combobox(CU_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state= 'readonly',width=16)
        sem_combo['values']=("Select Semester",'Semester-1',"Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

#     class student information
        Cs_frame=LabelFrame(Left_frame,bd=2, bg="white", relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Cs_frame.place(x=0,y=150,width=775,height=300 )
       # student id 
        sid_label=Label(Cs_frame,text='Student ID',font=("times new roman",12,"bold"),bg="white")
        sid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_ent=ttk.Entry(Cs_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentid_ent.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name 

        snm_label=Label(Cs_frame,text='Student Name ',font=("times new roman",12,"bold"),bg="white")
        snm_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentnm_ent=ttk.Entry(Cs_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentnm_ent.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division 
        cd_label=Label(Cs_frame,text='Class Division ',font=("times new roman",12,"bold"),bg="white")
        cd_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # studentcd_ent=ttk.Entry(Cs_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # studentcd_ent.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(Cs_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state= 'readonly',width=18)
        div_combo['values']=("A",'B',"C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll number 
        rn_label=Label(Cs_frame,text='Roll Number  ',font=("times new roman",12,"bold"),bg="white")
        rn_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentrn_ent=ttk.Entry(Cs_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        studentrn_ent.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gd_label=Label(Cs_frame,text='Gender ',font=("times new roman",12,"bold"),bg="white")
        gd_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        # studentgd_ent=ttk.Entry(Cs_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # studentgd_ent.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        gen_combo=ttk.Combobox(Cs_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state= 'readonly',width=18)
        gen_combo['values']=("Select gender",'MALE',"FEMALE","OTHER")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(Cs_frame,text='DOB ',font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentdb_ent=ttk.Entry(Cs_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        studentdb_ent.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        em_label=Label(Cs_frame,text='Email ',font=("times new roman",12,"bold"),bg="white")
        em_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentem_ent=ttk.Entry(Cs_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        studentem_ent.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone number 
        pn_label=Label(Cs_frame,text='Phone Number',font=("times new roman",12,"bold"),bg="white")
        pn_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentpn_ent=ttk.Entry(Cs_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        studentpn_ent.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        ad_label=Label(Cs_frame,text='Address ',font=("times new roman",12,"bold"),bg="white")
        ad_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentcd_ent=ttk.Entry(Cs_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        studentcd_ent.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name   


        tn_label=Label(Cs_frame,text='Teacher Name  ',font=("times new roman",12,"bold"),bg="white")
        tn_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        studenttn_ent=ttk.Entry(Cs_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        studenttn_ent.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()



        

        radiobutt1=ttk.Radiobutton(Cs_frame,width=20,variable=self.var_radio1, text="Take Photo Sample",value="Yes" )
        radiobutt1.grid(row=5,column=0)


        #photo sample 
        
        radiobutt2=ttk.Radiobutton(Cs_frame,width=20,variable=self.var_radio1,text="No Photo Sample",value="No" )
        radiobutt2.grid(row=5,column=1)


        #button frame 
        btn_frame=Frame(Cs_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=770,height=36)

        #save button 

        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width= 20,font=("times new roman",12,"bold"),bg="white",fg="black")
        save_btn.grid(row=0,column=0)

        # update button 
        up_btn=Button(btn_frame,text="UPDATE",width= 20,command=self.update_data,font=("times new roman",12,"bold"),bg="white",fg="black")
        up_btn.grid(row=0,column=1)

        # delet button 
        del_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width= 20,font=("times new roman",12,"bold"),bg="white",fg="black")
        del_btn.grid(row=0,column=2)

        #reset button 
        re_btn=Button(btn_frame,text="RESET",command=self.reset_data,width= 21,font=("times new roman",12,"bold"),bg="white",fg="black")
        re_btn.grid(row=0,column=3)

        # #TAKE PHOTO SAMPLE  frame 

        ft_frame=Frame(Cs_frame,bd=2,relief=RIDGE,bg="white")
        ft_frame.place(x=0,y=236,width=770,height=36)

        tkp_btn=Button(ft_frame,command=self.generate_dataset,text="Take Photo Sample",width= 41,font=("times new roman",12,"bold"),bg="white",fg="black")
        tkp_btn.grid(row=0,column=0)

        # #update photo sample 
        upp_btn=Button(ft_frame,text="Update Photo Sample ",width=42,font=("times new roman",12,"bold"),bg="white",fg="black")
                       
        upp_btn.grid(row=0,column=1)


 
 #right label frame 

        rt_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        rt_frame.place(x=800,y=10,width=670,height=500 )


        #back ground image 
        imgrt=Image.open(r"D:\AMS-FR\images\lft.jpg")
        imgrt=imgrt.resize((665,474),Image.Resampling.LANCZOS)
    
        
        self.photoimgrt=ImageTk.PhotoImage(imgrt)

        f_lbl=Label(rt_frame,image=self.photoimgrt)
        f_lbl.place(x=0,y=0,width=665,height=474)

#       data base details   TITLE 

        db_lbl=Label(rt_frame,text="DATABASE INFORMATION ",font=("times new roman",15,"bold"),bg="antiquewhite",fg="black")
        db_lbl.place(x=0,y=0,width=665,height=30)

        #search frame 
        
        search_frame=LabelFrame(rt_frame,bd=2, bg="white", relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=0,y=30,width=665,height=70)

        #search label
        search_label=Label(search_frame,text='Search By:',font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state= 'readonly',width=12)
        search_combo['values']=("Select ",'Roll_No',"Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=12,sticky=W)


        search_ent=ttk.Entry(search_frame,width=15,font=("times new roman",14,"bold"))
        search_ent.grid(row=0,column=2,padx=10,pady=5,sticky=W)


         
        #search button
        ser_btn=Button(search_frame,text="Search",width=12 ,font=("times new roman",12,"bold"),bg="white",fg="black")
        ser_btn.grid(row=0,column=3,padx=2)

        #show button
        show_btn=Button(search_frame,text="Show All",width=12 ,font=("times new roman",12,"bold"),bg="white",fg="black")
        show_btn.grid(row=0,column=4)

        #table  frame 
        table_frame=LabelFrame(rt_frame,bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=0,y=100,width=665,height=350)

        #scroll bar in table frame 
        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","ID","Name","Division","Roll No","Gender","DOB","Email","Phone Number","Address","Teacher","Photo"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone Number",text="Phone Number")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone Number",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


     #function declaration 
    def add_data(self):
        if self.var_Department.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="qwertyuioP1@",database="face_attendence")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_database values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_Department.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_id.get(),
                                                                                                                        self.var_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get()
                                                                                                                        
                                                                                                                        ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

########data fetch
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="qwertyuioP1@",database="face_attendence")
        my_cursor=conn.cursor()
        my_cursor.execute("select* from student_database")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
            
###########get cursor/updating the fetched  data 
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Department.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
######update function 
    def update_data(self):
        if self.var_Department.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                update=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="qwertyuioP1@",database="face_attendence")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student_database set Department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where id=%s",(

                                                                                                                                                                                self.var_Department.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                
                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_id.get()
                                                                                                                                                                                ))
                else:
                    if not update :
                        return
                messagebox.showinfo("success","student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        
                    
##########DELET function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student detail page ","do you want to delet this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="qwertyuioP1@",database="face_attendence")
                    my_cursor=conn.cursor()
                    sql="delete from student_database where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:

            
                messagebox.showinfo("delete","successfully deleted student details ",parent=self.root)


    #####reset data 
    def reset_data(self):
        self.var_Department.set("Select DEPARTMENT ")
        self.var_course.set("Select Course ")
        self.var_year.set("Select year ")
        self.var_semester.set("Select semester ")
        self.var_id.set(" ")
        self.var_name.set(" ")
        self.var_div.set("Select Division ")
        self.var_roll.set("")
        self.var_gender.set("Select Gender ")
        self.var_dob.set("")
        self.var_email.set(" ")
        self.var_phone.set(" ")
        self.var_address.set(" ")
        self.var_teacher.set("")
        self.var_radio1.set(" ")
        
 #######generate data set or take photo samples 
    def generate_dataset(self):
        if self.var_Department.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
        
            
            

            try:
                conn = mysql.connector.connect(
                                                    host="localhost",
                                                    username="root",
                                                    password="qwertyuioP1@",
                                                    database="face_attendence"
                                                )
                my_cursor = conn.cursor()

                # Fetch all records to determine the current maximum id (if needed)
                my_cursor.execute("SELECT * FROM student_database")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1  # Corrected the increment

                # Update the student record where id matches
                my_cursor.execute("UPDATE student_database SET Department=%s, course=%s, year=%s, semester=%s, name=%s, division=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s WHERE id=%s",(
                    
                                                                                                                                                                                                                            self.var_Department.get(),
                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                            self.var_id.get()  # Use self.var_id.get() if it refers to the correct ID
                                                                                                                                                                                                                        )
                                                                                                                                                                                                                    )

                conn.commit()  # Commit the changes to the database
                self.fetch_data()  # Fetch updated data
                self.reset_data()  # Reset form data
                conn.close()  # Close the connection

            except Exception as es:
                
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


                ######load predefined data on face facefrontal from open cv 
    

# Initialize the face classifier

                face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5 )
                    
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                # Start video capture
                cap = cv2.VideoCapture(0)

                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = f"data/user."+str(id)+"."+str(img_id)+".jpg"
                        
                        
                    cv2.imwrite(file_name_path)
                        
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                    
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                # Release the video capture object and close windows
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")


                                

                                                    


                    
                    


                    

                    









if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()