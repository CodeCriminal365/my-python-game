# ---------Full code to create a software application with python ---------------
# Import library(s)
import tkinter as tk
# Create window Tkinter
window = tk.Tk()
# Name our Tkinter application title
window.title(" Which Button??? ")
# Define window size in Tkinter python
window.geometry("700x500")
# Create a label widget in Tkinter
label = tk.Label(window, text="Which Button???", fg="white", bg="black",
font=('Impact 15'))
label.pack(pady=20)
# Function to update the label text for first button click in Tkinter
def on_click_btn1():
    label["text"] = "You clicked the first button"  
# Function to update the label text for second button click in Tkinter
def on_click_btn2():
    label["text"] = "You clicked the second button"
def on_click_btn3():
    label["text"] = "You clicked the third button"
def on_click_secret():
    label["text"] = "You Found It!"
def on_click_glitch():
    label["text"] = "You Lose"
def on_click_reset():
    label["text"] = "Which Button???"
# Create 1st button to update the label widget
btn1 = tk.Button(window, text="The First Button", command=on_click_btn1, fg="black", bg="yellow",font=('YaHei'))
btn1.pack(pady=20)
# Create 2nd button to update the label widget
btn2 = tk.Button(window, text="The Second Button", command=on_click_btn2, fg="black", bg="yellow",font=('YaHei'))
btn2.pack(pady=20)
btn3 = tk.Button(window, text="The Third Button", command=on_click_btn3, fg="black", bg="yellow",font=('YaHei'))
btn3.pack(pady=20)
secret = tk.Button(window, text="????????", command=on_click_secret, fg="black", bg="yellow",font=('YaHei'))
secret.pack(pady=20)
glitch = tk.Button(window, text="????????", command=on_click_glitch, fg="black", bg="yellow",font=('YaHei'))
glitch.pack(pady=20)
reset = tk.Button(window, text="Reset", command=on_click_reset, fg="black", bg="yellow",font=('YaHei'))
reset.pack(pady=20)
# Run main loop
window.mainloop()
