import tkinter.ttk as ttk
import tkinter as tk
from tkinter import * #Tk,Label,Button,mainloop,Frame,Scrollbar,Entry
ws = None
firstTime = True
tree = None
ikuy = 1
AC_var=None
PID_var=None
WH_var=None
lOC_var=None
CONNUM_var=None
BOXNUM_var=None
POREF_var=None
Colour_var=None
SIZE_var=None
FIN_var=None

def editItems():
  x = ""
  itemNo = tree.selection()[0]
  tree.item(itemNo,values=(100001, 'U104', 'ELB', 'E6', 'G21012', 58, 57983, 'PJB', '24x12x4', 'P2BRP'))
  ffej = tree.item(itemNo)
  print(itemNo)
  add(itemNo)
  '''
  for ikuy in range(1000000000000000000000000000000000000000000000000000):
      print(itemNo.index(ikuy))
      x = itemNo.index(ikuy)
      if x != ValueError:
          global reeeeeee
          reeeeeee = ikuy
  ii = list(ffej.values())
  print(ii[2])
  '''

def deleteItems():
   # Get selected item to Delete
   selected_item = tree.selection()[0]
   tree.delete(selected_item)
  
def viewInv():
  global tree
  ws.destroy()
  init()
  btn1 = Button(ws, text ="Back", command = home)
  #btn1.pack(pady = 10)
  btn1.place(x=30,y=30)
  
  btn2 = Button(ws, text ="Edit", command = editItems)
  btn2.pack(side="left",padx = 10)

  btn2 = Button(ws, text ="Delete", command = deleteItems)
  btn2.pack(side="left",padx = 10)
  
  TableMargin = Frame(ws, width=300)
  TableMargin.pack(side="left")
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

def add(itemNo):
  global AC_var,  PID_var,WH_var,lOC_var,CONNUM_var,BOXNUM_var,POREF_var,Colour_var,SIZE_var,FIN_var
  
  ws.destroy()
  init()
  
  AC_var=tk.StringVar()
  PID_var=tk.StringVar()
  WH_var=tk.StringVar()
  lOC_var=tk.StringVar()
  CONNUM_var=tk.StringVar()
  BOXNUM_var=tk.StringVar()
  POREF_var=tk.StringVar()
  Colour_var=tk.StringVar()
  SIZE_var=tk.StringVar()
  FIN_var=tk.StringVar()
  '''Asset Code,Product ID,Warehouse,Location,Container #,Box #,PO Ref,Color,Size,Finish'''
  AC_label = tk.Label(ws, text = 'Asset Code', font=('calibre',10, 'bold'))
  
  AC_var = tk.Entry(ws,textvariable = AC_var, font=('calibre',10,'normal'))
  
  PID_label = tk.Label(ws, text = 'Product ID', font=('calibre',10, 'bold'))
  
  PID_var = tk.Entry(ws,textvariable = PID_var, font=('calibre',10,'normal'))
  
  WH_label = tk.Label(ws, text = 'WareHouse', font = ('calibre',10,'bold'))
  
  WH_var=tk.Entry(ws, textvariable = WH_var, font = ('calibre',10,'normal'))
  
  LOC_label = tk.Label(ws, text = 'Location', font=('calibre',10, 'bold'))
  
  lOC_var = tk.Entry(ws,textvariable = lOC_var, font=('calibre',10,'normal'))
  
  CONNUM_label = tk.Label(ws, text = 'Container #', font=('calibre',10, 'bold'))
  
  CONNUM_var = tk.Entry(ws,textvariable = CONNUM_var, font=('calibre',10,'normal'))
  
  BOXNUM_label = tk.Label(ws, text = 'Box #', font=('calibre',10, 'bold'))
  
  BOXNUM_var = tk.Entry(ws,textvariable = BOXNUM_var, font=('calibre',10,'normal'))
  
  POREF_label = tk.Label(ws, text = 'PO Reference', font=('calibre',10, 'bold'))
  
  POREF_var = tk.Entry(ws,textvariable = POREF_var, font=('calibre',10,'normal'))
  
  Colour_label = tk.Label(ws, text = 'Colour', font=('calibre',10, 'bold'))
  
  Colour_var = tk.Entry(ws,textvariable = Colour_var, font=('calibre',10,'normal'))
  
  SIZE_label = tk.Label(ws, text = 'Size', font=('calibre',10, 'bold'))
  
  SIZE_var = tk.Entry(ws,textvariable = SIZE_var, font=('calibre',10,'normal'))
  
  FIN_label = tk.Label(ws, text = 'Finish', font=('calibre',10, 'bold'))
  
  FIN_var = tk.Entry(ws,textvariable = FIN_var, font=('calibre',10,'normal'))
  
  sub_btn=Button(ws,text = 'Submit', command = submitEdit)
  #clear_btn=Button(ws,text = 'Submit', command = submitEdit)

  AC_label.grid(row=1,column=0)
  AC_var.grid(row=1,column=1)
  PID_label.grid(row=2,column=0)
  PID_var.grid(row=2,column=1)
  WH_label.grid(row=3,column=0)
  WH_var.grid(row=3,column=1)
  LOC_label.grid(row=4,column=0)
  lOC_var.grid(row=4,column=1)
  CONNUM_label.grid(row=5,column=0)
  CONNUM_var.grid(row=5,column=1)
  BOXNUM_label.grid(row=6,column=0)
  BOXNUM_var.grid(row=6,column=1)
  POREF_label.grid(row=7,column=0)
  POREF_var.grid(row=7,column=1)
  Colour_label.grid(row=8,column=0)
  Colour_var.grid(row=8,column=1)
  SIZE_label.grid(row=9,column=0)
  SIZE_var.grid(row=9,column=1)
  FIN_label.grid(row=10,column=0)
  FIN_var.grid(row=10,column=1)
  
  sub_btn.grid(row=11,column=1)
  clear_btn.grid(row=12,column=1)

  
  
def home():
  global firstTime
  if not firstTime:
    ws.destroy()
  firstTime = False
  init()
  
  hello = Label(ws,text="Inventory")
  hello.pack()
  #button1 = Button(ws,text="Add",command=add)
  #button1.place(x=150,y=30)
  #button1.pack(side = "top",padx=30,pady=30,ipadx=9,ipady=20,expand=True)
  button2 = Button(ws,text="View Inv",command=viewInv)
  #button2.place(x=30,y=30)
  button2.pack(side = "right",padx=30,pady=30,ipadx=9,ipady=20,expand=True)
  
def init():
  global ws
  ws = Tk()
  ws.title("Inventory")
  ws.geometry("400x300+10+10")

def submitEdit():
  name=name_var.get()
  password=passw_var.get()
  print("The name is : " + name)
  print("The password is : " + password)
  name_var.set("")
  passw_var.set("")
  home()
  

home()
mainloop()
