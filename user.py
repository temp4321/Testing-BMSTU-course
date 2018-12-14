from tkinter import*
from tkinter.ttk import Treeview
from tkinter import messagebox
import datetime
from my_parser import *
from query import *

class user:
	def __init__(self, root, background_color, user_login, cursor):
		self.r = root
		self.bgc = background_color
		self.login = user_login
		self.cur = cursor
		
		self.cur.execute("select client_id from client where client_login = '" + user_login +"';")
		tmp = self.cur.fetchall()
		self.userid = tmp[0][0]
		
		self.today_date = '{0:%Y-%m-%d %H:%M:%S} '.format(datetime.datetime.now())

##############################################################################
	# 1. START

	# 1.1 INIT
	def init_start_widgets(self):
		self.choose_button = Button(self.r, text = "Записаться", width=20, height=7, command=self.choose)
		self.my_workouts_button = Button(self.r, text = "Мои занятия", width=20, height=7, command=self.show_my_workouts)

	# 1.2 PLACE
	def place_start(self):
		self.init_start_widgets()
		self.choose_button.place(x = 200, y = 240)
		self.my_workouts_button.place(x = 400, y = 240)

	# 1.3 REMOVE
	def remove_start(self):
		self.choose_button.destroy()
		self.my_workouts_button.destroy()

	# 1.4 COMMANDS
	def choose(self):
		self.remove_start()
		self.place_choose()

	def show_my_workouts(self):
		self.remove_start()
		self.place_my_worklouts()


##############################################################################


##############################################################################
	# 2. CHOOSE CLUB AND KIND OF SPORT

	# 2.1 INIT
	def init_choose_widgets(self, root):
		self.choose_label = Label(text='Выберите клуб и вид спорта:',\
		 						 font = 'Arial 20', bg = self.bgc)

		q = get_all_clubs()
		self.cur.execute(q)
		tmp = self.cur.fetchall()

		clubs = []

		for i in range(len(tmp)):
			clubs.append(tmp[i][0])

		self.variable_c = StringVar(root)
		self.variable_c.set(clubs[0]) # default value
		self.clubs_option_menu = OptionMenu(root, self.	variable_c, *clubs)
		self.clubs_option_menu.config(width = 20, height = 3, bg=self.bgc, font = 16)

		q = get_all_sports()
		self.cur.execute(q)
		tmp = self.cur.fetchall()

		kind_of_sport = []

		for i in range(len(tmp)):
			kind_of_sport.append(tmp[i][0])

		self.variable_k = StringVar(root)
		self.variable_k.set(kind_of_sport[0])
		self.kind_of_sport_option_menu = OptionMenu(root, self.variable_k, *kind_of_sport)
		self.kind_of_sport_option_menu.config(width=20,height=3,bg=self.bgc,font=16)

		self.next_in_choose_button = Button(root, text='Далее',width=15,\
			height=3,command=self.next_in_choose)

		self.back_to_start_button = Button(root, text='Назад',width=15,height=3,\
			command=self.back_to_start)

	# 2.2 PLACE
	def place_choose(self):
		self.init_choose_widgets(self.r)
		self.choose_label.place(x = 200, y = 160)
		self.clubs_option_menu.place(x = 260, y = 200)
		self.kind_of_sport_option_menu.place(x = 260, y = 300)
		self.next_in_choose_button.place(x = 305, y = 400)
		self.back_to_start_button.place(x = 305, y = 500)

	# 2.3 REMOVE
	def remove_choose(self):
		self.choose_label.destroy()
		self.clubs_option_menu.destroy()
		self.kind_of_sport_option_menu.destroy()
		self.next_in_choose_button.destroy()
		self.back_to_start_button.destroy()

	# 2.3 COMMANDS
	def next_in_choose(self):
		club = self.variable_c.get()
		kind_of_sport = self.variable_k.get()
		self.remove_choose()
		self.place_trainlist(club, kind_of_sport)

	def back_to_start(self):
		self.remove_choose()
		self.place_start()

##############################################################################


##############################################################################
	# 3. TRAINLIST

	# 3.1 INIT
	def init_trainlist_widgets(self, root, club, sport):
		headings = ["вид спорта", "тренер", "рейтинг","тип", "места", "дата",\
		"длительность"]

		self.trains_table = Treeview(root, selectmode="browse", show='headings',height = 25)
		self.trains_table["columns"] = headings
		self.trains_table["displaycolumns"] = headings

		for head in headings:
			self.trains_table.heading(head, text=head, anchor=CENTER)

		self.trains_table.column("вид спорта", anchor=CENTER, width = 180)
		self.trains_table.column("тренер", anchor=CENTER, width = 180)
		self.trains_table.column("рейтинг", anchor=CENTER, width = 70)
		self.trains_table.column("тип", anchor=CENTER, width = 40)
		self.trains_table.column("места", anchor=CENTER, width = 60)
		self.trains_table.column("дата", anchor=CENTER, width = 145)
		self.trains_table.column("длительность", anchor=CENTER, width = 120)

		q = get_actual_workouts(self.userid, self.today_date, club, sport)
		self.cur.execute(q)
		tmp = self.cur.fetchall()
		self.w_ids = []

		for train in tmp:
			train = list(train)
			poped = train.pop(len(train) - 1)
			self.w_ids.append(poped)
			self.trains_table.insert('', END, values = tuple(train))

		self.choose_train_button = Button(root,text="Выбрать",width=15,height=3,command=self.choose_train)
		self.back_to_choose_button = Button(root, text='Назад',width=15,height=3,\
			command=self.back_to_choose)

	# 3.2 PLACE
	def place_trainlist(self, club, kind_of_sport):
		self.init_trainlist_widgets(self.r, club, kind_of_sport)
		self.trains_table.place(x = 0, y = 0)
		self.choose_train_button.place(x = 320, y = 530)
		self.back_to_choose_button.place(x = 0, y = 530)

	# 3.3 REMOVE
	def remove_trainlist(self):
		self.trains_table.destroy()
		self.choose_train_button.destroy()
		self.back_to_choose_button.destroy()

	# 3.4 COMMANDS
	def choose_train(self):
		indd = self.trains_table.focus()
		if indd == "":
			messagebox.showinfo("", "Выберите тренировку")
		else:
			ind = int(convert_base(indd[1:], to_base=10, from_base=16)) - 1
			curr_workout_id = self.w_ids[ind]

			q = generate_insert_into_client_workout(self.userid, curr_workout_id)
			self.cur.execute(q)

			q = generate_update_for_places_count(curr_workout_id)
			self.cur.execute(q)

			self.remove_trainlist()
			self.place_start()
			messagebox.showinfo("", "Подтверждено")

	def back_to_choose(self):
		self.remove_trainlist()
		self.place_choose()

##############################################################################


##############################################################################
	# 4. MY_WORKOUTS

	# 4.1 INIT
	def init_my_workouts_widgets(self, root):
		self.my_workouts_label = Label(text='Мои занятия:',\
		 						 font = 'Arial 20', bg = self.bgc)
		self.past_workouts_button = Button(root,text="Прошедшие",width=17,height=10,\
			command=self.show_past)
		self.future_workouts_button = Button(root,text="Предстоящие",width=17,height=10,\
			command=self.show_future)
		self.back_to_start_button2 = Button(root, text='Назад',width=17,height=3,\
			command=self.back_to_start2)

	# 4.2 PLACE
	def place_my_worklouts(self):
		self.init_my_workouts_widgets(self.r)
		self.my_workouts_label.place(x=315, y = 80)
		self.past_workouts_button.place(x=315, y = 120)
		self.future_workouts_button.place(x = 315, y = 300)
		self.back_to_start_button2.place(x = 315, y = 500)

	# 4.3 REMOVE
	def remove_my_workouts(self):
		self.my_workouts_label.destroy()
		self.past_workouts_button.destroy()
		self.future_workouts_button.destroy()
		self.back_to_start_button2.destroy()

	# 4.4 COMMANDS
	def show_past(self):
		self.remove_my_workouts()
		self.place_past_workouts()

	def show_future(self):
		self.remove_my_workouts()
		self.place_future_workouts()

	def back_to_start2(self):
		self.remove_my_workouts()
		self.place_start()

##############################################################################


##############################################################################
	# 5. PAST WORKOUTS

	# 5.1 INIT
	def init_past_workouts_widgets(self, root):
		self.past_workouts_table = Treeview(root, selectmode="browse", show='headings',height = 25)

		headings = ["клуб", "вид спорта", "тренер", "дата", "длительность", "ваша оценка"]

		self.past_workouts_table["columns"] = headings
		self.past_workouts_table["displaycolumns"] = headings

		for head in headings:
			self.past_workouts_table.heading(head, text=head, anchor=CENTER)

		self.past_workouts_table.column("клуб", anchor=CENTER, width = 115)
		self.past_workouts_table.column("вид спорта", anchor=CENTER, width = 155)
		self.past_workouts_table.column("тренер", anchor=CENTER, width = 165)
		self.past_workouts_table.column("дата", anchor=CENTER, width = 135)
		self.past_workouts_table.column("длительность", anchor=CENTER, width = 110)
		self.past_workouts_table.column("ваша оценка", anchor=CENTER, width = 125)

		q = get_user_past_workouts(self.userid, self.today_date)
		self.cur.execute(q)
		tmp = self.cur.fetchall()
		self.w_ids_for_rating = []

		for train in tmp:
			train = list(train)
			poped = train.pop(len(train) - 1)
			self.w_ids_for_rating.append(poped)
			self.past_workouts_table.insert('', END, values = tuple(train))

		self.set_rating_button = Button(root,text="Поставить оценку",width=15,height=1, \
			command=self.set_rating)
		self.back_to_my_workouts_button = Button(root, text='Назад',width=15,height=3,\
			command=self.back_to_my_workouts)

		self.rating_entry = Text(root, height=1.2, width=16, font='Arial 12')

	# 5.2 PLACE
	def place_past_workouts(self):
		self.init_past_workouts_widgets(self.r)
		self.past_workouts_table.place(x=0,y=0)
		self.set_rating_button.place(x=320,y=530)
		self.back_to_my_workouts_button.place(x=0,y=530)
		self.rating_entry.place(x = 320, y = 560)

	# 5.3 REMOVE
	def remove_past_workouts(self):
		self.past_workouts_table.destroy()
		self.set_rating_button.destroy()
		self.back_to_my_workouts_button.destroy()
		self.rating_entry.destroy()

	# 5.4 COMMANDS
	def set_rating(self):
		indd = self.past_workouts_table.focus()

		if indd == "":
			messagebox.showinfo("", "Выберите тренировку")
		else:
			ind = int(convert_base(indd[1:], to_base=10, from_base=16)) - 1
			curr_workout_id = self.w_ids_for_rating[ind]

			q = get_current_workout_rating(self.userid, curr_workout_id)
			self.cur.execute(q)
			tmp = self.cur.fetchall()
			current_train_rating = tmp[0][0]

			if current_train_rating == " ":
				input_rating = self.rating_entry.get('1.0', 'end-1c')
				if input_rating.replace(".", "", 1).isdigit() == False:
					messagebox.showinfo("", "Оценка введена некоректно")
				elif float(input_rating) < 0 or float(input_rating) > 5:
					messagebox.showinfo("", "Оценка ставиться по пятибальной шкале")
				else:
					input_rating = round(float(input_rating), 2)
					q = update_rating(self.userid, curr_workout_id, input_rating)
					self.cur.execute(q)

					q = get_current_coach_id_rating(curr_workout_id)
					self.cur.execute(q)
					tmp = self.cur.fetchall()
					
					tmp_coach_id = int(tmp[0][0])
					tmp_coach_rating = tmp[0][1]
					tmp_coach_marked_w_count = tmp[0][2]

					new_rating = (tmp_coach_rating*tmp_coach_marked_w_count + input_rating)/(tmp_coach_marked_w_count + 1)
					q = update_coach_rating(tmp_coach_id, new_rating)
					self.cur.execute(q)


					self.remove_past_workouts()
					self.place_past_workouts()
			else:
				messagebox.showinfo("", "Оценка уже выставлена. В соответствии с нашими правилами оценка выставляется один раз и не подлежит изменению")
			
	def back_to_my_workouts(self):
		self.remove_past_workouts()
		self.place_my_worklouts()

##############################################################################


##############################################################################
	# 6. FUTURE WORKOUTS

	# 6.1 INIT
	def init_future_workouts_widgets(self, root):
		self.future_workouts_table = Treeview(root, selectmode="browse", show='headings',height = 25)

		headings = ["клуб", "вид спорта", "тренер", "дата", "длительность", "рейтинг"]

		self.future_workouts_table["columns"] = headings
		self.future_workouts_table["displaycolumns"] = headings

		for head in headings:
			self.future_workouts_table.heading(head, text=head, anchor=CENTER)

		self.future_workouts_table.column("клуб", anchor=CENTER, width = 115)
		self.future_workouts_table.column("вид спорта", anchor=CENTER, width = 155)
		self.future_workouts_table.column("тренер", anchor=CENTER, width = 165)
		self.future_workouts_table.column("дата", anchor=CENTER, width = 150)
		self.future_workouts_table.column("длительность", anchor=CENTER, width = 110)
		self.future_workouts_table.column("рейтинг", anchor=CENTER, width = 110)

		q = get_user_future_workouts(self.userid, self.today_date)
		self.cur.execute(q)
		tmp = self.cur.fetchall()
		self.w_ids_for_remove_workout = []

		for train in tmp:
			train = list(train)
			poped = train.pop(len(train) - 1)
			self.w_ids_for_remove_workout.append(poped)
			self.future_workouts_table.insert('', END, values = tuple(train))

		self.remove_workout_button = Button(root,text="Отменить тренировку",width=15,height=3,command=self.remove_workout)
		self.back_to_my_workouts_button2 = Button(root, text='Назад',width=15,height=3,\
			command=self.back_to_my_workouts2)


	# 6.2 PLACE
	def place_future_workouts(self):
		self.init_future_workouts_widgets(self.r)
		self.future_workouts_table.place(x=0,y=0)
		self.remove_workout_button.place(x=300, y=530)
		self.back_to_my_workouts_button2.place(x=0,y=530)

	# 6.3 REMOVE
	def remove_future_workouts(self):
		self.future_workouts_table.destroy()
		self.remove_workout_button.destroy()
		self.back_to_my_workouts_button2.destroy()

	# 6.4 COMMANDS
	def remove_workout(self):
		indd = self.future_workouts_table.focus()
		if indd == "":
			messagebox.showinfo("", "Выберите тренировку")
		else:
			ind = int(convert_base(indd[1:], to_base=10, from_base=16)) - 1
			curr_workout_id = self.w_ids_for_remove_workout[ind]

			q = delete_cancel_workout(self.userid, curr_workout_id)
			self.cur.execute(q)

			q = update_places(curr_workout_id)
			self.cur.execute(q)

			self.remove_future_workouts()
			self.place_future_workouts()

	def back_to_my_workouts2(self):
		self.remove_future_workouts()
		self.place_my_worklouts()

##############################################################################
