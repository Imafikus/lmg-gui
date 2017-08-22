from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.wm_title("Hello, world")
pomoc = Image.open("Pics/poligon1.jpg")
pomoc = pomoc.resize((800, 600), Image.LANCZOS)
img = ImageTk.PhotoImage(pomoc)
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
