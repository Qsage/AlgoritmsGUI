import math
from tkinter import *

from tkinter import messagebox

rootWindow = Tk()

rootWindow.title("Треугольники")
rootWindow.iconbitmap("./Content/Image/icon.ico")

root = Frame(
    rootWindow
)
root.pack(expand=True)

start = Button(
    root,
    text="Расчитать"
)


entryA = Entry(
    root,width=10
)
entryA.grid(row=1, column=4)

textA = Text(
    root,
    width=17,
    height=1
)
textA.grid(row=1,column=3)
textA.insert(0.0,"Длинна стороны A")

entryB = Entry(
    root,width=10
)
entryB.grid(row=2, column=4)

textB = Text(
    root,
    width=17,
    height=1
)
textB.grid(row=2,column=3)
textB.insert(0.0,"Длинна стороны B")

entryC = Entry(
    root,width=10
)
entryC.grid(row=3, column=4)

textC = Text(
    root,
    width=17,
    height=1
)

textC.grid(row=3,column=3)
textC.insert(0.0,"Длинна стороны C")

start.bind('<ButtonRelease-1>',
    lambda event:messagebox.showerror(title="Ошибка",message="Нет данных") if not (len(entryA.get())and len(entryB.get()) and len(entryB.get())) else polygonCreate(10,10,10+int(entryB.get()),10,getCoordinateCY(int(entryA.get()),int(entryB.get()),int(entryC.get())),getCoordinateCX(int(entryA.get()),int(entryB.get()),int(entryC.get()))))

start.bind('<Button>',lambda event:getTypeTiangle(int(entryA.get()),int(entryB.get()),int(entryC.get())),'+')

start.grid(row=1,column=1)


def getCoordinateCX(a, b, c):
    cosA = (b*b+c*c-a*a)/(2*b*c)
    cx1 = b*cosA
    cx =int(round(cx1,1))
    print(cx)

    return cx


def getCoordinateCY(a, b, c):
    cosA = (b*b+c*c-a*a)/(2*b*c)
    cy1 = b * math.sqrt(1-cosA*cosA)

    cy = int(round(cy1,1))
    print(cy)

    return cy


#print(getCoordinateCX(37,58,70))


def polygonCreate(ax,ay,bx,by,cx,cy):
    polyWindow = Tk()

    canvas = Canvas(
        polyWindow, width=500,height=500
    )
    canvas.pack()


    canvas.create_polygon(ax,ay,bx,by,cx,cy, fill='green')
    polyWindow.mainloop()



def getTypeTiangle(a,b,c):

    if (a + b > c) and (c + b > a) and (a + c > b):
        if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
            messagebox.showinfo(title="Тип треугольника", message="Прямоугольный")
        elif (a * a + b * b > c * c) or (a * a + c * c > b * b) or (c * c + b * b > a * a):
            messagebox.showinfo(title="Тип треугольника", message="Остроугольный")
        elif (a * a + b * b < c * c) or (a * a + c * c < b * b) or (c * c + b * b < a * a):
            messagebox.showinfo(title="Тип треугольника", message="Тупоугольный")
    else:
        messagebox.showerror(title="Тип треугольника", message="Треугольник невозможен")

root.mainloop()