from tkinter import *



root=Tk()
root.geometry("350x370")
root.title("my tkinter example")
root.resizable(width=False,height= False)


l_id=Label(root,text="ID")
L_id.place(x=50,y=50)

l_fname=Label(root,text="First name")
L_fname.place(x=50,y=100)

l_lname=Label(root,text="last name")
L_lname.place(x=50,y=150)

l_email=Label(root,text="Email")
L_email.place(x=50,y=200)

l_mobile=Label(root,text="Mobile")
L_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text"INSERT",bg="black",fg="white",font=("forte",12))
insert.place(x=20,y=300)

search=Button(root,text"SEARCH",bg="black",fg="white",font=("forte",12))
search.place(x=95,y=300)

update=Button(root,text"UPDATE",bg="black",fg="white",font=("forte",12))
update.place(x=174,y=300)

delete=Button(root,text"DELETE",bg="black",fg="white",font=("forte",12))
delete.place(x=252,y=300)
