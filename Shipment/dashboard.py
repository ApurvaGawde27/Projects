from __future__ import unicode_literals

# from pymongo import MongoClient
# from random import randint
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter.messagebox as ms
#import tkinter.ttk
from tkinter import Button
import sys

# try:
# 	client = MongoClient(port=27017)
# 	db=client.Assignment08
# 	print("Connected to MongoDB")
# except :
# 	print("Database connection Error ")
# 	print("No connection could be made because the target machine actively refused it ")
# 	ms.showerror("Error", "Connection Error")
# 	sys.exit(1)

root = Tk()
root.geometry("1100x500+220+130")
root.title("Shipment Management Company")
root.config(bg="white")
root.focus_force()

#Title
icon_title=PhotoImage(file="images/logo1.png")
title=Label(root, text="Shipment Management Company",image=icon_title,compound=LEFT,font=("times new roman", 40, "bold"),bg="#010c48", fg="white", anchor="w", padx=20).place(x=0,y=0,relwidth=1, height=70)
#logout button
btn_logout=Button(root,text="Logout",font=("times new roman", 15, "bold"),bg="yellow", cursor="hand2").place(x=1500,y=10, width=150, height=50)
#clock
lbl_clock=Label(root, text="Welcom to GoMovers\t\t Date: DD-MM-YYYY\t\t Time: HH:MMLSS",font=("times new roman", 15),bg="#4d636d", fg="white")
lbl_clock.place(x=0,y=70,relwidth=1, height=20)
#left Menu
MenuLogo=Image.open("images/hero-banner.jpg")
MenuLogo=MenuLogo.resize((200,200), Image.LANCZOS)
MenuLogo=ImageTk.PhotoImage(MenuLogo)
LeftMenu=Frame(root,bd=2,relief=RIDGE,bg="white")
LeftMenu.place(x=0,y=102,width=200,height=565)

lbl_menuLogo=Label(LeftMenu,image=MenuLogo)
lbl_menuLogo.pack(side=TOP, fill=X)
icon_side=PhotoImage(file="images/side1.png")


lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman", 20),bg="#009688").pack(side=TOP, fill=X)
btn_employee=Button(LeftMenu,text="Employee",command=employees, image=icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman", 18, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
btn_supplier=Button(LeftMenu,text="Supplier",image=icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman", 18, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
btn_category=Button(LeftMenu,text="Category",image=icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman", 18, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
btn_product=Button(LeftMenu,text="Product",image=icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman", 18, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
btn_sales=Button(LeftMenu,text="Sales",image=icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman", 18, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
btn_exit=Button(LeftMenu,text="Exit",image=icon_side,compound=LEFT,padx=20,anchor="w",font=("times new roman", 16, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

#content
lbl_employee=Label(root,text="Total Employee\n[ 0 ]", bg="#33bbf9", bd=5,relief=RIDGE, fg="white", font=("goudy old style",20, "bold") )
lbl_employee.place(x=300,y=120,height=150,width=300)

lbl_supplier=Label(root,text="Total Supplier\n[ 0 ]", bg="#33bbf9", bd=5,relief=RIDGE, fg="white", font=("goudy old style",20, "bold") )
lbl_supplier.place(x=650,y=120,height=150,width=300)

lbl_category=Label(root,text="Total Category\n[ 0 ]", bg="#33bbf9", bd=5,relief=RIDGE, fg="white", font=("goudy old style",20, "bold") )
lbl_category.place(x=1000,y=120,height=150,width=300)

lbl_product=Label(root,text="Total Product\n[ 0 ]", bg="#33bbf9", bd=5,relief=RIDGE, fg="white", font=("goudy old style",20, "bold") )
lbl_product.place(x=300,y=300,height=150,width=300)

lbl_sales=Label(root,text="Total Sales\n[ 0 ]", bg="#33bbf9", bd=5,relief=RIDGE, fg="white", font=("goudy old style",20, "bold") )
lbl_sales.place(x=650,y=300,height=150,width=300)

#Footer
    
lbl_footer=Label(root, text="Shipment Management Company-GoMovers",font=("times new roman", 12),bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
root.mainloop()