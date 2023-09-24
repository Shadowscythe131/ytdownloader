from tkinter import *
from pytube import YouTube
window=Tk()
window.title("Youtube Downloader")
window.geometry("750x400")
def download_video():
    output.config(text="Downloading")
    try:
        yt=YouTube(URLinput.get())
        video=yt.streams.get_highest_resolution()
        title=yt.title
        video.download(SPinput.get())
        output.config(text="Download successful of \""+title+"\" at "+SPinput.get()+".")
    except Exception as e:
        output.config(text="An error occurred or a connection to the youtube servers could not be created.\nCheck that you have a connection to the internet and that all fields are accurate: "+str(e))
label1=Label(window,text="URL:")
URLinput=Entry(window,width=20)
label2=Label(window,text="Download Path:")
SPinput=Entry(window)
submit=Button(window,text="Download",command=download_video)
output=Label(window)
label1.pack();URLinput.pack();label2.pack();SPinput.pack();submit.pack();output.pack()

window.mainloop()