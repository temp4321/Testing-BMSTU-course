import random

def to_file(data, file_name):
	with open(file_name, "w") as f:
		for row in data:
			i = 0
			for i in range(len(row)):
				f.write(str(row[i]))
				if i != len(row) - 1:
					f.write("|")
			f.write(" \n")

def get_r(mass):
	return str(mass[random.randint(0, len(mass) - 1)])

def gen_past_date():
	return "2018-0" + str(random.randint(1,8)) + "-" + str(random.randint(0, 1))\
	 + str(random.randint(1, 9)) + " 1" + str(random.randint(0,9)) + ":" + \
	 str(random.randint(1,5)) + "0:00 "


def gen_future_date():
	return "2018-1" + str(random.randint(0,2)) + "-" + str(random.randint(0, 1))\
	 + str(random.randint(1, 9)) + " 1" + str(random.randint(0,9)) + ":" + \
	 str(random.randint(1,5)) + "0:00"

def is_in_mas(mas, k1, k2):
	for i in range(len(mas)):
		if mas[i][0] == k1 and mas[i][1] == k2:
			return True
	return False

club1_count = 234
club2_count = 120
club3_count = 57
club4_count = 201

clubs = [[1, "forlife1", "Moscow", "Tverskaya 3", club1_count],
		  [2, "forlife2", "Moscow", "St. Arbat 10", club2_count],
		  [3, "forlife3", "Moscow", "Dolshanskaya 4", club3_count],
		  [4, "forlife4", "SPB", "Parkov 9", club4_count]]

familii = ["Ivanov", "Petrov", "Sidorov", "Andreev", "Gulatov", \
	"Maksimenko", "Doriskapcheev", "Antonov", "Kulichev", "Gordeev",\
	"Entimenko", "Popugaev"]

imena = ["Andrey", "Stepan", "Fedor", "Aleksandr", "Yuri", "Nikita",\
	"Sergey", "Ilya", "Konstantin", "Vladislav", "Aleksey", "Vitaliy",\
	"Evgeniy", "Vladimir"]

bookvi = ["a", "b", "c", "d", "f", "i", "g", "h"]
emails = ["@yandex.ru", "@mail.ru", "@gmail.com", "@rambler.ru"]
workout_type = ["I", "G"]
duribility = ["30min", "35min", "40min", "45min", "50min", "60min"]

clients = []

def gen_clients_for_club(clients, count, club_id):
	client_sum = len(clients) + 1

	for i in range(count):
		client_id = client_sum
		client_name = get_r(familii) + " " + get_r(imena)
		client_birth_date = "199" + str(random.randint(0, 9)) + "-0" \
		+ str(random.randint(1, 9)) + "-" + str(random.randint(0,1)) + \
		str(random.randint(1, 9))
		client_clubid = club_id
		client_login = "user" + str(client_sum)
		client_password = str(random.randint(0, 5)) + str(random.randint(0, 5))+ \
		str(random.randint(0, 5)) + str(random.randint(0, 5)) + str(random.randint(0, 5))
		client_email = get_r(bookvi) + get_r(bookvi) + get_r(bookvi) + \
		get_r(bookvi) + get_r(bookvi) + get_r(bookvi) + get_r(bookvi) + get_r(emails)
		clients.append([client_id, client_name, client_birth_date, client_clubid, \
			client_login, client_password, client_email])
		client_sum += 1

	return clients



sport = [[1, "Box"], [2, "Football"], [3, "Florball"], [4, "Rastyashka"],\
[5, "Turnik"], [6, "Fitnes"], [7, "Swimming"], [8, "Hapkido"], [9, "Pilates"],\
[10, "Yoga"]]

def gen_coachs(count):
	coachs = []

	for i in range(count):
		coach_id = i + 1
		coach_name = get_r(familii) + " " + get_r(imena)
		tmp = random.randint(1, 5)
		if tmp == 5:
			coach_rating = tmp
		else:
			coach_rating = tmp + random.random()
		coach_rating = round(coach_rating, 2)
		coach_marked_workouts_count = random.randint(20, 30)
		coachs.append([coach_id, coach_name, coach_rating, coach_marked_workouts_count])

	return coachs

def gen_workouts(coachs, clients, clubs, sport):
	workouts = []

	w_count = 1

	for i in range(len(coachs)):
		for j in range(coachs[i][3]):
			w_id = w_count
			w_clubid = random.randint(1, 4)
			w_sportid = random.randint(1, 10)
			w_coachid = coachs[i][0]
			if j > coachs[i][3]/2:
				w_date = gen_future_date()
			else:
				w_date = gen_past_date()
			w_type = get_r(workout_type)
			if w_type == "I":
				w_places = random.randint(0,1)
			else:
				w_places = random.randint(5, 20)
			w_duribility = get_r(duribility)

			workouts.append([w_id, w_clubid, w_sportid, w_coachid,\
				w_date, w_type, w_places, w_duribility])
			w_count += 1

	return workouts

def gen_client_workout(clients, workouts):
	res = []

	for i in range(len(workouts)):
		if workouts[i][6] == 0:
			cw_clientid = random.randint(1, len(clients))
			cw_workoutid = workouts[i][0]
			if workouts[i][4][5] == "1":
				cw_rating = " "
			else:
				rnd = random.randint(0,1)
				if rnd == 1:
					tmp = random.randint(1,5)
					if tmp == 5:
						cw_rating = str(5)
					else:
						tmp = tmp + random.random()
						tmp = round(tmp, 2)
						cw_rating = str(tmp)
				else:
					cw_rating = " "

			if is_in_mas(res, cw_clientid, cw_workoutid) == False:
				res.append([cw_clientid, cw_workoutid, cw_rating])

		elif workouts[i][6] != 1:
			for j in range(int(workouts[i][6]/2)):
				cw_clientid = random.randint(1, len(clients))
				cw_workoutid = workouts[i][0]
				if workouts[i][4][5] == "1":
					cw_rating = " "
				else:
					rnd = random.randint(0,1)
					if rnd == 1:
						tmp = random.randint(1,5)
						if tmp == 5:
							cw_rating = str(5)
						else:
							tmp = tmp + random.random()
							tmp = round(tmp, 2)
							cw_rating = str(tmp)
					else:
						cw_rating = " "

				if is_in_mas(res, cw_clientid, cw_workoutid) == False:
					res.append([cw_clientid, cw_workoutid, cw_rating])

	return res


clients = gen_clients_for_club(clients, club1_count, 1)
clients = gen_clients_for_club(clients, club2_count, 2)
clients = gen_clients_for_club(clients, club3_count, 3)
clients = gen_clients_for_club(clients, club4_count, 4)
coachs = gen_coachs(40)
workouts = gen_workouts(coachs, clients, clubs, sport)
client_workout = gen_client_workout(clients, workouts)

to_file(clients, "client.tbl")
to_file(sport, "sport.tbl")
to_file(clubs, "club.tbl")
to_file(coachs, "coach.tbl")
to_file(workouts, "workout.tbl")
to_file(client_workout, "client_workout.tbl")