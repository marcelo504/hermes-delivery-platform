import sqlite3
import os.path

class delivery_data:

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

		c.execute("CREATE TABLE deliveries (id  integer primary key autoincrement,"
										"client_id integer NOT NULL,"
										"description text,"
										"status text,"
										"priority text,"
										"created_at datetime default CURRENT_TIMESTAMP,"
										"delivered_at datetime,"
										"delman_id integer"
										")")

		self.conn.commit()

	def new_delivery(self, delivery_data):

		if 'client_id' not in delivery_data:
			return False

		if 'description' not in delivery_data:
			return False

		if 'priority' not in delivery_data:
			return False

		if 'delman_id' not in delivery_data:
			return False

		# Insert in SQLite

		c = self.conn.cursor()

		c.execute("INSERT INTO deliveries (client_id, description, priority, status, delman_id) VALUES (?,?,?,?,?)", 
			(delivery_data['client_id'],
			delivery_data['description'],
			"Waiting",
			delivery_data['priority'],
			delivery_data['delman_id']))

		self.conn.commit()

	def edit_delivery(self, id, field, new_value):
		c = self.conn.cursor()

		if field != 'client_id' and field != 'description' and field != 'status' and field != 'delman_id':
			return False

		c.execute("UPDATE TABLE deliveries SET "+field+"="+new_value+" WHERE id ="+id)
		self.conn.commit()

	def get_deliveries(self):
		c = self.conn.cursor()

		c.execute("SELECT * FROM deliveries")

		return c.fetchall()

	def view_deliveries(self):
		c = self.conn.cursor()

		c.execute("SELECT * FROM deliveries")

		data = c.fetchall()

		print("Deliveries found:")

		for client in data:
			print(client)
		