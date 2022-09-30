from First import *
from Func4 import *
from tkinter import *



window = Tk()
window.title("Алгоритмы")
window.iconbitmap("./Content/Image/icon.ico")

ButtonImage= PhotoImage(file='./Content/Image/ButtonImage.png')

MainFrame = Frame(
    window,
    padx=10,
    pady=10
    )
MainFrame.pack(expand=True)


entry = Entry(
    MainFrame
)
entry.grid(row=0, column=2)


testButton = Button(
    MainFrame,
    image=ButtonImage,
    borderwidth = 0
)

testButton.bind('<ButtonRelease-1>',
    lambda event: FirstAlg(int(entry.get())))

testButton.grid(row=0,column=1)


entry1 = Entry(
    MainFrame
)
entry1.grid(row=5, column=2)


testButton1 = Button(
   MainFrame,
    text="Test1"
)

testButton1.bind('<ButtonRelease-1>',
    lambda event: Task1(entry1.get()))

testButton1.grid(row=5,column=1)


testButton2 = Button(
   MainFrame,
    text="Пингвин"
)

testButton2.bind('<ButtonRelease-1>',
    lambda event: Task2())

testButton2.grid(row=6,column=1)

testButton3 = Button(
   MainFrame,
    text="Целочисленное деление"
)

entry2 = Entry(
    MainFrame
)
entry2.grid(row=7, column=2)
entry3 = Entry(
    MainFrame
)
entry3.grid(row=8, column=2)

testButton3.bind('<ButtonRelease-1>',
    lambda event: Task3(int(entry2.get()),int(entry3.get())))

testButton3.grid(row=7,column=1)



testButton4 = Button(
   MainFrame,
    text="Остаток от деления"
)

entry4 = Entry(
    MainFrame
)
entry4.grid(row=9, column=2)
entry5 = Entry(
    MainFrame
)
entry5.grid(row=10, column=2)

testButton4.bind('<ButtonRelease-1>',
    lambda event: Task4(int(entry4.get()),int(entry5.get())))

testButton4.grid(row=9,column=1)

testButton4 = Button(
   MainFrame,
    text="Остаток от деления"
)

entry4 = Entry(
    MainFrame
)
entry4.grid(row=9, column=2)
entry5 = Entry(
    MainFrame
)
entry5.grid(row=10, column=2)

testButton4.bind('<ButtonRelease-1>',
    lambda event: Task4(int(entry4.get()),int(entry5.get())))

testButton4.grid(row=9,column=1)




testButton5 = Button(
   MainFrame,
    text="Решение уравнения"
)

entry6 = Entry(
    MainFrame
)
entry6.grid(row=1, column=4)
entry7 = Entry(
    MainFrame
)
entry7.grid(row=2, column=4)
entry8 = Entry(
    MainFrame
)
entry8.grid(row=3, column=4)
entry9 = Entry(
    MainFrame
)
entry9.grid(row=4, column=4)

testButton5.bind('<ButtonRelease-1>',
    lambda event: Task5(float(entry6.get()),float(entry7.get()),float(entry8.get()),float(entry9.get())))

testButton5.grid(row=1,column=3)


testButton6 = Button(
   MainFrame,
    text="Возведение 2 в степень n"
)

entry10 = Entry(
    MainFrame
)

entry10.grid(row=5, column=4)
testButton6.bind('<ButtonRelease-1>',
    lambda event: Task6(float(entry10.get())))

testButton6.grid(row=5,column=3)


window.mainloop()