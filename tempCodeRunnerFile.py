from tkinter import*
from PIL import Image, ImageTk #pip install pillow py

class RMS:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #===¡cons=====
        # self.logo_dash=ImageTk.PhotoImage(file="images/logo.png")
        #===title=====
        title=Label(self.root, text="Student Result Managment System", font=("goudy old style", 20, "bold"), bg="#033054", fg="white") .place(x=0,y=0,relwidth=1, height=50)
        #===MenU====
        M_Frame=LabelFrame(self.root, text="Menus", font=( "times new roman" ,15),bg="white")
        M_Frame.place(x=10,y=70,width=1340, height=80)

        btn_course=Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=20,y=5,width=200,height=46)
        btn_course=Button(M_Frame, text="View Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=240,y=5,width=200,height=46)
        btn_course=Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=460,y=5,width=200,height=46)


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()