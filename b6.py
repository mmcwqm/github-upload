from tkinter import *
 
root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack(side=LEFT)
 
MenuBttn0 = Menubutton(frame, text = "Favourite food", relief = RAISED)
 
Var1 = IntVar()
 
Menu0 = Menu(MenuBttn0, tearoff = 0)
 
Menu0.add_radiobutton(label = "Pizza", variable = Var1, value = 1)
Menu0.add_radiobutton(label = "Cheese Burger", variable = Var1, value = 2)
Menu0.add_radiobutton(label = "Salad", variable = Var1, value = 3)
 
MenuBttn0["menu"] = Menu0
 
MenuBttn0.pack()

 
frame1 = Frame(root)
frame1.pack(side=RIGHT)
 
MenuBttn1 = Menubutton(frame1, text = "Favourite food", relief = RAISED)
 
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
 
Menu1 = Menu(MenuBttn1, tearoff = 0)
 
Menu1.add_checkbutton(label = "Pizza", variable = Var1)
Menu1.add_checkbutton(label = "Cheese Burger", variable = Var2)
Menu1.add_checkbutton(label = "Salad", variable = Var3)
 
MenuBttn1["menu"] = Menu1
 
MenuBttn1.pack()

root.mainloop()