import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    

root=Tk()
root.title('Atharva Music player project')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'E:\Atharva\A_ Music')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="PLAY",command=playsong)
playbtn.config(font=('sans serif',20),bg="DodgerBlue2",fg="white",padx=6,pady=6)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="PAUSE",command=pausesong)
pausebtn.config(font=('sans serif',20),bg="DodgerBlue2",fg="white",padx=6,pady=6)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="STOP",command=stopsong)
stopbtn.config(font=('sans serif',20),bg="DodgerBlue2",fg="white",padx=6,pady=6)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="RESUME",command=resumesong)
Resumebtn.config(font=('sans serif',20),bg="DodgerBlue2",fg="white",padx=6,pady=6)
Resumebtn.grid(row=1,column=3)

mainloop()