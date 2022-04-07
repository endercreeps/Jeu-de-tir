from tkinter import *
from turtle import *
import math
from PIL import Image ,ImageTk
from random import randint

def create_window() :
    root = Tk()
    root.title("Jeu de tir")
    root.geometry("1500x922+170+45")
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
    global cible,cible_
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
    global cible,vie,stop,timer,point_time,point,nb_tir,nb_tir_juste,start_time
    if point_time:
        nb_tir+=1
    if stop:
        cordo=(graphic_zone.coords(cible_))
        if cordo[0]-x<=5 and cordo[0]-x>=-5  and cordo[1]-y<=5 and cordo[1]-y>=-5 :
            graphic_zone.delete(cible)
            point+=130
            aff_point['text'] = f"Point : {point}"
            cible=create_cible()
            nb_tir_juste+=1
        elif cordo[0]-x<=10 and cordo[0]-x>=-10  and cordo[1]-y<=10 and cordo[1]-y>=-10 :
            graphic_zone.delete(cible)
            point+=100
            aff_point['text'] = f"Point : {point}"
            cible=create_cible()
            nb_tir_juste+=1
        elif cordo[0]-x<=40 and cordo[0]-x>=-40  and cordo[1]-y<=40 and cordo[1]-y>=-40 :
            graphic_zone.delete(cible)
            point+=50
            aff_point['text'] = f"Point : {point}"
            cible=create_cible()
            nb_tir_juste+=1
        else:
            vie-=1
            aff_vie['text'] = f"Vie : {vie}"
        test()
    else: 
        pass
    if start_time:
        time()
        start_time=False
        
def time():
    global timer,point,point_time
    if point !=0:
        if point_time:
            timer-=1
        aff_time['text'] = f"Temps : {timer}"
        root.after(1000,time)
    test()

def test():
    global cible,vie,stop,timer,point_time,point,nb_tir,nb_tir_juste,initial
    if vie ==0:
        graphic_zone.delete(cible)
        fin = Label(root, text="PERDU",font=("Courrier",50), fg="red",bg='#181818')
        fin.place(x=638,y=300) 
        score = Label(root, text=f"Vous avez un score de {point}\nUn ratio de {round((point/(initial-timer))/100,2)}\nUne précision de {int((nb_tir_juste/nb_tir)*100)}%",font=("Courrier",30), fg="red",bg='#181818')
        score.place(x=519,y=370) 
        stop=False
        point_time=False
    if timer<=0:
        graphic_zone.delete(cible)
        fin = Label(root, text="FINI",font=("Courrier",50), fg="red",bg='#181818')
        fin.place(x=688,y=300) 
        score = Label(root, text=f"Vous avez un score de {point}\nUn ratio de {round((point/(initial-timer))/100,2)}\nUne précision de {int((nb_tir_juste/nb_tir)*100)}%",font=("Courrier",30), fg="red",bg='#181818')
        score.place(x=519,y=370)
        stop=False
        point_time=False

color = "#282C34"
global vie,stop,timer,point_time,point,nb_tir,nb_tir_juste,start_time,initial
stop = True
initial=5
timer=initial
point=0
vie=5
start_time=True
point_time=True
nb_tir=0
nb_tir_juste=0
root=create_window()
graphic_zone=create_widgets()
backgroundr=create_background() 
# pointeur=create_pointeur()
cible=create_cible()
root.config(cursor="tcross")
# graphic_zone.bind("<Motion>",cordo)
graphic_zone.bind("<ButtonPress-1>",tir)

aff_vie = Label(root, text=f"Vie : {vie}",font=("Courrier",18), fg="red",bg='#181818')
aff_vie.place(x=1350,y=842)
aff_point = Label(root, text=f"Point : {point}",font=("Courrier",18), fg="red",bg='#181818')
aff_point.place(x=1350,y=815)
aff_time = Label(root, text=f"Temps : {timer}",font=("Courrier",18), fg="red",bg='#181818')
aff_time.place(x=1350,y=870)

root.mainloop()


