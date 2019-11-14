import sqlite3
import os.path

class deliveryman_data:

	#SQLite Connector
	conn = None

	def __init__(self, file_path):
		
		#SQLite File Path
		self.sqlite_path = file_path

		if not os.path.exists(self.sqlite_path):
			self.init_database()
		else:
			self.conn = sqlite3.connect(self.sqlite_path)


	def init_database(self):
		self.conn = sqlite3.connect(self.sqlite_path)

		c = self.conn.cursor()

		c.execute("CREATE TABLE deliverymen (id  integer primary key autoincrement ,"
										"name text NOT NULL,"
										"phone text NOT NULL"
										")")

		self.conn.commit()

	def new_deliveryman(self, client_data):

		if 'name' not in client_data:
			return False

		if 'phone' not in client_data:
			return False

		# Insert in SQLite

		c = self.conn.cursor()

		c.execute("INSERT INTO deliverymen (name, phone) VALUES (?,?)", 
			(client_data['name'],
			client_data['phone']))

		self.conn.commit()


	def edit_client(self, id, field, new_value):
		c = self.conn.cursor()

		if field != 'name' and field != 'phone':
			return False

		c.execute("UPDATE TABLE deliverymen SET "+field+"="+new_value+" WHERE id =?",id)
		pass


	def view_deliverymen(self):
		c = self.conn.cursor()

		c.execute("SELECT * FROM deliverymen")

		data = c.fetchall()

		print("Deliverymen found:")

		for client in data:
			print(client)
		