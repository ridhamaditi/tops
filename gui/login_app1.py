from tkinter import *

def login():
	pass

def signup():
	def register():
		fname = e1.get()
		lname = e2.get()
		uname = e3.get()
		age = e4.get()
		gender = v.get()
		password = e6.get()
		c_password = e7.get()

		if password == c_password:
			import sqlite3
			conn = sqlite3.connect('test.db')
			c = conn.cursor()
			try:
				age = int(age)
				c.execute("insert into login_details values('{}','{}', '{}', {}, '{}', '{}')".format(uname, fname, lname, age, gender, password))
				conn.commit()
				Label(signup_screen, text="Success.").grid(row=8, column=1)
			except:
				Label(signup_screen, text="Error.").grid(row=8, column=1)
				conn.rollback()
			conn.close()
		else:
			Label(signup_screen, text="Password doesn't match.").grid(row=8, column=1)

	master.destroy()
	signup_screen = Tk()
	signup_screen.title("Sign up")
	Label(signup_screen, text="First name").grid(row=0, column=0)
	Label(signup_screen, text="Last name").grid(row=1, column=0)
	Label(signup_screen, text="Username").grid(row=2, column=0)
	Label(signup_screen, text="Age").grid(row=3, column=0)
	Label(signup_screen, text="Gender").grid(row=4, column=0)
	Label(signup_screen, text="Password").grid(row=5, column=0)
	Label(signup_screen, text="Confirm Password").grid(row=6, column=0)

	e1 = Entry(signup_screen)
	e1.grid(row=0, column=1)
	e2 = Entry(signup_screen)
	e2.grid(row=1, column=1)
	e3 = Entry(signup_screen)
	e3.grid(row=2, column=1)
	e4 = Entry(signup_screen)
	e4.grid(row=3, column=1)
	v = StringVar()
	v.set("Male")
	r1 = Radiobutton(signup_screen, text="Male", variable=v, value="Male")
	r1.grid(row=4, column=1)
	r2 = Radiobutton(signup_screen, text="Female", variable=v, value="Female")
	r2.grid(row=4, column=2)
	e6 = Entry(signup_screen)
	e6.grid(row=5, column=1)
	e7 = Entry(signup_screen)
	e7.grid(row=6, column=1)

	Button(signup_screen, text="Register", command=register).grid(row=7, column=1)
	
	signup_screen.mainloop()

master = Tk()
Label(master, text="Welcome to my login app.").grid(row=0, column=1)
Button(master, text="Login", command=login).grid(row=1, column=0)
Button(master, text="Sign up", command=signup).grid(row=1, column=2)
master.mainloop()
