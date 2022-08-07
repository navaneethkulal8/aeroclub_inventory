from tkinter import *
from PIL import Image, ImageTk
from numpy import around
print ("Hello Aero club")
aero_root = Tk()
aero_root.title("AeroClubNitte_Inventory")
aero_root.geometry("700x450")
# min and max takes the parameter in width x height
aero_root.minsize(700,450)
def hello():
    print("hello navaneeth s kumar")



#adding an image in the app only png format 
# image= PhotoImage(filename)

# # for Jpg images importing the PILLOW library is necessary
# image = Image.open("bg2.jpg")
# photo = ImageTk.PhotoImage(image)

# bg_lable = Label(image=photo)
# bg_lable.pack()
################################ button tutorial ###################################
# frame= Frame(aero_root, borderwidth=6, bg="grey",relief=SUNKEN)
# frame.pack(side=LEFT,anchor="nw")

# b1 = Button(frame, fg="red",text="print now",command=hello)
# b1.pack(side=LEFT,padx=23)

# b2 = Button(frame, fg="red",text="print now",command=hello)
# b2.pack(side=LEFT,padx=23)
# b3 = Button(frame, fg="red",text="print now",command=hello)
# b3.pack(side=LEFT,padx=23)
# b4 = Button(frame, fg="red",text="print now",command=hello)
# b4.pack(side=LEFT,padx=23)
######################################################################################



aero_root.mainloop()

 