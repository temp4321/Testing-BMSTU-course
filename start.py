from tkinter import*
from user import user
from query import *

class start:
	def __init__(self, root, background_color, cursor):
		self.r = root
		self.bgc = background_color
		self.cur = cursor

	def init_widgets(self, root, bgc):
		self.login = Text(root,height=1.2,width=15,font='Arial 12')
		self.password = Text(root, height=1.2,width=15, font = 'Arial 12')
		self.loginlabel = Label(text='Логин:', font='Arial 14', bg = bgc)
		self.passwordlabel = Label(text='Пароль:', font='Arial 14', bg = bgc)
		self.login_button = Button(root, text = 'Войти', width=20,height=2,\
		 font='arial 14', command = self.loginevent)
		self.errorlabel = Label(text='Неверный логин или пароль',font='Arial 12', fg = 'Red', bg = bgc)

	def place_all(self):
		self.init_widgets(self.r, self.bgc)
		self.loginlabel.place(x = 295, y = 220)
		self.passwordlabel.place(x = 280, y = 245)
		self.login.place(x = 360, y = 220)
		self.password.place(x = 360, y = 245)
		self.login_button.place(x = 280, y = 300)

	def remove_all(self):
		self.loginlabel.destroy()
		self.passwordlabel.destroy()
		self.login.destroy()
		self.password.destroy()
		self.login_button.destroy()
		self.errorlabel.destroy()

	def loginevent(self):
		inputed_login = self.login.get('1.0', 'end-1c')
		inputed_password = self.password.get('1.0', 'end-1c')
		
		q = get_all_log_pass()
		self.cur.execute(q)
		tmp = self.cur.fetchall()
		print(tmp)

		res = ""
		for i in range(len(tmp)):
			if tmp[i][0] == inputed_login and tmp[i][1] == inputed_password:
				if inputed_login == "admin":
					res = "admin"
				else:
					res = "user"

		if res == "admin":
			self.remove_all()
			#...

		elif res == "user":
			self.remove_all()
			user_page = user(self.r, self.bgc, inputed_login, self.cur)
			user_page.place_start()

			return True
			#...

		else:
			self.errorlabel.place(x = 300, y = 275)

			return False

	def eb(self):
		return 1

