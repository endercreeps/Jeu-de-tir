from tkinter import *
from turtle import *
import math
from PIL import Image ,ImageTk
from random import randint

def create_window() :
    root = Tk()
    root.title("Jeu de tir")
    root.geometry("1500x922")
    root.minsize(1500,922)
    root.iconbitmap("pointeur_0.ico")
    root.config(background='#424242')
    return root

def create_widgets():
    graphic_zone = Canvas(root, width=1499, height=921 , bg = color,highlightthickness=0)
    graphic_zone.pack()
    return graphic_zone

def create_background():
    background=ImageTk.PhotoImage(Image.open("bgd.jpg"),master=root)
    background_o=graphic_zone.create_image(0,0,anchor='nw',image=background)
    return background

# def create_pointeur():
#     pointeur=ImageTk.PhotoImage(Image.open("pointeur_0.png"),master=root)
#     pointeur_=graphic_zone.create_image(0,0,anchor='nw',image=pointeur)
#     return pointeur

def create_cible():
    global cible
    global cible_
    cible=ImageTk.PhotoImage(Image.open("cible_0.png"),master=root)
    cible_=graphic_zone.create_image(randint(60,1440),randint(80,620),anchor='center',image=cible)
    return cible

# def cordo(event):
#     x=event.x
#     y=event.y
#     print(x,y)

def tir(event):
    coordo=[]
    x,y=event.x,event.y
    global stop
    global cible_
    global cible
    global vie
    global point
    if stop:
        cordo=(graphic_zone.coords(cible_))
        if cordo[0]-x<=40 and cordo[0]-x>=-40  and cordo[1]-y<=40 and cordo[1]-y>=-40 :
            graphic_zone.delete(cible)
            point+=100
            cible=create_cible()
        else:
            vie-=1
            aff_vie['text'] = f"Vie : {vie}"
        test()
    else: 
        pass
        
def test():
    global cible
    global vie
    global stop
    if vie ==0:
        fin = Label(root, text="PERDU",font=("Courrier",50), fg="red",bg='#181818')
        fin.place(x=650,y=400) 
        graphic_zone.delete(cible)
        stop=False

color = "#282C34"
global vie
global point
global stop
stop = True
timer=0
point=0
vie=5
root=create_window()
graphic_zone=create_widgets()
backgroundr=create_background() 
# pointeur=create_pointeur()
cible=create_cible()
root.config(cursor="tcross")
# graphic_zone.bind("<Motion>",cordo)
graphic_zone.bind("<ButtonPress-1>",tir)
timer+=1

aff_vie = Label(root, text=f"Vie : {vie}",font=("Courrier",18), fg="red",bg='#181818')
aff_vie.place(x=1400,y=842)


root.mainloop()


