
# Database Implementations
import core.database.client_data as client_class
import core.database.delivery_data as delivery_class
import core.database.deliveryman_data as delman_class



# # Database objects Setup
# client_obj = client_class.client_data('client_database.db')
# delivery_obj = delivery_class.delivery_data('deliveries_database.db')
# delman_obj = delman_class.deliveryman_data('deliverymen_database.db')

# client_test = {
# 	'name':'John',
# 	'address':'Fake Address',
# 	'phone':'Fake Phone',
# 	'common_cart':None
# }

# #client_obj.new_client(client_test)
# client_obj.view_clients()

# delivery_test = {
# 	'client_id':1,
# 	'delman_id':1,
# 	'description':'Some Stuff',
# 	'priority':'HIGH'
# }

# #delivery_obj.new_delivery(delivery_test)

# delivery_obj.view_deliveries()

# delman_test = {
# 	'name':'Jimmy',
# 	'phone':'SomePhone'
# }

# delman_obj.new_deliveryman(delman_test)

# delman_obj.view_deliverymen()



### MAIN IMPLEMENTATION ###

import signal
import threading
import os

# Database Implementations classes
import core.database.client_data as client_class
import core.database.delivery_data as delivery_class
import core.database.deliveryman_data as delman_class

# Server Connector
import core.server_connector as server_class

#Termination Event
term_event = threading.Event()

project_name = '[Hermes - Delivery Platform]'

def abort_trigger(signal, frame):
	global term_event
	term_event.set()

def hermes_main():

	# Database objects Setup
	client_obj = client_class.client_data('client_database.db')
	delivery_obj = delivery_class.delivery_data('deliveries_database.db')
	delman_obj = delman_class.deliveryman_data('deliverymen_database.db')

	# Setup Termination Signals
	signal.signal(signal.SIGTERM, abort_trigger)
	signal.signal(signal.SIGINT, abort_trigger)

	# Setup Flask Class
	server = server_class.server_class(1,"server_thread",client_obj, delivery_obj, delman_obj)

	server.run()

	print(project_name+" Startup Complete")

	while term_event.is_set() == False:
		term_event.wait(0.5)

	server.stop()

	print(project_name+" Ending...")

	pass

if __name__ == "__main__":
	hermes_main()