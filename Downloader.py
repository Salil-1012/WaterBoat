import pytube
from tkinter import *
from PIL import Image,ImageTk
from Y_vedio import Y_vedio

class Downloader:
    def __init__ (self,root):
        self.root=root
        self.root.title("YOUTUBE DOWNLOADER")
        self.root.geometry("1350x600")

        img=Image.open("img.jpg")
        img=img.resize((1350,600),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        imglabel=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        imglabel.place(x=0,y=0,width=1350,height=600)
        
   
        
        download=Button(self.root,text="YOUTUBE VIDEO DOWNLOAD",command=self.vedio,width=14,font=("Arial",14,"bold"),bg="white",fg="red",bd=2,relief=RIDGE)
        download.grid(row=0,column=0)
        download.place(x=490,y=20,width=330)
        
     
        
    def vedio(self):
        self.new_window=Toplevel(self.root)
        self.app=Y_vedio(self.new_window)
        
    

if __name__ == "__main__":
    root=Tk()
    obj=Downloader(root)
    root.mainloop()