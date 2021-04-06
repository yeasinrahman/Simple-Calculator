from tkinter import *
win=Tk()
win.geometry('644x1000')




def click(event):
    global screen
    text=event.widget.cget('text')
  

    if text =='=':
        if screen.get().isdigit():

            value = int(screen.get())
        else:
            
            try:
                value = eval(screen1.get())

            except Exception as e:
                
                value = "Error" 

        
        screen.set(value)
        screen1.update()


    elif text=='C':
        screen.set('')
        screen1.update()


    else:
        screen.set(screen.get() + text)
        screen1.update()


Label(win,text='Calculator',font='lucida 35 bold',pady=8,bg='white').pack()

screen=StringVar()
screen.set('')
screen1=Entry(win,textvar=screen,font='lucida 35 bold',bg='black',fg='white')
screen1.pack(pady=8)

f=Frame(win,bg='orange')


b=Button(f,text='9', font='lucida 35 bold',pady=5,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)



b=Button(f,text='8', font='lucida 35 bold',pady=5,padx=4)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)


b=Button(f,text='7', font='lucida 35 bold',pady=5,padx=4)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)

b=Button(f,text='+', font='lucida 35 bold',pady=5,padx=3)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)




f.pack()

f=Frame(win,bg='orange')
b=Button(f,text='6', font='lucida 35 bold',pady=5,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)


b=Button(f,text='5', font='lucida 35 bold',pady=5,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)


b=Button(f,text='4', font='lucida 35 bold',pady=5,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)

b=Button(f,text='-', font='lucida 39 bold',pady=5,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)


f.pack()

f=Frame(win,bg='orange')
b=Button(f,text='3', font='lucida 35 bold',pady=5,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)


b=Button(f,text='2', font='lucida 35 bold',pady=5,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)


b=Button(f,text='1', font='lucida 35 bold',pady=5,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)


b=Button(f,text='*', font='lucida 37 bold',pady=5,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)



f.pack()




f=Frame(win,bg='orange')

b=Button(f,text='0', font='lucida 37 bold',pady=3,padx=6)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)

b=Button(f,text='/', font='lucida 35 bold',pady=5,padx=6)
b.pack(side=LEFT,padx=6,pady=5)
b.bind('<Button-1>',click)


b=Button(f,text='C', font='lucida 32 bold',pady=3,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)


b=Button(f,text='=', font='lucida 32 bold',pady=5,padx=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)

f.pack()

win['bg']='grey'
win.mainloop()
