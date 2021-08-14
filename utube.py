from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
from PIL import Image,ImageTk
import time

window=Tk()
window.title("Opening YouTube Video Downloader....")
window.geometry("550x350")
window.configure(bg="black")

image=Image.open("yt.png")
resize_img=image.resize((550,350))
img=ImageTk.PhotoImage(resize_img)

limg=Label(window,image=img,bd=0)
limg.image=img
limg.place(x=0,y=0)

bar = Progressbar(window,orient=HORIZONTAL,length=550,mode="determinate")
bar.start(10)
bar.place(x=0,y=330)

def main_window():
    window.destroy()
    root=Tk()
    root.title("YouTube Video/Audio Downloader")
    root.geometry("550x350")
    root.configure(bg="old lace")
    
    def browse():
        dir=filedialog.askdirectory()
        path.set(dir)
            
    def downloader(ext="mp4"):
        choice=v.get()
        df=path.get()

        if len(q.get()) != 0 and df and choice == 1:
            YouTube(q.get()).streams.filter(progressive = True,file_extension=ext).first().download()
            messagebox.showinfo("Successful","Successfully Downloaded Video In\n"+df)

        elif len(q.get()) != 0 and df and choice == 2:
            YouTube(q.get()).streams.filter(only_audio = True).first().download()
            messagebox.showinfo("Successful","Successfully Downloaded Audio In\n"+df)

        elif len(q.get()) != 0 and df and not choice:
            messagebox.showinfo("Missing","Please select format")

        elif len(q.get()) != 0 and not df and not choice:
            messagebox.showinfo("Missing","Please select format and destination")

        elif len(q.get()) != 0 and not df and choice:
            messagebox.showinfo("Missing","Please select destination")
            
        elif not len(q.get()) != 0 and df and not choice:
            messagebox.showinfo("Missing","Please enter a URL and select extension")

        elif not len(q.get()) != 0 and df and choice:
            messagebox.showinfo("Missing","Please enter a URL")

        elif not len(q.get()) != 0 and not df and choice:
            messagebox.showinfo("Missing","Please enter a URL and select destination")

        elif not len(q.get()) != 0 and not df and not choice:
            messagebox.showinfo("Missing","Please fill the required fields")
            
        elif not len(q.get()) != 0 and not df:
            messagebox.showinfo("Missing","Please enter URL and select Destination")

    image=Image.open("yt1.png")
    resize_img=image.resize((545,140))
    img=ImageTk.PhotoImage(resize_img)

    limg=Label(root,image=img,bd=0)
    limg.image=img
    limg.place(x=0,y=2)

    l1=Label(root,text="Video URL :",font = ("Helvetica",14),bg="old lace",fg="black").place(x=10,y=165)
    q=StringVar()
    e=Entry(root,textvariable=q,font = ("Helvetica",10),width=35,bd = 9).place(x=125,y=165)

    v=IntVar()
    r1 = Radiobutton(root, text="Video", variable=v, value=1,bg="tomato",width=5).place(x=395,y= 167)
    r2 = Radiobutton(root, text="Audio", variable=v, value=2,bg="tomato",width=5).place(x=465,y= 167)
    l2=Label(root,text="Destination :",font = ("Helvetica",14),bg="old lace",fg="black").place(x=10,y=215)

    path=StringVar()
    e1=Entry(root,textvariable=path,font = ("Helvetica",10),width=35,bd=9).place(x=125,y=215)
    b2=Button(root,text="Browse",font =("segoe UI",10),width =10,bg="gold",command=browse).place(x=395,y=215)

    b=Button(root,text="Download ↓",font = ("Verdana",12,"bold"),bg="red",fg="white",command = downloader).place(x=210,y=270)

window.after(1500,main_window)
mainloop() 
