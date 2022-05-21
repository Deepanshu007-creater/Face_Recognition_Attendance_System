import tkinter.messagebox

import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student_detail import Student_detail
from train import Train
from face_detect import Face_Detect
import os
from Attandence import Attandence


class face_recognition():

    #-------------Root Window---------------
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x710+0+0')
        self.root.title('Face Recognition Attandence System')


        #-----------------label 1 first image---------------

        img1=Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\IIMT_college_1 (2).jpg')
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimage1)
        first_label.place(x=0,y=0,width=500,height=130)

        #---------------label 1 second image---------------

        img2 = Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\IIMT_college_2.jpg')
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimage2)
        first_label.place(x=500, y=30, width=500, height=130)

        #--------------label 1 third image-----------------

        img3 = Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\IIMT_college_3.jpg')
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        first_label = Label(self.root, image=self.photoimage3)
        first_label.place(x=1000, y=35, width=500, height=130)

        #----------------clz title on lable 1----------

        clz_title=Label(root,text='IIMT College of Engineering',font=('times new roman',25,'bold'),fg='red')
        clz_title.place(x=0,y=0,width=1530,height=35)

        #----------------background image-------------------

        bg_img=Image.open(r"C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\bg.jpg")
        bg_img=bg_img.resize((1530,710),Image.ANTIALIAS)
        self.bg_photoimage=ImageTk.PhotoImage(bg_img)

        bg_label=Label(self.root,image=self.bg_photoimage)
        bg_label.place(x=0,y=130,width=1530,height=710)

        #-------------project title---------------

        project_ttl=Label(bg_label,text='Face Recognition Attandnce System',font=('times new roman',35,'bold'),fg='red')
        project_ttl.place(x=0,y=0,width=1530,height=45)

        #--------------buttons--------------


                 #--------------------student button------------

        img4=Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\student_button.jpg')
        img4=img4.resize((170,170),Image.ANTIALIAS)
        self.button1_photoimage=ImageTk.PhotoImage(img4)

        student_btn_img=Button(bg_label,image=self.button1_photoimage,command=self.student,cursor='hand2')
        student_btn_img.place(x=100,y=100,width=170,height=170)

        student_btn=Button(bg_label,text='Students Detail',command=self.student,cursor='hand2',font=('times new roman',16,'bold'),bg='white',fg='red')
        student_btn.place(x=100,y=260,width=170,height=45)

                #----------------detect face----------------------

        img5=Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\detect_face.jpg')
        img5=img5.resize((170,170),Image.ANTIALIAS)
        self.button2_photoimage=ImageTk.PhotoImage(img5)

        detect_face_img=Button(bg_label,image=self.button2_photoimage,cursor='hand2',command=self.detect_face)
        detect_face_img.place(x=400,y=100,width=170,height=170)

        detect_face_btn=Button(bg_label,command=self.detect_face ,text='Detect Faces',font=('times new roman',16,'bold'),bg='white',fg='red',cursor='hand2')
        detect_face_btn.place(x=400,y=260,width=170,height=45)

               #-----------attandence----------------------

        img6=Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\attandence.jpg')
        img6=img6.resize((170,170),Image.ANTIALIAS)
        self.button3_photoimage=ImageTk.PhotoImage(img6)

        attandence_img=Button(bg_label,command=self.Attandence,image=self.button3_photoimage,cursor='hand2')
        attandence_img.place(x=700,y=100,width=170,height=170)

        attandence_btn=Button(bg_label,text='Attandence',command=self.Attandence,cursor='hand2',font=('times new roman',16,'bold'),bg='white',fg='red')
        attandence_btn.place(x=700,y=260,width=170,height=45)

                #------------train faces--------------------

        img7=Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\train_face.jpg')
        img7=img7.resize((170,170),Image.ANTIALIAS)
        self.button4_photoimage=ImageTk.PhotoImage(img7)

        train_face_img=Button(bg_label,command=self.train,image=self.button4_photoimage,cursor='hand2')
        train_face_img.place(x=100,y=340,width=170,height=170)

        train_face_btn=Button(bg_label,command=self.train,text='Train Faces',cursor='hand2',font=('times new roman',16,'bold'),bg='white',fg='red')
        train_face_btn.place(x=100,y=500,width=170,height=45)

                #-------------photos---------------------

        img8=Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\faces.jpg')
        img8=img8.resize((170,170),Image.ANTIALIAS)
        self.button5_photoimage=ImageTk.PhotoImage(img8)

        face_img=Button(bg_label,command=self.open_img,image=self.button5_photoimage,cursor='hand2')
        face_img.place(x=400,y=340,width=170,height=170)

        face_btn=Button(bg_label,command=self.open_img,text='Face Images',cursor='hand2',font=('times new roman',16,'bold'),bg='white',fg='red')
        face_btn.place(x=400,y=500,width=170,height=45)

                #-----------exit--------------

        img9=Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\exit.jpg')
        img9=img9.resize((170,170),Image.ANTIALIAS)
        self.button6_photoimage=ImageTk.PhotoImage(img9)

        exit_img=Button(bg_label,command=self.iExit,image=self.button6_photoimage,cursor='hand2')
        exit_img.place(x=700,y=340,width=170,height=170)

        exit_btn=Button(bg_label,text='Exit',command=self.iExit,cursor='hand2',font=('times new roman',16,'bold'),bg='white',fg='red')
        exit_btn.place(x=700,y=500,width=170,height=45)

    def open_img(self):
        os.startfile('data')



    def student(self):
        self.new_window=Toplevel(self.root)
        self.stud=Student_detail(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.stud=Train(self.new_window)

    def detect_face(self):
        self.new_window=Toplevel(self.root)
        self.stud=Face_Detect(self.new_window)

    def Attandence(self):
        self.new_window=Toplevel(self.root)
        self.stud=Attandence(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project")
        if self.iExit>0:
            self.root.destroy()
        else:
            return





if __name__=='__main__':
    root=Tk()
    obj=face_recognition(root)
    root.mainloop()




