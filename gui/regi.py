from tkinter import *
import sqlite3

def submit():
	s1=e1.get()
	s2=e2.get()
	s3=e3.get()
	s4=v.get()
	s5=e5.get()
	s6=e6.get()

	try:
		# f=open("tkinterRegi.txt","a")
		# f.write(s1+"\n")
		# f.write(s2+"\n")
		# f.write(s3+"\n")
		# f.write(s4+"\n")
		# f.write(s5+"\n")
		# f.write(s6+"\n")
		# f.write("------------------------------------------------------------------------------------\n")
		# f.close()
		conn = sqlite3.connect("test.db")
		c = conn.cursor()
		sql = "INSERT INTO EMPLOYEE (`FIRST_NAME`, `LAST_NAME`, `EID`, `GENDER`, `AGE`, `SALARY`) VALUES ('{}', '{}', '{}', '{}', {}, {})".format(s1, s2, s3, s4, s5, s6)
		c.execute(sql)
		conn.commit()
		conn.close()
		k=Label(master,text="Data Saved Successfully.")
		k.grid(row=8,column=1)
		k.config(font=12,fg="white",bg="grey")

		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		#e4.delete(0,END)
		e5.delete(0,END)
		e6.delete(0,END)


	except:
		k=Label(master,text="Error while saving Data.")
		k.grid(row=8,column=1)
		k.config(font=12,fg="white",bg="grey")


master=Tk()
master.title("MyApp")
master.config(bg="lightgreen")

l=Label(master,text="Welcome to Registration App")
l.grid(row=0,column=0)
l.config(font=24,fg="white",bg="grey")

l1=Label(master,text="First name:     ")
l1.grid(row=1,column=0)
e1=Entry(master)
e1.grid(row=1,column=1)

l2=Label(master,text="Last name:     ")
l2.grid(row=2,column=0)
e2=Entry(master)
e2.grid(row=2,column=1)

l3=Label(master,text="Employee Id:     ")
l3.grid(row=3,column=0)
e3=Entry(master)
e3.grid(row=3,column=1)

l4=Label(master,text="Gender:     ")
l4.grid(row=4,column=0)
v = StringVar()
v.set("Female")
e41 = Radiobutton(master, text="Male", variable=v, value="Male")
e41.grid(row=4,column=1)
e42 = Radiobutton(master, text="Female", variable=v, value="Female")
e42.grid(row=4,column=2)

l5=Label(master,text="Age:     ")
l5.grid(row=5,column=0)
e5=Entry(master)
e5.grid(row=5,column=1)

l6=Label(master,text="Salary:     ")
l6.grid(row=6,column=0)
e6=Entry(master)
e6.grid(row=6,column=1)



b=Button(master,text="Submit To Save",command=submit)
b.grid(row=7,column=1)

master.mainloop()
