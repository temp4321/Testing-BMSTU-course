def convert_base(num, to_base=10, from_base=16):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def get_create_table_queries(filename):
	file_str = ""
	with open(filename, "r") as f:
		file_str = f.read()
	
	queries = []
	ind = 0
	for i in range(len(file_str)):
		if file_str[i] == ';':
			queries.append(file_str[ind:i].replace("\n", ""))
			ind = i + 1

	return queries


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def get_necessary_format(data):
	ind = 0
	result = ""

	for i in range(len(data)):
		if data[i] == '|':
			if is_number(data[ind:i]):
				result += data[ind:i] + ","
			else:
				result += "'" + data[ind:i] + "',"
			ind = i + 1
	if is_number(data[ind:i]):
		result += data[ind:i] + ")"
	else:
		result += "'" + data[ind:i] + "')"

	return result


def get_insert_into_table_queries(tbls_pathe):
	queries = []
	insert_constant_parts = [] 
	insert_constant_parts.append("INSERT INTO club (club_id, club_name, club_city, club_addr, club_guest_count) VALUES (")
	insert_constant_parts.append("INSERT INTO coach (coach_id, coach_name, coach_rating, coach_marked_workouts_count) VALUES (")
	insert_constant_parts.append("INSERT INTO sport (sport_id, sport_name) VALUES (")
	insert_constant_parts.append("INSERT INTO workout (w_id, w_clubid, w_sportid, w_coachid, w_date, w_type, w_places, w_duribility) VALUES (")
	insert_constant_parts.append("INSERT INTO client (client_id, client_name, client_birth_date, client_clubid, client_login, client_password, client_email) VALUES (")
	insert_constant_parts.append("INSERT INTO client_workout (cw_clientid, cw_workoutid, cw_rating) VALUES (")

	for i in range(len(tbls_pathe)):
		file_str = ""
		with open(tbls_pathe[i], "r") as f:
			file_str = f.read()

		ind = 0
		for j in range(len(file_str)):
			if file_str[j] == '\n':
				query = insert_constant_parts[i] + get_necessary_format(file_str[ind:j])
				queries.append(query)
				ind = j + 1

	return queries

#print(get_create_table_queries("create.sql"))