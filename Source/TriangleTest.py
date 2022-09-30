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
start.grid(row=1,column=1)

entryX1 = Entry(
    root,width=10
)
entryX1.grid(row=1, column=4)

textX1 = Text(
    root,
    width=2,
    height=1
)
textX1.grid(row=1,column=3)
textX1.insert(0.0,"X1")

entryX2 = Entry(
    root,width=10
)
entryX2.grid(row=2, column=4)

textX2 = Text(
    root,
    width=2,
    height=1
)
textX2.grid(row=2,column=3)
textX2.insert(0.0,"X2")

entryY1 = Entry(
    root,width=10
)
entryY1.grid(row=3, column=4)

textY1 = Text(
    root,
    width=2,
    height=1
)
textY1.grid(row=3,column=3)
textY1.insert(0.0,"Y1")

entryY2 = Entry(
    root,width=10
)
entryY2.grid(row=4, column=4)

textY2 = Text(
    root,
    width=2,
    height=1
)
textY2.grid(row=4,column=3)
textY2.insert(0.0,"Y2")

textZ1 = Text(
    root,
    width=2,
    height=1
)
textZ1.grid(row=5,column=3)
textZ1.insert(0.0,"Z1")

entryZ1 = Entry(
    root,width=10
)
entryZ1.grid(row=5, column=4)

textZ2 = Text(
    root,
    width=2,
    height=1
)
textZ2.grid(row=6,column=3)
textZ2.insert(0.0,"Z2")
entryZ2 = Entry(
    root,width=10
)
entryZ2.grid(row=6, column=4)





start.bind('<ButtonRelease-1>',
    lambda event:messagebox.showerror(title="Ошибка",message="Нет данных") if not (len(entryX1.get())and len(entryX2.get())and len(entryY1.get())and len(entryY2.get())and len(entryZ1.get())and len(entryZ2.get())) else
    polygonCreate(float(entryX1.get()),float(entryX2.get()),float(entryY1.get()),float(entryY2.get()),float(entryZ1.get()),float(entryZ2.get())))

def polygonCreate(x1,x2,y1,y2,z1,z2):
    polyWindow = Tk()

    canvas = Canvas(
        polyWindow, width=500,height=500
    )
    canvas.pack()

    canvas.create_polygon((x1,x2),(y1,y2),(z1,z2))
    polyWindow.mainloop()

root.mainloop()