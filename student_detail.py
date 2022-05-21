from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student_detail():
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x710+0+0')
        self.root.title('Students Details')

        #-----------------variable--------------
        self.var_dept=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_course=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll_no=StringVar()
        self.var_sec=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phn=StringVar()
        self.var_email=StringVar()
        self.var_add=StringVar()
        self.var_teacher=StringVar()
        self.var_pic_sts=StringVar()




        #------------label 1 student image 1------------------
        img1=Image.open(r"C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\student_detail_label1.jpg")
        img1=img1.resize((500,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        label1_img=Label(root,image=self.photoimage1)
        label1_img.place(x=0,y=0,width=500,height=100)

        #------------label 2 student image 2------------------

        img2 = Image.open(r"C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\student_detail_label2.jpg")
        img2 = img2.resize((500, 100), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        label2_img = Label(root, image=self.photoimage2)
        label2_img.place(x=500, y=0, width=500, height=100)

        #------------label 3 student image 3----------------

        img3 = Image.open(r"C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\student_detail_label3.jpg")
        img3 = img3.resize((500, 100), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        label3_img = Label(root, image=self.photoimage3)
        label3_img.place(x=1000, y=0, width=500, height=100)

        #--------------background image-----------------

        img4 = Image.open(r"C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\bg.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        bg_img = Label(root, image=self.photoimage4)
        bg_img.place(x=0, y=100, width=1530, height=710)

        #--------------------title-------------------

        project_ttl = Label(bg_img, text='Student Details', font=('times new roman', 35, 'bold'),fg='red')
        project_ttl.place(x=0, y=0, width=1530, height=45)

        #------------------mainframe------------------

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=50,width=1330,height=600)

            #--------------Left label frame------------

        left_label=LabelFrame(main_frame,text='Student Details',bd=2,relief=RIDGE,font=('times new roman',15,'bold'))
        left_label.place(x=10,y=10,width=730,height=640)

                #-----------image--------------------

        img5=Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\logo.jpg')
        img5=img5.resize((730,100),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(img5)

        left_lbl_img=Label(left_label,image=self.photoimage5)
        left_lbl_img.place(x=0,y=0,width=720,height=100)

                #----------currunt course info---------

        curr_course=LabelFrame(left_label,bd=2,text='Currunt Course Information',relief=RIDGE,font=('times new roman',15,'bold'))
        curr_course.place(x=10,y=100,width=710,height=120)

                    #------------department--------------

        dept=Label(curr_course,text='Department',font=('times new roman',15,'bold'))
        dept.grid(row=0,column=0,padx=5,pady=5)

        dept_combo=ttk.Combobox(curr_course,font=('times new roman',14),textvariable=self.var_dept,state='readonly')
        dept_combo['values']=['Select the department','CSE','IT','Mechanical','Civil','ECE','EE']
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=5,pady=5)

                    #------------course----------------------

        course = Label(curr_course, text='Course', font=('times new roman', 15, 'bold'))
        course.grid(row=0, column=2, padx=5,pady=5)

        course_combo = ttk.Combobox(curr_course, font=('times new roman', 14),textvariable=self.var_course, state='readonly')
        course_combo['values'] = ['Select the course', 'B.tech', 'BE', 'B.sc', 'MBA', 'BBA', 'M.sc']
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=5,sticky=W)

                    #----------year-----------------------

        year = Label(curr_course, text='Years', font=('times new roman', 15, 'bold'))
        year.grid(row=1, column=0, padx=5,pady=5)

        year_combo = ttk.Combobox(curr_course, font=('times new roman', 14), textvariable=self.var_year,state='readonly')
        year_combo['values'] = ['Select the year', '2021-2022', '2020-2021', '2019-2020', '2018-2019', '2017-2018', '2016-2017','2015-2016','2014-2015']
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=5,sticky=W)

                    #-----------semester--------------------

        sem = Label(curr_course, text='Semester', font=('times new roman', 15, 'bold'))
        sem.grid(row=1, column=2, padx=5,pady=5)

        sem_combo = ttk.Combobox(curr_course, font=('times new roman', 14), textvariable=self.var_sem,state='readonly')
        sem_combo['values'] = ['Select the semester','1','2','3','4','5','6','7','8']
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=5, pady=5)


                #--------------class student information--------
        class_info = LabelFrame(left_label, bd=2, text='Class Student Information', relief=RIDGE,
                                 font=('times new roman', 15, 'bold'))
        class_info.place(x=10, y=220, width=710, height=240)

                    #-----------student id---------------------

        student_id= Label(class_info, text='Student ID', font=('times new roman', 15, 'bold'))
        student_id.grid(row=0, column=0, padx=5)

        student_id_entry=ttk.Entry(class_info,font=('times new roman', 15, 'bold'),textvariable=self.var_id)
        student_id_entry.grid(row=0,column=1,padx=5,pady=5)

                    #----------student name-------------------

        student_name = Label(class_info, text='Student Name', font=('times new roman', 15, 'bold'))
        student_name.grid(row=0, column=2, padx=5,pady=5)

        student_name_entry = ttk.Entry(class_info, font=('times new roman', 15, 'bold'),textvariable=self.var_name)
        student_name_entry.grid(row=0, column=3, padx=5, pady=5)

                    #------------section----------------------

        student_section = Label(class_info, text='Section', font=('times new roman', 15, 'bold'))
        student_section.grid(row=1, column=0, padx=5,pady=5)

        student_section_entry = ttk.Combobox(class_info, font=('times new roman', 14), state='readonly', textvariable=self.var_sec)
        student_section_entry['values'] = ['Select section', 'A', 'B','C']
        student_section_entry.current(0)
        student_section_entry.grid(row=1, column=1, padx=5, pady=5)

                    #-------------roll no-------------------

        roll_no = Label(class_info, text='Roll No.', font=('times new roman', 15, 'bold'))
        roll_no.grid(row=1, column=2, padx=5,pady=5)

        roll_no_entry = ttk.Entry(class_info, font=('times new roman', 15, 'bold'),textvariable=self.var_roll_no)
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5)

                    #------------gender--------------------

        gender = Label(class_info, text='Gender', font=('times new roman', 15, 'bold'))
        gender.grid(row=2, column=0)

        gender = ttk.Combobox(class_info, font=('times new roman', 14),state='readonly',textvariable=self.var_gender)
        gender['values']=['Select gender','Male','Female']
        gender.current(0)
        gender.grid(row=2, column=1,padx=5,pady=5)

                    #------------DOB----------------------

        dob = Label(class_info, text='DOB.', font=('times new roman', 15, 'bold'))
        dob.grid(row=2, column=2, padx=5,pady=5)

        dob_entry = ttk.Entry(class_info, font=('times new roman', 15, 'bold'),textvariable=self.var_dob)
        dob_entry.grid(row=2, column=3, padx=5, pady=5)

                    #-----------phone no------------------

        phn_no = Label(class_info, text='Phone No.', font=('times new roman', 15, 'bold'))
        phn_no.grid(row=3, column=0, padx=5,pady=5)

        phn_no_entry = ttk.Entry(class_info, font=('times new roman', 15, 'bold'),textvariable=self.var_phn)
        phn_no_entry.grid(row=3, column=1, padx=5, pady=10)

                    #-------------Email---------------------

        email = Label(class_info, text='Email ID.', font=('times new roman', 15, 'bold'))
        email.grid(row=3, column=2, padx=5,pady=5)

        email_entry = ttk.Entry(class_info, font=('times new roman', 15, 'bold'),textvariable=self.var_email)
        email_entry.grid(row=3, column=3, padx=5, pady=5)

                    #----------address-----------------------

        student_add = Label(class_info, text='Address', font=('times new roman', 15, 'bold'))
        student_add.grid(row=4, column=0, padx=5,pady=5)

        student_add_entry = ttk.Entry(class_info, font=('times new roman', 15, 'bold'),textvariable=self.var_add)
        student_add_entry.grid(row=4, column=1, padx=5, pady=5)

                    #---------------teacher-------------------

        teacher = Label(class_info, text='Teacher Name.', font=('times new roman', 15, 'bold'))
        teacher.grid(row=4, column=2, padx=5,pady=5)

        teacher_entry = ttk.Entry(class_info, font=('times new roman', 15, 'bold'),textvariable=self.var_teacher)
        teacher_entry.grid(row=4, column=3, padx=5, pady=5)

        #------------------button frame---------------------

        btn_frm=LabelFrame(left_label,relief=RIDGE)
        btn_frm.place(x=10,y=465,width=710,height=100)

        #save btn
        save_btn=Button(btn_frm,text='Save',cursor='hand2',bg='dark blue',fg='white',
                        font=('times new roman',15,'bold'),width=14,command=self.add_data)
        save_btn.grid(row=0,column=0)
        #delete btn
        dlt_btn = Button(btn_frm, text='Delete', cursor='hand2', bg='dark blue', command=self.delete_data,fg='white',
                          font=('times new roman', 15, 'bold'), width=14)
        dlt_btn.grid(row=0, column=1)
        #update btn
        update_btn = Button(btn_frm, text='Update',command=self.update_data, cursor='hand2', bg='dark blue', fg='white',
                          font=('times new roman', 15, 'bold'), width=14)
        update_btn.grid(row=0, column=2)
        #reset btn
        reset_btn = Button(btn_frm, command=self.reset_data,text='Reset', cursor='hand2', bg='dark blue', fg='white',
                          font=('times new roman', 15, 'bold'), width=14)
        reset_btn.grid(row=0, column=3)

        #take image
        take_btn = Button(btn_frm,command=self.generated_dataset, text='Take Image', cursor='hand2', bg='dark blue', fg='white',
                          font=('times new roman', 15, 'bold'), width=14)
        take_btn.grid(row=1, column=0)

        # #update image
        # update_btn_img = Button(btn_frm, text='Update Image', cursor='hand2', bg='dark blue', fg='white',
        #                   font=('times new roman', 15, 'bold'), width=14)
        # update_btn_img.grid(row=1, column=1)

        #radio button
        radio_btn1=ttk.Radiobutton(btn_frm,text='Take image sample',value='Yes',variable=self.var_pic_sts)
        radio_btn1.grid(row=1,column=2)

        radio_btn2 = ttk.Radiobutton(btn_frm, text='No image sampling',value='No',variable=self.var_pic_sts)
        radio_btn2.grid(row=1, column=3)
        #-------------Right label frame-------------

        right_label = LabelFrame(main_frame,text='Student Details' ,bd=2, relief=RIDGE,font=('times new roman',15,'bold'))
        right_label.place(x=750, y=10, width=560, height=640)

        img6 = Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\logo.jpg')
        img6 = img6.resize((550, 100), Image.ANTIALIAS)
        self.photoimage6 = ImageTk.PhotoImage(img6)

        right_lbl_img = Label(right_label, image=self.photoimage6)
        right_lbl_img.place(x=0, y=0, width=550, height=100)

        #search frame
        search_frm = LabelFrame(right_label, bd=2, relief=RIDGE,
                                 font=('times new roman', 15, 'bold'))
        search_frm.place(x=10, y=100, width=540, height=80)

        search_label=Label(search_frm,text='Search By',bd=2,relief=RIDGE,bg='dark blue',fg='white',font=('times new roman',14,'bold'))
        search_label.place(x=10,y=7,width=100,height=40)

        search_by = ttk.Combobox(search_frm, font=('times new roman', 14), state='readonly')
        search_by['values'] = ['Select search by', 'Roll No', 'Phone No']
        search_by.current(0)
        search_by.place(x=120,y=13,width=120)

        search_by_entry = ttk.Entry(search_frm, font=('times new roman', 14, 'bold'))
        search_by_entry.place(x=250,y=13,width=110)

        search_btn = Button(search_frm, text='Search', cursor='hand2', bg='dark blue', fg='white',
                           font=('times new roman', 15, 'bold'))
        search_btn.place(x=370,y=7,width=70)

        showall_btn = Button(search_frm, text='Show All', cursor='hand2', bg='dark blue', fg='white',
                            font=('times new roman', 15, 'bold'))
        showall_btn.place(x=450, y=7, width=80)

        #------------------------table frm-------------------------
        table_frm=Frame(right_label,relief=RIDGE,bd=2)
        table_frm.place(x=10,y=190,width=540,height=350)

        #-------------------scroll bar---------------------
        scroll_x=ttk.Scrollbar(table_frm,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frm,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frm,columns=('dept','year','course','sem','id','name','sec','roll_no',
                                                           'gender','dob','phn','email','add','teacher','pic_sts')
                                        ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #-------------------TABLE------------------------

        self.student_table.heading('dept',text='Department')
        self.student_table.heading('year', text='Year')
        self.student_table.heading('course', text='Course')
        self.student_table.heading('sem', text='Semester')
        self.student_table.heading('id', text='Student ID')
        self.student_table.heading('name', text='Name')
        self.student_table.heading('sec', text='Section')
        self.student_table.heading('roll_no', text='Roll No')
        self.student_table.heading('gender', text='Gender')
        self.student_table.heading('dob', text='DOB')
        self.student_table.heading('phn', text='Phone No')
        self.student_table.heading('email', text='Email ID')
        self.student_table.heading('add', text='Address')
        self.student_table.heading('teacher', text='Teacher')
        self.student_table.heading('pic_sts', text='Photo status')

        self.student_table['show']='headings'

        self.student_table.column('dept',width=100)
        self.student_table.column('year', width=100)
        self.student_table.column('sec', width=100)
        self.student_table.column('sem', width=100)
        self.student_table.column('course', width=100)
        self.student_table.column('id', width=100)
        self.student_table.column('name', width=100)
        self.student_table.column('roll_no', width=100)
        self.student_table.column('gender', width=100)
        self.student_table.column('dob', width=100)
        self.student_table.column('phn', width=100)
        self.student_table.column('email', width=100)
        self.student_table.column('teacher', width=100)
        self.student_table.column('add', width=100)
        self.student_table.column('pic_sts', width=100)


        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #----------------feature function-------------------

        #----------------save btn feature-------------------

    def add_data(self):
        if self.var_dept.get()=='Select Department' or self.var_id.get()=='' or self.var_roll_no.get()=='':
            messagebox.showerror('Error','Please provide all details...')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', database='face_recognition', user='root',
                                           password='DeepGujjar@007')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into student_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                  (self.var_dept.get(),self.var_year.get(),self.var_course.get(),self.var_sem.get(),
                                   self.var_id.get(),self.var_name.get(),self.var_sec.get(),self.var_roll_no.get(),
                                   self.var_gender.get(),self.var_dob.get(),self.var_phn.get(),self.var_email.get(),
                                   self.var_add.get(),self.var_teacher.get(),self.var_pic_sts.get()))
                messagebox.showinfo('success', 'you have successfully update your data')
                conn.commit()
                self.fetch_data()
                conn.close()
            except  Exception as es:
                messagebox.showerror('error', f'Due to:{str(es)}', parent=self.root)

        #--------------fatch all data-----------------------

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', database='face_recognition', user='root', password='DeepGujjar@007')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from student_table')
        row = my_cursor.fetchall()

        if len(row) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in row:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()

        #-----------------get cursor-------------------------

    def get_cursor(self,event=''):
        focus_cursor=self.student_table.focus()
        content=self.student_table.item(focus_cursor)
        data=content['values']
        self.var_dept.set(data[0]),
        self.var_year.set(data[1]),
        self.var_course.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_sec.set(data[6]),
        self.var_roll_no.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_phn.set(data[10]),
        self.var_email.set(data[11]),
        self.var_add.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_pic_sts.set(data[14])

   #-----------------------update data-------------------------
    def update_data(self):
        if self.var_dept.get() == 'Select Department' or self.var_id.get() == '' or self.var_roll_no.get() == '':
            messagebox.showerror('Error', 'Please provide all details...')

        else:
            Update=messagebox.askyesno('Ask','Do you want to update this data?',parent=self.root)
            if Update>0:
                conn = mysql.connector.connect(host='localhost', database='face_recognition', user='root',
                                               password='DeepGujjar@007')
                my_cursor = conn.cursor()

                dept = self.var_dept.get()
                year = self.var_year.get()
                course = self.var_course.get()
                sem = self.var_sem.get()
                name = self.var_name.get()
                sec = self.var_sec.get()
                roll_no = self.var_roll_no.get()
                gender = self.var_gender.get()
                dob = self.var_dob.get()
                phn = self.var_phn.get()
                email = self.var_email.get()
                teacher = self.var_teacher.get()
                pic_sts = self.var_pic_sts.get()
                # add=self.var_add.get()
                id=self.var_id.get()

                inputs=(dept,year,course,sem,name,sec,roll_no,gender,dob,phn,email,teacher,pic_sts,id)
                # ,roll_no,gender,dob,phn,email,add,teacher,pic_sts,
                # ,roll_no=%s,gender=%s,dob=%s,phn=%s,email=%s,add=%s,teacher=%s,pic_sts=%s
                query='update student_table set dept=%s,year=%s,course=%s,sem=%s,name=%s,sec=%s,roll_no=%s,gender=%s,dob=%s,phn=%s,email=%s,teacher=%s,pic_sts=%s where id=%s'
                my_cursor.execute(query,inputs)

                conn.commit()

                conn.close()
                self.fetch_data()
                messagebox.showinfo('success','you have successfully update your data')

    #------------------DELETE------------------------------

    def delete_data(self):
        if self.var_id.get()=='':
            messagebox.showerror('Error','please provide a student id',parent=self.root)

        else:
            try:
                Delete=messagebox.askyesno('ask','do you want to delete the data',parent=self.root)

                if Delete>0:
                    conn = mysql.connector.connect(host='localhost', database='face_recognition', user='root',
                                                       password='DeepGujjar@007')
                    my_cursor = conn.cursor()
                    my_cursor.execute('delete from student_table where id=%s',([self.var_id.get()]))

                else:
                    if not Delete:
                        return
                messagebox.showinfo('success','you have successfully deleted data')
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to:{str(es)}',parent=self.root)

    #-----------------------reset-----------------------

    def reset_data(self):
        self.var_dept.set('Select the department')
        self.var_year.set('Select the year')
        self.var_course.set('Select the course')
        self.var_sem.set('Select the semester')
        self.var_id.set('')
        self.var_name.set('')
        self.var_sec.set('Select section')
        self.var_roll_no.set('')
        self.var_gender.set('Select the gender')
        self.var_dob.set('')
        self.var_phn.set('')
        self.var_email.set('')
        self.var_add.set('')
        self.var_teacher.set('')
        self.var_pic_sts.set('')

    #-------------------------------generating dataset---------------------------------

    def generated_dataset(self):
        if self.var_id.get()=='':
            messagebox.showerror('Error','please provide a student id',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', database='face_recognition', user='root',
                                               password='DeepGujjar@007')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from student_table')
                my_result=my_cursor.fetchall()
                id=0
                for i in my_result:
                    id=id+1

                dept = self.var_dept.get()
                year = self.var_year.get()
                course = self.var_course.get()
                sem = self.var_sem.get()
                name = self.var_name.get()
                sec = self.var_sec.get()
                roll_no = self.var_roll_no.get()
                gender = self.var_gender.get()
                dob = self.var_dob.get()
                phn = self.var_phn.get()
                email = self.var_email.get()
                teacher = self.var_teacher.get()
                pic_sts = self.var_pic_sts.get()
                # add=self.var_add.get()
                id = self.var_id.get()

                inputs = (dept, year, course, sem, name, sec, roll_no, gender, dob, phn, email, teacher, pic_sts, id)
                query = 'update student_table set dept=%s,year=%s,course=%s,sem=%s,name=%s,sec=%s,roll_no=%s,gender=%s,dob=%s,phn=%s,email=%s,teacher=%s,pic_sts=%s where id=%s'
                my_cursor.execute(query, inputs)

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #------------------------pre defined load data-------------------

                face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    #-----------scaling face

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path='data/user.'+str(id)+'.'+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow('cropped face',face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('result','Generating data set completed...')
            except Exception as es:
                messagebox.showerror('error',f'Due to:{str(es)}',parent=self.root)

if __name__=='__main__':
    root=Tk()
    obj=Student_detail(root)
    root.mainloop()