import tkinter as tk
from tkinter import *
root=tk.Tk()

# setting the windows size
root.geometry("300x100")

# declaring string variable
# for storing name and password
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


# defining a function that will
# get the name and password and
# print them on the screen
def submit():

    Asset_Code=AC_var.get()
    print(Asset_Code)
    Product_ID=PID_var.get()
    print(Product_ID)
    Warehouse=WH_var.get()
    print(Warehouse)
    Location=lOC_var.get()
    print(Location)
    Container_Num=CONNUM_var.get()
    print(Container_Num)
    Box_Num=BOXNUM_var.get()
    print(Box_Num)
    PO_Ref=POREF_var.get()
    print(PO_Ref)
    Colour=Colour_var.get()
    print(Colour)
    Size=SIZE_var.get()
    print(Size)
    Finish=FIN_var.get()
    print(Finish)

    AC_var.delete(0, END)
    AC_var.insert(0, "")
    PID_var.delete(0, END)
    PID_var.insert(0, "")
    WH_var.delete(0, END)
    WH_var.insert(0, "")
    lOC_var.delete(0, END)
    lOC_var.insert(0, "")
    CONNUM_var.delete(0, END)
    CONNUM_var.insert(0, "")
    BOXNUM_var.delete(0, END)
    BOXNUM_var.insert(0, "")
    POREF_var.delete(0, END)
    POREF_var.insert(0, "")
    Colour_var.delete(0, END)
    Colour_var.insert(0, "")
    SIZE_var.delete(0, END)
    SIZE_var.insert(0, "")
    FIN_var.delete(0, END)
    FIN_var.insert(0, "")
    #print("The name is : " + )
    #print("The password is : " + password)
    
    #AC_var.set("")
    #PID_var.set("")
    #WH_var.set("")
    #lOC_var.set("")
    #CONNUM_var.set("")
    #BOXNUM_var.set("")
    #POREF_var.set("")
    #Colour_var.set("")
    #SIZE_var.set("")
    #FIN_var.set("")
	
	
# creating a label for
# name using widget Label
#Asset Code,Product ID,Warehouse,Location,Container #,Box #,PO Ref,Color,Size,Finish
# creating a entry for input
# name using widget Entry
AC_label = tk.Label(root, text = 'Asset Code', font=('calibre',10, 'bold'))

AC_var = tk.Entry(root,textvariable = AC_var, font=('calibre',10,'normal'))

PID_label = tk.Label(root, text = 'Product ID', font=('calibre',10, 'bold'))

PID_var = tk.Entry(root,textvariable = PID_var, font=('calibre',10,'normal'))

WH_label = tk.Label(root, text = 'WareHouse', font = ('calibre',10,'bold'))

WH_var=tk.Entry(root, textvariable = WH_var, font = ('calibre',10,'normal'))

LOC_label = tk.Label(root, text = 'Location', font=('calibre',10, 'bold'))

lOC_var = tk.Entry(root,textvariable = lOC_var, font=('calibre',10,'normal'))

CONNUM_label = tk.Label(root, text = 'Container #', font=('calibre',10, 'bold'))

CONNUM_var = tk.Entry(root,textvariable = CONNUM_var, font=('calibre',10,'normal'))

BOXNUM_label = tk.Label(root, text = 'Box #', font=('calibre',10, 'bold'))

BOXNUM_var = tk.Entry(root,textvariable = BOXNUM_var, font=('calibre',10,'normal'))

POREF_label = tk.Label(root, text = 'PO Reference', font=('calibre',10, 'bold'))

POREF_var = tk.Entry(root,textvariable = POREF_var, font=('calibre',10,'normal'))

Colour_label = tk.Label(root, text = 'Colour', font=('calibre',10, 'bold'))

Colour_var = tk.Entry(root,textvariable = Colour_var, font=('calibre',10,'normal'))

SIZE_label = tk.Label(root, text = 'Size', font=('calibre',10, 'bold'))

SIZE_var = tk.Entry(root,textvariable = SIZE_var, font=('calibre',10,'normal'))

FIN_label = tk.Label(root, text = 'Finish', font=('calibre',10, 'bold'))

FIN_var = tk.Entry(root,textvariable = FIN_var, font=('calibre',10,'normal'))

def Clearit():
     root.destroy()
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
clear_btn=tk.Button(root,text = 'Destroy Window', command = Clearit)

# placing the label and entry in
# the required position using grid
# method
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
# performing an infinite loop
# for the window to display
root.mainloop()
