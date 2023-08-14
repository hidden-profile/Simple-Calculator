from tkinter import *
m=Tk()
m.title('Calculator') 
m.configure(bg='black')
inp=Entry(m,width=25,font=('Arial',18),justify=RIGHT)
#inp.configure(bg='pink')
def clear():
    inp.delete(0,END)

def click(x):
    x1=inp.get()
    clear()
    y=x1+x 
    inp.insert(0,y)

first=0
symbol=''
li=['+','-','X','/']

def calc(sy):
    global first,symbol
    symbol=sy
    first=inp.get()
    for q in li:
        if q in first:
            first=first.replace(q,'')
    clear()
    inp.insert(0,first+symbol)

def equal():
    res=''
    global first,symbol
    second=inp.get().replace(str(first)+symbol,'')
    clear()
    if symbol=='+':
        res=int(first)+int(second)
    elif symbol=='-':
        res=int(first)-int(second)
    elif symbol=='X':
        res=int(first)*int(second)
    elif symbol=='/':
        res=int(first)/int(second)
    inp.insert(0,res)


    
b0=Button(m,text='0',padx=36,pady=10,command=lambda: click('0'),fg='white',bg='grey')
b1=Button(m,text='1',padx=36,pady=10,command=lambda: click('1'),fg='white',bg='grey')
b2=Button(m,text='2',padx=36,pady=10,command=lambda: click('2'),fg='white',bg='grey')
b3=Button(m,text='3',padx=36,pady=10,command=lambda: click('3'),fg='white',bg='grey')
b4=Button(m,text='4',padx=36,pady=10,command=lambda: click('4'),fg='white',bg='grey')
b5=Button(m,text='5',padx=36,pady=10,command=lambda: click('5'),fg='white',bg='grey')
b6=Button(m,text='6',padx=36,pady=10,command=lambda: click('6'),fg='white',bg='grey')
b7=Button(m,text='7',padx=36,pady=10,command=lambda: click('7'),fg='white',bg='grey')
b8=Button(m,text='8',padx=36,pady=10,command=lambda: click('8'),fg='white',bg='grey')
b9=Button(m,text='9',padx=36,pady=10,command=lambda: click('9'),fg='white',bg='grey')
eq=Button(m,text='=',padx=36,pady=10,command=equal,fg='white',bg='grey')
ac=Button(m,text='AC',padx=34,pady=10,command=clear,fg='white',bg='grey')
add=Button(m,text='+',padx=36,pady=10,command=lambda: calc('+'),fg='white',bg='grey')
sub=Button(m,text='-',padx=36,pady=10,command=lambda: calc('-'),fg='white',bg='grey')
mul=Button(m,text='X',padx=36,pady=10,command=lambda: calc('X'),fg='white',bg='grey')
div=Button(m,text='/',padx=36,pady=10,command=lambda: calc('/'),fg='white',bg='grey')

inp.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
b0.grid(row=4,column=0,padx=2,pady=2)
eq.grid(row=4,column=1,padx=2,pady=2)
ac.grid(row=4,column=2,padx=2,pady=2)
b1.grid(row=3,column=0,padx=2,pady=2)
b2.grid(row=3,column=1,padx=2,pady=2)
b3.grid(row=3,column=2,padx=2,pady=2)
b4.grid(row=2,column=0,padx=2,pady=2)
b5.grid(row=2,column=1,padx=2,pady=2)
b6.grid(row=2,column=2,padx=2,pady=2)
b7.grid(row=1,column=0,padx=2,pady=2)
b8.grid(row=1,column=1,padx=2,pady=2)
b9.grid(row=1,column=2,padx=2,pady=2)

add.grid(row=1,column=3,padx=2,pady=2)
sub.grid(row=2,column=3,padx=2,pady=2)
mul.grid(row=3,column=3,padx=2,pady=2)
div.grid(row=4,column=3,padx=2,pady=2)
m.mainloop()