from tkinter import *
root=Tk()
root.geometry("500x400+200+100")

#adding title
root.title("SUUUUUUUUU")

#adding label 
l1=Label(root,text="hello there")
l1.grid(column=0, row=0)

#def function
def clicked():
    l1.configure(text="Button clicked")

#button and other stuff
bt=Button(root,text="Enter",command=clicked,font="vardana",bg="orange",fg="blue")
bt.grid(column=1,row=0)

# bt.grid(column=1, row=0)



root.mainloop()