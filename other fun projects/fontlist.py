import tkinter as tk
from tkinter import *
from tkinter import font
# Create window Tkinter
window = tk.Tk()
# Name our Tkinter application title
window.title("Font List ")
# Define window size in Tkinter python
window.geometry("700x500")
root = Tk()
root.title('Font Families')
fonts=list(font.families())
fonts.sort()
label = tk.Label(window, text="List Of Fonts Are In Next Window", fg="white", bg="black",font=('Calibri 15 bold'))
label.pack(pady=20)
def populate(frame):
    '''Put in the fonts'''
    listnumber = 1
    for item in fonts:
        label = "listlabel" + str(listnumber)
        label = Label(frame,text=item,font=(item, 16)).pack()
        listnumber += 1

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()
