import jaydebeapi

class connection:
	def __init__(self):
		driver_name = "org.apache.ignite.IgniteJdbcThinDriver"
		url = "jdbc:ignite:thin://localhost:10800"
		lib = "/home/david/ignite/apache-ignite-fabric-2.6.0-bin/libs/ignite-core-2.6.0.jar"
		self.conn = jaydebeapi.connect(driver_name, url, [] , lib, lib)	

	def get_connection(self):
		return self.conn

	def get_cursor(self):
		return self.conn.cursor()

	def close(self):
		self.conn.close()