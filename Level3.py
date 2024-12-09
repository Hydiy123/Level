from tkinter import *
from tkinter.messagebox import  showinfo
from tkinter import Entry
import random
import pygame 


password = "17171"

pygame.mixer.init()


def par():
    global password
    pad = p.get()
    if pad == password:
        
        pad = password
        print("Password is correct")
        msg = "Password is correct"
        showinfo(title="Correct Password",message=msg)
        sound = pygame.mixer.Sound("cherry.wav")
        sound.play()
        
    else:
        print("try again")

root = Tk()
root.title("Security")
root.geometry("500x500+100+100")
root.resizable(0,0)
root.config(bg="#1a1a1a")

v = StringVar()
p = Entry(root,textvariable=v,font=("Comic Sans MS","15","bold"))
p.pack()

b1 = Button(root,text="Enter",bg="white",font=("Comic Sans MS","15","bold"),command=par)
b1.pack()

name_lbl= Label(root,text="Music by bluelike_u-24430674,Music by Albert-Paul from Pixabay",font=("Comic Sans MS","15","bold"))
name_lbl.pack()

name1_lbl= Label(root,text="Music by Albert-Paul from Pixabay",font=("Comic Sans MS","15","bold"))
name1_lbl.pack()
root.mainloop()