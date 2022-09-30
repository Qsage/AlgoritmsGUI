from tkinter import *


def Task1(name):
    root = Tk()
    text=Text(root,width=25, height=5)
    s=name
    text.insert(0.0,"Hello ")
    text.insert(6.0,s)
    text.insert(float(len(name)), "!")
    text.pack()
    root.iconbitmap("./Content/Image/icon.ico")
    root.mainloop()


def Task2():
    root = Tk()

    listbox=Listbox(root)
    listbox.pack()

    listbox.insert(END,'    _~_    ')
    listbox.insert(END,'   (o o)   ')
    listbox.insert(END,'  /  V  \  ')
    listbox.insert(END,' /(  _  )\ ')
    listbox.insert(END,'   ^^ ^^   ')


    root.iconbitmap("./Content/Image/icon.ico")
    root.mainloop()


def Task3(k,n):
    root = Tk()
    text = Text(root, width=25, height=5)


    text.insert(1.0, k//n)

    text.pack()
    root.iconbitmap("./Content/Image/icon.ico")
    root.mainloop()

def Task4(k,n):

    root = Tk()
    root.title("Алгоритм 4.4")
    text = Text(root, width=25, height=5, wrap=WORD)
    if(k<n):
        text.insert(1.0, "Первое число, меньше второго")
    else:
        text.insert(1.0, k%n)

    text.pack()
    root.iconbitmap("./Content/Image/icon.ico")
    root.mainloop()

def Task5(a,b,c,d):
    root = Tk()
    listbox=Listbox(root)

    t = (b + d) // 100
    x = (b + d) % 100
    print(a + c + t, '', x)

    listbox.insert(END, a+c+t)
    listbox.insert(END, x)

    listbox.pack()

    root.iconbitmap("./Content/Image/icon.ico")
    root.mainloop()

def Task6(n):
    root = Tk()
    root.title("Алгоритм 4.6")
    text = Text(root, width=25, height=5, wrap=WORD)

    text.insert(1.0,2 ** n)
    text.pack()
    root.iconbitmap("./Content/Image/icon.ico")
    root.mainloop()