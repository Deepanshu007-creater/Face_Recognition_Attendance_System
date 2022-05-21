import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2
import csv
from tkinter import filedialog
import os


myData=[]
class Attandence():

    #-------------Root Window---------------
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x710+0+0')
        self.root.title('Face Recognition Attandence System')

        # -----------------variable--------------
        self.var_atten_dept = StringVar()
        self.var_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_roll_no = StringVar()
        self.var_attandence_sts=StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()


        #-----------------label 1 first image---------------

        img1=Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\IIMT_college_1 (2).jpg')
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimage1)
        first_label.place(x=0, y=0, width=500, height=130)

        img5 = Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\logo.jpg')
        img5 = img5.resize((730, 100), Image.ANTIALIAS)
        self.photoimage5 = ImageTk.PhotoImage(img5)

        left_lbl_img = Label(root, image=self.photoimage5, bg='white')
        left_lbl_img.place(x=500, y=0, width=1000, height=130)

        #-------------main frame

        main_frame = Frame(root, bd=2,bg="white")
        main_frame.place(x=13, y=140, width=1330, height=600)

        #---------------left frame
        left_label=LabelFrame(main_frame,text='Attandence Details',bd=2,relief=RIDGE,font=('times new roman',15,'bold'))
        left_label.place(x=10,y=10,width=750,height=550)

             #-----------student id---------------------

        student_id= Label(left_label, text='Student ID', font=('times new roman', 15, 'bold'))
        student_id.grid(row=0, column=0, padx=5)

        student_id_entry=ttk.Entry(left_label,textvariable=self.var_id,font=('times new roman', 15, 'bold'))
        student_id_entry.grid(row=0,column=1,padx=5,pady=5)

                    #----------student name-------------------

        nameLable = Label(left_label, text='Student Name', font=('times new roman', 15, 'bold'))
        nameLable.grid(row=0, column=2, padx=5,pady=5)

        atten_name = ttk.Entry(left_label,textvariable=self.var_atten_name ,font=('times new roman', 15, 'bold'))
        atten_name.grid(row=0, column=3, padx=5, pady=5)

             #------------department----------------------

        deptLable = Label(left_label, text='Department', font=('times new roman', 15, 'bold'))
        deptLable.grid(row=1, column=0, padx=5,pady=5)

        atten_dept = ttk.Entry(left_label, textvariable=self.var_atten_dept, font=('times new roman', 15, 'bold'))
        atten_dept.grid(row=1, column=1, padx=5, pady=5)

                     # -------------roll no-------------------
        rollLabel = Label(left_label, text='Roll No.', font=('times new roman', 15, 'bold'))
        rollLabel.grid(row=1, column=2, padx=5, pady=5)

        atten_roll_no = ttk.Entry(left_label,textvariable=self.var_atten_roll_no ,font=('times new roman', 15, 'bold'))
        atten_roll_no.grid(row=1, column=3, padx=5, pady=5)

        #---------------time

        timeLable = Label(left_label, text='Time.', font=('times new roman', 15, 'bold'))
        timeLable.grid(row=2, column=2, padx=5, pady=5)

        atten_time = ttk.Entry(left_label,textvariable=self.var_atten_time ,font=('times new roman', 15, 'bold'))
        atten_time.grid(row=2, column=3, padx=5, pady=5)

        # ----------date------------------

        dateLable = Label(left_label, text='Date.', font=('times new roman', 15, 'bold'))
        dateLable.grid(row=2, column=0, padx=5, pady=5)

        atten_date = ttk.Entry(left_label, textvariable=self.var_atten_date,font=('times new roman', 15, 'bold'))
        atten_date.grid(row=2, column=1, padx=5, pady=10)

             #----------attandence sts
        attandence_lable = Label(left_label, text='Attandence Status', font=('times new roman', 15, 'bold'))
        attandence_lable.grid(row=3, column=0, padx=5, pady=5)

        self.attandence_sts = ttk.Combobox(left_label, textvariable=self.var_attandence_sts,font=('times new roman', 14), state='readonly')
        self.attandence_sts['values'] = ['Select the department', 'Present','Absent']
        self.attandence_sts.current(0)
        self.attandence_sts.grid(row=3, column=1, padx=5, pady=5)

        # -----------btn frame

        btn_frm = LabelFrame(left_label, relief=RIDGE)
        btn_frm.place(x=10, y=200, width=535, height=40)

        # save btn
        import_btn = Button(btn_frm, text='Import csv', command=self.importCsv, cursor='hand2', bg='dark blue', fg='white',
                            font=('times new roman', 15, 'bold'), width=14)
        import_btn.grid(row=0, column=0)
        # delete btn
        export_btn = Button(btn_frm, text='Export csv', command=self.exportCsv,cursor='hand2', bg='dark blue', fg='white',
                            font=('times new roman', 15, 'bold'), width=14)
        export_btn.grid(row=0, column=1)
        # update btn
        # update_btn = Button(btn_frm, text='Reset', cursor='hand2', bg='dark blue',
        #                     fg='white',
        #                     font=('times new roman', 15, 'bold'), width=14)
        # update_btn.grid(row=0, column=2)
        # reset

        reset_btn = Button(btn_frm, text='Reset', command=self.reset_data,cursor='hand2', bg='dark blue',
                           fg='white',
                           font=('times new roman', 15, 'bold'), width=14)
        reset_btn.grid(row=0, column=2)

        #---------------right frame
        right_label = LabelFrame(main_frame, text='Attandence Details', bd=2, relief=RIDGE,
                                 font=('times new roman', 15, 'bold'))
        right_label.place(x=760, y=10, width=560, height=550)

        # ------------------------table frm-------------------------
        table_frm = Frame(right_label, relief=RIDGE, bd=2)
        table_frm.place(x=10, y=10, width=540, height=480)

        # -------------------scroll bar---------------------
        scroll_x = ttk.Scrollbar(table_frm, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frm, orient=VERTICAL)

        self.attandence_table = ttk.Treeview(table_frm,
                                          columns=('id','roll_no', 'name','department','time','date','attandence_sts')
                                          , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attandence_table.xview)
        scroll_y.config(command=self.attandence_table.yview)

        # -------------------TABLE------------------------

        self.attandence_table.heading('department', text='Department')
        self.attandence_table.heading('id', text='Student ID')
        self.attandence_table.heading('name', text='Name')
        self.attandence_table.heading('roll_no', text='Roll No')
        self.attandence_table.heading('time', text='Time')
        self.attandence_table.heading('date', text='Date')
        self.attandence_table.heading('attandence_sts', text='Attandence status')

        self.attandence_table['show'] = 'headings'

        self.attandence_table.column('department', width=100)
        self.attandence_table.column('id', width=100)
        self.attandence_table.column('name', width=100)
        self.attandence_table.column('roll_no', width=100)
        self.attandence_table.column('time', width=100)
        self.attandence_table.column('date', width=100)
        self.attandence_table.column('attandence_sts', width=100)

        self.attandence_table.pack(fill=BOTH, expand=1)

        self.attandence_table.bind("<ButtonRelease>",self.get_cursor)


        #---------fetch data

    def fetchData(self,rows):
        self.attandence_table.delete(*self.attandence_table.get_children())
        for i in rows:
            self.attandence_table.insert("",END,values=i)

    def importCsv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV file","*.csv"),("ALL file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(("CSV file", "*.csv"),("ALL file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.attandence_table.focus()
        content=self.attandence_table.item(cursor_row)
        rows=content['values']
        self.var_id.set(rows[0])
        self.var_atten_roll_no.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dept.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_attandence_sts.set(rows[6])

    def reset_data(self):
        self.var_id.set("")
        self.var_atten_roll_no.set("")
        self.var_atten_name.set("")
        self.var_atten_dept.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_attandence_sts.set("")






if __name__=='__main__':
    root=Tk()
    obj=Attandence(root)
    root.mainloop()