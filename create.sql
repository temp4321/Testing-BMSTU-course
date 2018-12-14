CREATE TABLE club (club_id INTEGER NOT NULL,
                   club_name CHAR(25) NOT NULL,
                   club_city CHAR(25) NOT NULL,
                   club_addr CHAR(100) NOT NULL,
                   club_guest_count INTEGER NOT NULL,
                   PRIMARY KEY(club_id));

CREATE TABLE coach (coach_id INTEGER NOT NULL,
                    coach_name CHAR(25) NOT NULL,
                    coach_rating double precision NOT NULL,
                    coach_marked_workouts_count INTEGER NOT NULL,
                    PRIMARY KEY(coach_id));

CREATE TABLE sport (sport_id INTEGER NOT NULL,
                    sport_name CHAR(25) NOT NULL,
                    PRIMARY KEY(sport_id));

CREATE TABLE workout (w_id INTEGER NOT NULL,
                      w_clubid INTEGER NOT NULL,
                      w_sportid INTEGER NOT NULL,
                      w_coachid INTEGER NOT NULL,
                      w_date DATETIME NOT NULL,
                      w_type CHAR(1) NOT NULL,
                      w_places INTEGER NOT NULL,
                      w_duribility CHAR(10) NOT NUll,
                      PRIMARY KEY(w_id));

CREATE TABLE client (client_id INTEGER NOT NULL,
                     client_name CHAR(50) NOT NULL,
                     client_birth_date DATE NOT NULL,
                     client_clubid INTEGER NOT NULL,
                     client_login CHAR(30) NOT NULL,
                     client_password CHAR(30) NOT NULL,
                     client_email CHAR(30) NOT NULL,
                     PRIMARY KEY(client_id));

CREATE TABLE client_workout (cw_clientid INTEGER NOT NULL,
                             cw_workoutid INTEGER NOT NULL,
                             cw_rating CHAR(10) NOT NULL,
                             PRIMARY KEY(cw_clientid, cw_workoutid));