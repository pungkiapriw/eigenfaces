from tkinter import *
import os

main = Tk()
main.geometry('{}x{}'.format(1440, 810))
main.wm_title("Face recognition using OpenCV with Eigenface algorithm -")

svalue = StringVar() # defines the widget state as string

comments = """Welcome to face recognition using Eigenface algorithm.
Enter the name of the person in the text box given above to get trained.
Click the train to train the faces and recognize to recognize it"""








widgets = Label(main, 
           justify=LEFT,
           padx = 10, 
           text=comments).pack(side="bottom")

w = Entry(main,textvariable=svalue) # adds a textarea widget
w.pack()
w.place(x=400,y=100)
def eigen_train_button_fn():
    name = svalue.get()
    os.system('python train_eigen.py {}'.format(name))

def eigen_recog_button_fn():
    os.system('python recog_eigen.py')

train_eigen_button = Button(main,text="train", command=eigen_train_button_fn)
train_eigen_button.pack()
train_eigen_button.place(x=499,y=150)
recog_eigen_button = Button(main,text="recognize", command=eigen_recog_button_fn)
recog_eigen_button.pack()
recog_eigen_button.place(x=465,y=200)

main.mainloop()
