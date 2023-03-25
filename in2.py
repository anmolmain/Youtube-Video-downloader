from pytube import Playlist
from pytube import YouTube
from tkinter import *
from tkinter import messagebox

# Import the required library
from tkinter import *
from tkinter import ttk
win=Tk()
win.title("Youtube video downloader")
win.geometry("1080x620+100+20")
win.configure(bg='silver')
def get_input():

    try:
        u = text.get(1.0, "end-1c")
        pth0 = "/"
        pth1 = pth.get(1.0, "end-1c")+pth0
        p = Playlist(u)
        tag = res.get(1.0, "end-1c")
        for url in p.video_urls:
            yt = YouTube(url)
            # print(yt.title)       
            YouTube(url).streams.get_by_itag(tag).download(pth1)
        messagebox.showinfo("Information","All videos downloaded")

    except:
        messagebox.showerror("Error", "You entered something incorrect")
        win.destroy()

l1=Label(win, text=" ", font=('Calibri 15'))
l1.configure(bg='silver')
l1.pack()

l2=Label(win, text="Enter video url :", font=('Calibri 15'))
l2.configure(bg='silver')
l2.pack()
text=Text(win, width=80, height=5)
text.insert(END, "")
text.pack()
l3=Label(win, text="Enter Path for downloading :", font=('Calibri 15'))
l3.configure(bg='silver')
l3.pack()
pth=Text(win, width=80, height=2)
pth.insert(END, "")
pth.pack()

l4=Label(win, text="Enter resolution Tag :", font=('Calibri 15'))
l4.pack()
l4.configure(bg='silver')

l1=Label(win, text="Resolution tags \n18 : 360p\n22 : 720p\n137 1080p\n140 : 128kps", font=('Calibri 15'))
l1.configure(bg='silver')
l1.pack()
res=Text(win, width=80, height=2)
res.insert(END, "")
res.pack()
l1=Label(win, text=" ", font=('Calibri 15'))
l1.configure(bg='silver')
l1.pack()
b=Button(win, text="Download", command=get_input, font=('bold 20'))
b.pack()

l1=Label(win, text=" ", font=('Calibri 25'))
l1.configure(bg='silver')
l1.pack()

l7=Label(win, text=" ", font=('Calibri 20'))
l7.configure(bg='silver')
l7.pack()

l7.configure(text="Note : The screen will become unresponsive ones download start",bg='indianred')
l1=Label(win, text=" ", font=('Calibri 10'))
l1.configure(bg='silver')
l1.pack()
l8=Label(win, text="", font=('Calibri 10'))
l8.configure(text="Credits : github @anmolmain",bg='indianred')
l8.pack()

win.mainloop()





