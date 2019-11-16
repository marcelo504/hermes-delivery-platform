import sqlite3
import os.path

class client_data:

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

		c.execute("CREATE TABLE clients (id  integer primary key autoincrement ,"
										"name text NOT NULL,"
										"address text NOT NULL,"
										"phone text NOT NULL,"
										"c_cart text)")

		self.conn.commit()

	def new_client(self, client_data):

		if 'name' not in client_data:
			return False

		if 'address' not in client_data:
			return False

		if 'phone' not in client_data:
			return False

		if 'common_cart' not in client_data:
			return False

		# Insert in SQLite

		c = self.conn.cursor()

		c.execute("INSERT INTO clients (name, address, phone, c_cart) VALUES (?,?,?,?)", 
			(client_data['name'],
			client_data['address'],
			client_data['phone'],
			client_data['common_cart']))

		self.conn.commit()


	def edit_client(self, id, field, new_value):
		c = self.conn.cursor()

		if field != 'name' and field != 'address' and field != 'phone' and field != 'common_cart':
			return False

		c.execute("UPDATE TABLE clients SET "+field+"="+new_value+" WHERE id ="+str(id))
		self.conn.commit()

	def get_client_id(self, id):
		c = self.conn.cursor()

		c.execute("SELECT * FROM clients WHERE id="+str(id))

		client = c.fetchall()

		return client[0]

	def view_clients(self):
		c = self.conn.cursor()

		c.execute("SELECT * FROM clients")

		data = c.fetchall()

		print("Clients found:")

		for client in data:
			print(client)
		