from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2

class Train():
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x710+0+0')
        self.root.title('Training Data')



        img4 = Image.open(r"C:\Users\Dell\PycharmProjects\Face Recognition Attandence System\project image\train.jpg")
        img4 = img4.resize((1530, 770), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        bg_img = Label(root, image=self.photoimage4)
        bg_img.place(x=0, y=0, width=1530, height=770)

        train_face_btn = Button(root, command=self.train_data,text='Click here to train your data...', cursor='hand2', font=('times new roman', 16, 'bold'),
                                bg='red', fg='white')
        train_face_btn.place(x=575, y=630, width=320, height=45)

        # text='IIMT College of Engineering'



    def train_data(self):
        data_dir=('data')
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        face=[]
        ids=[]
        for image in path:
            # img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            img=Image.open(image).convert('L')

            imageNp=np.array(img)
            id=int(os.path.split(image)[1].split('.')[1])

            face.append(imageNp)
            ids.append(id)
            cv2.imshow('Training...',imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #---------train the classifier---------------
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(face,ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo('result','training data completed')



if __name__=='__main__':
    root=Tk()
    obj=Train(root)
    root.mainloop()