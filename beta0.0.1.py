
import tkinter.ttk as ttk
from tkinter import * #Tk,Label,Button,mainloop,Frame,Scrollbar,Entry
ws = None
firstTime = True
tree = None
ikuy = 1
name_var=None
passw_var=None

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
  global name_var,  passw_var
  ws.destroy()
  init()
  name_var=StringVar()
  passw_var=StringVar()
  '''Asset Code,Product ID,Warehouse,Location,Container #,Box #,PO Ref,Color,Size,Finish'''
  assetCode_label = Label(ws, text = 'Asset Code', font=('calibre',10, 'bold'))

  name_entry = Entry(ws,textvariable = name_var, font=('calibre',10,'normal'))
  
  assetCode_label = Label(ws, text = 'Product ID', font = ('calibre',10,'bold'))
  
  passw_entry=Entry(ws, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    
  name_label = Label(ws, text = 'Warehouse', font=('calibre',10, 'bold'))

  name_entry = Entry(ws,textvariable = name_var, font=('calibre',10,'normal'))
  
  passw_label = Label(ws, text = 'Location', font = ('calibre',10,'bold'))
  
  passw_entry=Entry(ws, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

  passw_label = Label(ws, text = 'Container #', font = ('calibre',10,'bold'))
  
  passw_entry=Entry(ws, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
  
  sub_btn=Button(ws,text = 'Submit', command = submitEdit)
  name_label.grid(row=0,column=0)
  name_entry.grid(row=0,column=1)
  passw_label.grid(row=1,column=0)
  passw_entry.grid(row=1,column=1)
  sub_btn.grid(row=2,column=1)

  
  
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