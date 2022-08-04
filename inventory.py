from tkinter import *
from PIL import Image, ImageTk
from numpy import around
print ("Hello Aero club")
aero_root = Tk()
aero_root.title("AeroClubNitte_Inventory")
aero_root.geometry("700x450")
# min and max takes the parameter in width x height
aero_root.minsize(700,450)



#adding an image in the app only png format 
# image= PhotoImage(filename)

# for Jpg images importing the PILLOW library is necessary
image = Image.open("bg2.jpg")
photo = ImageTk.PhotoImage(image)

bg_lable = Label(image=photo)
bg_lable.pack()



aero_root.mainloop()

 