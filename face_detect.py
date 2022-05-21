from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os


class Face_Detect():
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x710+0+0')
        self.root.title('Face Detect')

        clz_title = Label(root, text='Face Detection', font=('times new roman', 50, 'bold'), fg='red',bg='white')
        clz_title.place(x=730, y=0, width=730, height=100)

        img5 = Image.open(r'C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\logo.jpg')
        img5 = img5.resize((730, 100), Image.ANTIALIAS)
        self.photoimage5 = ImageTk.PhotoImage(img5)

        left_lbl_img = Label(root, image=self.photoimage5,bg='white')
        left_lbl_img.place(x=0, y=0, width=730, height=100)

        img4 = Image.open(r"C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\face_detection_data.jpg")
        img4 = img4.resize((1530, 650), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        bg_img = Label(root, image=self.photoimage4)
        bg_img.place(x=0, y=100, width=1530, height=650)


        train_face_btn = Button(root, command=self.face_detect_data, text='Click here to detect the face', cursor='hand2',
                                font=('times new roman', 16, 'bold'),
                                bg='red', fg='white')
        train_face_btn.place(x=255, y=630, width=440, height=60)

        train_face_btn = Button(root, command=self.face_detect_data, text='scan',
                                cursor='hand2',
                                font=('times new roman', 16, 'bold'),
                                bg='red', fg='white')
        train_face_btn.place(x=1080, y=420, width=110, height=40)

    def mark_attandence(self,i,r,n,d):
        with open("attandence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    def face_detect_data(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,clf):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            # gray=Image.open(img).convert('L')
            feature=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)

            coord=[]
            for (x,y,w,h) in feature:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host='localhost', database='face_recognition', user='root',
                                               password='DeepGujjar@007')
                my_cursor = conn.cursor()
                my_cursor.execute('select name from student_table where id='+str(id))
                n=my_cursor.fetchone()
                n='+'.join(n)

                my_cursor.execute('select roll_no from student_table where id=' + str(id))
                r = my_cursor.fetchone()
                r = '+'.join(r)

                my_cursor.execute('select dept from student_table where id=' + str(id))
                d = my_cursor.fetchone()
                d = '+'.join(d)

                my_cursor.execute('select id from student_table where id=' + str(id))
                i = my_cursor.fetchone()
                i = '+'.join(i)


                if confidence>77:
                    cv2.putText(img, f'ID:{i}', (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    cv2.putText(img,f'Roll No:{r}',(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,color,3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,color,3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,color,3)
                    self.mark_attandence(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, "Unknown Person", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,color, 3)

                coord=[x,y,w,h]
            return coord
        # color=(255,255,255)
        # text='Face'
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),clf)
            return img

        faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img=recognize(img,clf,faceCascade)
            cv2.imshow('Face Recognition...',img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__=='__main__':
    root=Tk()
    obj=Face_Detect(root)
    root.mainloop()