from tkinter import *
 
root = Tk()
root.geometry('500x500')
 
for x in range(10):
    for y in range(6):
         entry = Entry(root, width = 8)
         entry.grid(row = x, column = y)
 
root.mainloop()