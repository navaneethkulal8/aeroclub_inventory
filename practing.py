from cProfile import label
from tkinter import *
root= Tk()
root.title("navi")

def myfunc():
    print("print navaneeth")

# my_menu = Menu(root)
# my_menu.add_command(lable="file",command=myfunc)
# my_menu.add_command(label="exit",command=quit)
# root.config(menu=my_menu)

filemenu = Menu(root)
m1 = Menu(filemenu,tearoff=0) #tearoff is the removeable  widget thing
m1.add_command(label="save",command=myfunc)
m1.add_command(label="save as",command=myfunc)
m1.add_separator() # line bw the options
m1.add_command(label="navi",command=myfunc)
m1.add_command(label="print",command=myfunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="file",menu=m1)


root.mainloop()