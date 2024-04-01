from tkinter import *
import tkinter as tk
import pyautogui

gui=pyautogui

window=Tk()
window.geometry('400x500')

def bn1():
    gui.press('1')

def bn2():
    gui.press('2')

def bn3():
    gui.press('3')

def bn4():
    gui.press('+')

def bn5():
    gui.press('4')

def bn6():
    gui.press('5')
def bn7():
    gui.press('6')

def bn8():
    gui.press('*')

def bn9():
    gui.press('7')

def bn10():
    gui.press('8')

def bn11():
    gui.press('9')

def bn12():
    gui.press('-')
    
def bn13():
    gui.press('0')
def bn14():
    gui.press('.')
def bn15():
    gui.press('/')
def bn16():
    val=entry.get()
    cal=eval(val)

    entry.delete(0,tk.END)
    entry.insert(0,cal)
   


label=Label(window,text='hI HOW')

entry=Entry(window,width=60)



btn1=Button(window,text='1',width=6,height=2,command=bn1)
btn2=Button(window,text='2',width=6,height=2,command=bn2)
btn3=Button(window,text='3',width=6,height=2,command=bn3)
btn4=Button(window,text='+',width=6,height=2,command=bn4)

btn5=Button(window,text='4',width=6,height=2,command=bn5)
btn6=Button(window,text='5',width=6,height=2,command=bn6)
btn7=Button(window,text='6',width=6,height=2,command=bn7)
btn8=Button(window,text='*',width=6,height=2,command=bn8)

btn9=Button(window,text='7',width=6,height=2,command=bn9)
btn10=Button(window,text='8',width=6,height=2,command=bn10)
btn11=Button(window,text='9',width=6,height=2,command=bn11)
btn12=Button(window,text='-',width=6,height=2,command=bn12)

btn13=Button(window,text='0',width=6,height=2,command=bn13)
btn14=Button(window,text='.',width=6,height=2,command=bn14)
btn15=Button(window,text='/',width=6,height=2,command=bn15)
btn16=Button(window,text='=',width=6,height=2,command=bn16)


btn1.place(x=40,y=100)
btn2.place(x=130,y=100)
btn3.place(x=220,y=100)
btn4.place(x=310,y=100)

btn5.place(x=40,y=190)
btn6.place(x=130,y=190)
btn7.place(x=220,y=190)
btn8.place(x=310,y=190)

btn9.place(x=40,y=280)
btn10.place(x=130,y=280)
btn11.place(x=220,y=280)
btn12.place(x=310,y=280)

btn13.place(x=40,y=370)
btn14.place(x=130,y=370)
btn15.place(x=220,y=370)
btn16.place(x=310,y=370)

entry.place(x=20,y=10)






window.mainloop()

entry.pack()

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

btn5.pack()
btn6.pack()
btn7.pack()
btn8.pack()


btn9.pack()
btn10.pack()
btn11.pack()
btn12.pack()

btn13.pack()
btn14.pack()
btn15.pack()
btn16.pack()



