from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x233")
root.title("slider")
def getDollar():
    tmsg.showinfo("Ammount Credited:",f"The {mySlider.get()} ammount has been credited to your account")
Label(root,text="How many dollars is required").pack()
mySlider = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)#default is vertical
mySlider.pack()
Button(root, text="Get dollars!", command=getDollar).pack()

root.mainloop()