# start, loginevent
def get_all_log_pass():
	return "select \
					client_login, \
					client_password \
			from \
					client;"


# user, 2
def get_all_clubs():
	return "select \
					club_name \
			from \
					club;"


def get_all_sports():
	return "select \
					sport_name \
			from \
					sport;"

# user, 3
def get_actual_workouts(userid, today_date, club, sport):
	return "select DISTINCT\
					sport_name, \
					coach_name, \
					coach_rating, \
					w_type, \
					w_places, \
					w_date, \
					w_duribility, \
					w_id \
			from \
					workout, \
					sport, \
					coach, \
					client_workout, \
					club \
			where \
					w_sportid = sport_id and \
					w_coachid = coach_id and \
					w_clubid = club_id and \
					w_id = cw_workoutid and \
					w_places > 0 and \
					w_id NOT IN (select \
										cw_workoutid \
								from \
										client_workout \
								where \
										cw_clientid = " + str(userid) + ") and \
					club_name = '" + club + "' and \
					sport_name = '" + sport + "' and \
					w_date >= '" + today_date + "';"


def generate_insert_into_client_workout(userid, w_id):
	return "insert into client_workout \
			(cw_clientid, cw_workoutid, cw_rating) \
			values (" + str(userid) + ", " + str(w_id) + ", ' ');"


def generate_update_for_places_count(w_id):
	return "update \
					workout \
			set \
					w_places = w_places - 1 \
			where \
					w_id = " + str(w_id) + " and \
					w_places > 0;"


# user, 4
def get_user_past_workouts(userid, today_date):
	return "select DISTINCT\
					club_name, \
					sport_name, \
					coach_name, \
					w_date, \
					w_duribility, \
					cw_rating, \
					w_id \
			from \
					club, \
					coach, \
					sport, \
					workout, \
					client_workout \
			where \
					w_sportid = sport_id and \
					w_coachid = coach_id and \
					w_clubid = club_id and \
					w_id = cw_workoutid and \
					cw_clientid = " + str(userid) + " and \
					w_date < '" + today_date + "';"


def get_user_future_workouts(userid, today_date):
	return "select DISTINCT\
					club_name, \
					sport_name, \
					coach_name, \
					w_date, \
					w_duribility, \
					cw_rating, \
					w_id \
			from \
					club, \
					coach, \
					sport, \
					workout, \
					client_workout \
			where \
					w_sportid = sport_id and \
					w_coachid = coach_id and \
					w_clubid = club_id and \
					w_id = cw_workoutid and \
					cw_clientid = " + str(userid) + " and \
					w_date >= '" + today_date + "';"


def get_current_workout_rating(userid, w_id):
	return "select \
					cw_rating \
			from \
					client_workout \
			where \
					cw_clientid = " + str(userid) + " and \
					cw_workoutid = " + str(w_id) + ";"


def update_rating(userid, w_id, inputed_rating):
	return "update \
					client_workout \
			set \
					cw_rating = '" + str(inputed_rating) + "' \
			where \
					cw_clientid = " + str(userid) + " and \
					cw_workoutid = " + str(w_id) + ";"


def get_current_coach_id_rating(w_id):
	return "select \
					coach_id, \
					coach_rating, \
					coach_marked_workouts_count \
			from \
					coach, \
					workout \
			where \
					w_coachid = coach_id and \
					w_id = " + str(w_id) + ";"


def update_coach_rating(coach_id, new_rating):
	return "update \
					coach \
			set \
					coach_rating = " + str(new_rating) + ", \
					coach_marked_workouts_count = coach_marked_workouts_count + 1 \
			where \
					coach_id = " + str(coach_id) + ";"


def delete_cancel_workout(userid, w_id):
	return "delete from client_workout \
			where \
					cw_clientid = " + str(userid) + " and \
					cw_workoutid = " + str(w_id) + ";"

def update_places(w_id):
	return "update \
					workout \
			set \
					w_places = w_places + 1 \
			where \
					w_id = " + str(w_id) + ";"
