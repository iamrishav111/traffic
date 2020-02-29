from PIL import Image, ImageTk
from tkinter import Tk, BOTH,X
from tkinter.ttk import Frame, Label, Style,Progressbar
import time
width=300
height=200


def initUI(master,path,pic,xi,yi):
    stgImg=Image.open(str((path-1)5)++str(pic)+.jpg)
    # paths=homeiamrishavPycharmProjectsHelloWorld0
    stgImg=stgImg.resize((width,height),Image.ANTIALIAS)
    stgImg2=ImageTk.PhotoImage(stgImg)
    # frame=Frame(master,height=800)
    # frame.pack(fill=X)
    label=Label(master, image=stgImg2)
    label.image = stgImg2
    label.place(x=543xi-495.5,y=288yi-269)
    label1=Label(master)
    progress=Progressbar(label1,length=200,mode='determinate')
    progress['value']=path33
    fn=str(path33)
    label2=Label(master,text=fn,font=arial 12 bold,background=yellow)

    label2.place(x=543xi-240.5,y=288yi-49)

    progress.pack()
    label1.place(x=543xi-495.5,y=288yi-49)
    root.update_idletasks()


root = Tk()
root.title(Traffic)
root.configure(background=#f0eec5)
root.geometry({0}x{1}+0+0.format(root.winfo_screenwidth(), root.winfo_screenheight()))
initUI(root,1,1,1,1)
for i in range(1,3)
    for j in range(1,10)
        initUI(root,i,j,(j-1)%3 +1,(j-1)3 +1)
    time.sleep(3)
root.mainloop()