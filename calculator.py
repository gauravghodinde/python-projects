from tkinter import*
win=Tk()
display=Frame(win,width=300,height=100)

display1=Label(display,text='0',bg='red',fg='yellow')

display.grid()
display.pack()
dis=Frame(win,width=300,height=300)

dis.pack()
win.mainloop()
