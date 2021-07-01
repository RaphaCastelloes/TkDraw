import tkinter as tk
from tkinter.constants import BOTTOM, LEFT
#from pynput.mouse import Listener

toDraw = False

def myfunction(event):
    if toDraw == True:
        x, y = event.x, event.y
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)
        canvas.old_coords = x, y
        
def on_click(event):
    global toDraw 
    x, y = event.x, event.y
    canvas.old_coords = x, y
    toDraw = True

def on_release(event):
    global toDraw 
    toDraw = False

def clean():
    canvas.delete('all')

def resize():
    if root.attributes("-zoomed") == False:
        print (root.attributes("-zoomed"))
        root.attributes("-zoomed",True)
    else:
        print (root.attributes("-zoomed"))
        root.attributes("-zoomed",False)

root = tk.Tk()
root.geometry('136x80')

buttonHide = tk.Button(root, text="Resize", command=resize)
buttonHide.pack(side="left")
buttonClean = tk.Button(root, text="Clean", command=clean)
buttonClean.pack(side="left")


canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)
#canvas.grid(row=0,column=2)
canvas.old_coords = None

root.bind('<Button-1>', on_click)
root.bind('<ButtonRelease-1>', on_release)
root.bind('<Motion>', myfunction)

root.wait_visibility(root)
root.wm_attributes('-alpha',0.25)
root.wm_attributes("-topmost", True)

root.mainloop()