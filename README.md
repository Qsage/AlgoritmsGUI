# AlgoritmsGUI

# Пимер функции, получающей на вход число и возвращающей список

    def name(n):
      i=0
      newWindow=Tk() #создание окна для списка
      newWindow.title("Название окна") #Присваивание подписи
      newWindow.iconbitmap("./Content/Image/icon.ico") #Не менять

      listbox=Listbox(newWindow) #Создание списка и закрепление его к окну newWindow
      listbox.pack() #Запаковка списка

      while i <= n:
          if (i ** 2 <= n):
              listbox.insert(END,i**2) #Добавление значения i**2 в конец списка
              i += 1

          if (i ** 2 > n):
              break
      newWindow.mainloop() #Установка окна newWindow как основного


# Пимер функции, получающей на вход два числа и возвращающей текст
    
    def name(k,n):

      root = Tk() #Желательно использовать название root для окон функции
      root.title("Алгоритм 4.4")
      text = Text(root, width=25, height=5, wrap=WORD) #Создание текстового блока, в окне root
      if(k<n):
          text.insert(1.0, "Первое число, меньше второго") #Запись результата в текстовый блок, на позицию первого символа
      else:
          text.insert(1.0, k%n)

      text.pack()
      root.iconbitmap("./Content/Image/icon.ico")
      root.mainloop()
 
 
# Все алгоритмы разбиты на файлы, в соотвествие с номером задания и поключаются в main.py следующим образом:
    from FileName import *
# Так же все файлы лежат в папке Source
# В начале каждого такого файла должнабыть строчка:
    from tkinter import *


# Пример создания кнопкки и формы ввода:
   
       entry = Entry(       #Создаем форму ввода под название entry и крепим к окну MainFrame(основное окно)
        MainFrame
    )
    entry.grid(row=0, column=2) #Назначаем положение в первой строке, втором столбце


    testButton = Button(    #Создаем кнопку под название testButton и крепим к окну MainFrame(основное окно)
        MainFrame,
        image=ButtonImage,      #Назанчаем изображение для кнопки(не используется, в место этого, пишется text="Название кнопки")
        borderwidth = 0         #Выключаем обводку(не используется)
    )

    testButton.bind('<ButtonRelease-1>',        #Считываем нажатие кнопки testButton
        lambda event: FirstAlg(int(entry.get())))   #Вызываем функию FirstAlg(преобразованное в int значение из поля ввода entry)

    testButton.grid(row=0,column=1) #Назначаем положение в первой строке, первом столбце
