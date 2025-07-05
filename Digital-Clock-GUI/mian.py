# Day 9 - Digital Clock GUI by Muhammad Qamar

from tkinter import *
from time import strftime

# Create window
root = Tk()
root.title("Digital Clock by Muhammad Qamar")
root.geometry("350x150")
root.resizable(False, False)
root.configure(bg='black')

# Clock label
label = Label(root, font=('Arial', 40), bg='black', fg='lime')
label.pack(anchor='center', pady=30)

# Update time every second
def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)  # call this function again after 1 sec

update_time()
root.mainloop()
