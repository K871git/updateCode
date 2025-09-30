from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("combobox")
root.geometry("200x100+50+30")

# combo=Combobox(root)
# combo['values']=(1,2,5,6,"hello","suuuu")
# combo.current(2)
# combo.grid(column=0,row=1)

chk=BooleanVar()
chk.set(True)
chk=Checkbutton(root,text="Select", var=chk)
chk.grid(column=2,row=1)
root.mainloop()


