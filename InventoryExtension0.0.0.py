import tkinter
import tkinter.ttk as ttk
from tkinter import Tk,Label,Button,mainloop,Frame,Scrollbar


def viewInv():
    TableMargin = Frame(window, width=500)
    TableMargin.pack(side="top")
    scrollbarx = Scrollbar(TableMargin, orient='horizontal')
    scrollbary = Scrollbar(TableMargin, orient='vertical')
    tree = ttk.Treeview(TableMargin, columns=("Firstname", "Lastname", "Address"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side='right', fill='y')
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side='bottom', fill='x')
    tree.heading('Firstname', text="Firstname", anchor='w')
    tree.heading('Lastname', text="Lastname", anchor='w')
    tree.heading('Address', text="Address", anchor='w')
    tree.column('#0', stretch='no', minwidth=0, width=0)
    tree.column('#1', stretch='no', minwidth=0, width=200)
    tree.column('#2', stretch='no', minwidth=0, width=200)
    tree.column('#3', stretch='no', minwidth=0, width=300)
    tree.pack()

  
print("this is")
#window = tkinter.Tk()
window = Tk()
window.title("Hello wold")
window.geometry("400x300")

hello = Label(text="Inventory")
hello.pack()
button1 = Button(text="Add",command=viewInv)
button1.pack(side = "top",padx=30,pady=30,ipadx=9,ipady=20,expand=True)
button2 = Button(text="View Inv")
#button.place(x=50,y=30)
button2.pack(side = "right",padx=30,pady=30,ipadx=9,ipady=20,expand=True)




mainloop()
