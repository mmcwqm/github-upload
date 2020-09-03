from tkinter.colorchooser import askcolor
import tkinter as tk
 
def callback():
    result = askcolor(title = "Tkinter Color Chooser")
    label.configure(fg = result[1])
    print(result[1])
     
root = tk.Tk()
tk.Button(root, text='Choose Color',command=callback).pack(pady=20)
 
label = tk.Label(root, text = "Color", fg = "black")
label.pack()
 
root.geometry('180x160')
tk.mainloop()