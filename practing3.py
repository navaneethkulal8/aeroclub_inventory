from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("Scrollbar tutorial")
# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)
listbox = Listbox(root,yscrollcommand= scrollbar.set)
for i in range (233):
    listbox.insert(END,f"Item{i}")
listbox.pack()    
scrollbar.config(command=listbox.yview)
root.mainloop()