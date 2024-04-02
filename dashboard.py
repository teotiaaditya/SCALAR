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
        
        #===content window=====
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((920, 350))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300, height=100)
        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300, height=100)
        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300, height=100)

        footer=Label(self.root, text="Student Result Managment System\nContact us for any info 999xxxxx11.", font=("goudy old style", 15), bg="#262626", fg="white") .pack(side=BOTTOM, fill=X)
        

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()