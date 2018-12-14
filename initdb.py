from connection import connection
from my_parser import *

print("Connecting to server...")

try:
	conn = connection()
	create_table_queries = get_create_table_queries("create.sql")

	cur = conn.get_cursor()

	for i in range(len(create_table_queries)):
		cur.execute(create_table_queries[i])

	print("Connection complite")

	tbls_path = ["data/club.tbl", "data/coach.tbl", "data/sport.tbl",\
		"data/workout.tbl", "data/client.tbl", "data/client_workout.tbl"]

	print("Start parcing...")
	insert_into_table_queries = get_insert_into_table_queries(tbls_path)
	print("Parcing complite")

	print("Start putting...")
	for i in range(len(insert_into_table_queries)):
		cur.execute(insert_into_table_queries[i])
	print("Putting complite")

except Exception as e:
	print("Connection to server is failed")
	print(e)
