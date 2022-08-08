from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("status bar")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor='w')
sbar.pack(side=BOTTOM,fill=X)
root.mainloop()