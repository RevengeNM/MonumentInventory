import tkinter
import tkinter.ttk as ttk
from tkinter import Tk,Label,Button,mainloop,Frame,Scrollbar
ws = None

def viewInv():
  ws.destroy()
  init()
  btn1 = Button(ws, text ="Back", command = home)
  btn2 = Button(ws, text ="Edit", command = edit)
  btn1.pack(x=50,y=20)
  btn2.place(x=70,y=20)
  btn1.pack()
  btn2.pack()
  TableMargin = Frame(ws, width=300)
  TableMargin.pack(side="top")
  scrollbarx = Scrollbar(TableMargin, orient='horizontal')
  scrollbary = Scrollbar(TableMargin, orient='vertical')
  
  tree = ttk.Treeview(TableMargin, columns=("a", "b", "c","d","e","f","g","h","i","j"), height=200, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  scrollbary.config(command=tree.yview)
  scrollbary.pack(side='right', fill='y')
  scrollbarx.config(command=tree.xview)
  scrollbarx.pack(side='bottom', fill='x')
  #Asset Code,Product ID,Warehouse,Location,Container #,Box #,PO Ref,Color,Size,Finish
  tree.heading('a', text="Asset Code", anchor='w')
  tree.heading('b', text="Product ID", anchor='w')
  tree.heading('c', text="Warehouse", anchor='w')
  tree.heading('d', text="Location", anchor='w')
  tree.heading('e', text="Container#", anchor='w')
  tree.heading('f', text="Box#", anchor='w')
  tree.heading('g', text="PO Ref", anchor='w')
  tree.heading('h', text="Color", anchor='w')
  tree.heading('i', text="Size", anchor='w')
  tree.heading('j',text="Finish", anchor='w')
  
  
  tree.column('#0',stretch='no', minwidth=0, width=0)
  tree.column('#1',stretch='no', minwidth=0, width=200)
  tree.column('#2',stretch='no', minwidth=0, width=200)
  tree.column('#3',stretch='no', minwidth=0, width=300)
  tree.pack()

  f = open("Inv.csv")
  read = f.readlines()
  for r in range(len(read)-1):
    tree.insert("",r,values=(read[r+1].split(',')))

def edit():
  pass
  

def home():
  init()
  hello = Label(ws,text="Inventory")
  hello.pack()
  button1 = Button(ws,text="Add")
  button1.place(x=150,y=30)
  #button1.pack(side = "top",padx=30,pady=30,ipadx=9,ipady=20,expand=True)
  button2 = Button(ws,text="View Inv",command=viewInv)
  button2.place(x=30,y=30)
  #button2.pack(side = "right",padx=30,pady=30,ipadx=9,ipady=20,expand=True)
  button3 = Button(ws,text="Edit",command=edit)
  button3.place(x=250,y=30)



print("this is")
#window = tkinter.Tk()
def init():
  global ws
  ws = Tk()
  ws.title("Inventory")
  ws.geometry("400x300+10+10")
home()


mainloop()
