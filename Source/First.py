from tkinter import *

def FirstAlg(n):

    i=0
    newWindow=Tk()
    newWindow.title("Первый алгоритм")
    newWindow.iconbitmap("./Content/Image/icon.ico")


    listbox=Listbox(newWindow)
    listbox.pack()

    while i <= n:

        if (i ** 2 <= n):
            listbox.insert(END,i**2)
            i += 1

        if (i ** 2 > n):
            break
    newWindow.mainloop()