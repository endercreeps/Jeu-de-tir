from fonction import *

# ==========================================================================================================================================
# 
# Fenètre
# 
# ==========================================================================================================================================

def create_window():
    root=Tk()
    root.title("Jeu de tir")
    root.geometry("1500x922+170+45")
    root.minsize(1500,922)
    root.iconbitmap("pointeur_0.ico")
    root.config(background='#424242')
    #root.resizable(width=False,height=False)
    return root

# ==========================================================================================================================================
# 
# Canvas
# 
# ==========================================================================================================================================

def create_widgets():
    graphic_zone=Canvas(root,width=1499,height=921,bg=color,highlightthickness=0)
    graphic_zone.pack()
    return graphic_zone

# ==========================================================================================================================================
# 
# Background
# 
# ==========================================================================================================================================

def create_background():
    background=ImageTk.PhotoImage(Image.open("bgd.jpg"),master=root)
    background_o=graphic_zone.create_image(0,0,anchor='nw',image=background)
    return background

# ==========================================================================================================================================
# 
# Cible
# 
# ==========================================================================================================================================

def create_cible():
    global cible,cible_
    cible=ImageTk.PhotoImage(Image.open("cible_0.png"),master=root)
    cible_=graphic_zone.create_image(randint(60,1440),randint(80,620),anchor='center',image=cible)
    return cible

# ==========================================================================================================================================
# 
# Système de tir
# 
# ==========================================================================================================================================

def tir(event):
    x,y=event.x,event.y
    global cible,vie,stop,timer,point_time,point,nb_tir,nb_tir_juste,start_time
    if point_time:
        nb_tir+=1
    if stop:
        cordo=(graphic_zone.coords(cible_))
        if cordo[0]-x<=5 and cordo[0]-x>=-5 and cordo[1]-y<=5 and cordo[1]-y>=-5:
            graphic_zone.delete(cible)
            point+=130
            aff_point['text']=f"Point : {point}"
            cible=create_cible()
            nb_tir_juste+=1
        elif cordo[0]-x<=10 and cordo[0]-x>=-10 and cordo[1]-y<=10 and cordo[1]-y>=-10:
            graphic_zone.delete(cible)
            point+=100
            aff_point['text']=f"Point : {point}"
            cible=create_cible()
            nb_tir_juste+=1
        elif cordo[0]-x<=40 and cordo[0]-x>=-40 and cordo[1]-y<=40 and cordo[1]-y>=-40:
            graphic_zone.delete(cible)
            point+=50
            aff_point['text']=f"Point : {point}"
            cible=create_cible()
            nb_tir_juste+=1
        else:
            vie-=1
            aff_vie['text']=f"Vie : {vie}"
        verif_life()
    else: 
        pass
    if start_time:
        time()
        start_time=False

# ==========================================================================================================================================
# 
# Gestion temps
# 
# ==========================================================================================================================================
    
def time():
    global timer,point,point_time
    timer=int(timer)
    if point!=0:
        if point_time:
            timer-=1
        aff_time['text']=f"Temps : {timer}"
        root.after(1000,time)
    verif_life()

# ==========================================================================================================================================
# 
# Vérif temps+score / Fin du jeu
# 
# ==========================================================================================================================================

def verif_life():
    global cible,vie,stop,timer,point_time,point,nb_tir,nb_tir_juste,initial,name
    if vie==0:
        ratio=round((point/(int(initial)-int(timer)))/100,2)
        précision=int((nb_tir_juste/nb_tir)*100)
        graphic_zone.delete(cible)
        fin=Label(root,text="PERDU",font=("Courrier",50), fg="red",bg='#181818')
        fin.place(x=638,y=300) 
        score=Label(root, text=f"Vous avez un score de {point}\nUn ratio de {ratio}\nUne précision de {précision}%",font=("Courrier",30),fg="red",bg='#181818')
        score.place(x=519,y=370) 
        stop=False
        point_time=False

        conn=sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""INSERT INTO score(Name, Score, Ratio, Précision) VALUES(?, ?, ?, ?)""",(name,point,ratio,précision))
        conn.commit()
        conn.close()

    if int(timer)<=0:
        ratio=round((point/(int(initial)-int(timer)))/100,2)
        précision=int((nb_tir_juste/nb_tir)*100)
        graphic_zone.delete(cible)
        fin=Label(root,text="FINI",font=("Courrier",50), fg="red",bg='#181818')
        fin.place(x=688,y=300)
        score=Label(root,text=f"Vous avez un score de {point}\nUn ratio de {ratio}\nUne précision de {précision}%",font=("Courrier",30),fg="red",bg='#181818')
        score.place(x=519,y=370)
        stop=False
        point_time=False

        conn=sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""INSERT INTO score(Name, Score, Ratio, Précision) VALUES(?, ?, ?, ?)""",(name,point,ratio,précision))
        conn.commit()
        conn.close()

# ==========================================================================================================================================
# 
# Main : variable
# 
# ==========================================================================================================================================

global vie,stop,timer,point_time,point,nb_tir,nb_tir_juste,start_time,initial,name
stop=True
start_time=True
point_time=True
game=False
initial=30
timer=initial
point=0
vie=5
nb_tir=0
nb_tir_juste=0
name=""
color="#282C34"

# ==========================================================================================================================================
# 
# Main : fonction
# 
# ==========================================================================================================================================

root=create_window()
graphic_zone=create_widgets()
backgroundr=create_background()
cible=create_cible()
root.config(cursor="tcross")
root.withdraw()

# ==========================================================================================================================================
# 
# Toplevel
# 
# ==========================================================================================================================================

menu=Toplevel(root)
menu.title("Paramètre du jeu")
menu.geometry("320x485+770+300")
menu.minsize(320,485)
menu.iconbitmap("pointeur_0.ico")
menu.config(background='#424242')
menu.resizable(width=False,height=False)

# ==========================================================================================================================================
# 
# Check entry
# 
# ==========================================================================================================================================

def check():
    global name
    global initial
    global stop
    global timer
    initial=entry_time.get()
    name=entry_name.get()
    condition1=True
    condition2=True
    if len(initial)==0:
        entry_time.delete(0,END) 
        entry_time.insert(0,"Rentrer une valeur")
        condition1=True
    else:
        try:
            if int(initial)>30:
                entry_time.delete(0,END)
                entry_time.insert(0,"Rentrer une valeur")
                condition1=True
            if int(initial)<5:
                entry_time.delete(0,END)
                entry_time.insert(0,"Rentrer une valeur")
                condition1=True
            else:
                condition1=False
        except:
                entry_time.delete(0,END)
                entry_time.insert(0,"Rentrer une valeur")
                condition1=True
    if len(name)==0:
            entry_name.delete(0,END)
            entry_name.insert(0,"Rentrer une valeur")
            condition2=True
    else:
        condition2=False
    if condition1==False and condition2==False:
        stop=True
        menu.destroy()
        timer=initial
        aff_time['text']=f"Temps : {timer}"
        root.deiconify()

# ==========================================================================================================================================
# 
# Def entry
# 
# ==========================================================================================================================================

frame=Frame(menu,bg='#424242')

aff_temps=Label(frame, text="Choisissez le temps\nde jeu compris entre\n5 et 30 secondes",font=("Courrier",18), fg="white",bg='#424242')
aff_temps.pack(expand=YES)

entry_time=Entry(frame,font=("Courrier",18),bg='white', cursor=None)
entry_time.pack(expand=YES)

aff_name=Label(frame, text="Choisissez votre nom",font=("Courrier",18), fg="white",bg='#424242')
aff_name.pack(expand=YES)

entry_name=Entry(frame,font=("Courrier",18),bg='white', cursor=None)
entry_name.pack(expand=YES)

button=Button(frame,text="Entrer", font=("Courrier", 10), bg='white', fg='#424242', command=check)
button.pack(expand=YES)

frame.pack(expand=YES)

# ==========================================================================================================================================
# 
# Label
# 
# ==========================================================================================================================================

aff_vie=Label(root, text=f"Vie : {vie}",font=("Courrier",18), fg="red",bg='#181818')
aff_vie.place(x=1350,y=742)

aff_point=Label(root, text=f"Point : {point}",font=("Courrier",18), fg="red",bg='#181818')
aff_point.place(x=1350,y=715)

aff_time=Label(root, text=f"Temps : {timer}",font=("Courrier",18), fg="red",bg='#181818')
aff_time.place(x=1350,y=770)

# ==========================================================================================================================================
# 
# Loop + bind
# 
# ==========================================================================================================================================

graphic_zone.bind("<ButtonPress-1>",tir)

root.mainloop()