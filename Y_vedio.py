from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import pytube

class Y_vedio:
    def __init__ (self,root):
        self.link_of_vedio = StringVar()
        self.root = root
        self.root.title("YOUTUBE DOWNLOADER")
        self.root.geometry("700x500")
        self.root.configure(bg="white")

        img=Image.open("img.jpg")
        img = img.resize((700, 120), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        imglabel = Label(self.root, image=self.photoimg, bd=2, relief=RIDGE)
        imglabel.place(x=0, y=0, width=700, height=120)

        canvas1 = Frame(self.root, bd=4, bg="black", relief=RIDGE)
        canvas1.place(x=0, y=120, width=700, height=380)

        lbl = Label(self.root, text="ENTER THE YOUTUBE LINK : ", font=("Arial", 14, "bold"), bg="black", fg="white")
        lbl.place(x=190, y=180, width=300, height=15)
        
        txt = ttk.Entry(self.root, width=35, textvariable=self.link_of_vedio, font=("times new roman", 12, "bold"))
        txt.grid(row=0, column=0)
        txt.place(x=200, y=230, height=30)
        
        download = Button(self.root, text="DOWNLOAD VIDEO", command=self.download, width=14,
                          font=("Arial", 12, "bold"), bg="white", fg="red", bd=2, relief=RIDGE)
        download.grid(row=0, column=0)
        download.place(x=210, y=310, width=260)
    
    def download(self):
        try:
            print("Donwload......")
            Enter_the_link = self.link_of_vedio.get()
            vedio_link = pytube.YouTube(Enter_the_link)
            quality = vedio_link.streams.get_highest_resolution()

            print("Title: ",vedio_link.title)
            print("VIWS : ",vedio_link.views)
            print("Length : ",vedio_link.length)
            print("Descrption",vedio_link.description)
            print("Rating",vedio_link.rating)
            quality.download('')
            messagebox.showinfo('Info', 'FULL DOWNLOADED SUCCESSFULLY', parent=self.root)
        except Exception as e:
            print("Not Download")
            print(e)
            messagebox.showinfo('Info',f'{e} TRY AGAIN LATER ',parent=self.root)
            
            
if __name__ == "__main__":
    root=Tk()
    obj=Y_vedio(root)
    root.mainloop()