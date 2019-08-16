from tkinter import *

def submit():
	s=t.get('1.0',END)
	try:
		f=open("tkinter.txt","w")
		f.write(s)
		f.close()
		l1=Label(master,text="Data Saved Successfully.")
		l1.grid(row=3,column=0) 
		l1.config(font=12,fg="white",bg="grey")
		t.delete('1.0',END)

	except:
		l1=Label(master,text="Error while saving data.")
		l1.grid(row=3,column=0) 
		l1.config(font=12,fg="white",bg="grey")



master=Tk()
master.title("MyApp")
master.config(bg="lightgreen")

l=Label(master,text="Welcome to my MyApp")
l.grid(row=0,column=0) 
l.config(font=24,fg="white",bg="grey")

t=Text(master,height=15,width=25)
t.grid(row=1,column=0)

b=Button(master,text="Submit To Save",command=submit)
b.grid(row=2,column=0)

master.mainloop()