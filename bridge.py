#!/usr/bin/python3

'''
Use this script to connect to the car's network to read and send packets. 

A URL must be added bellow in order to connect.

You can either use it as a command-line tool and give the packet as an argument or
change the script to fit your needs
'''

import socketio
import time
import sys
from engineio.payload import Payload

#In case of issues with the connection increase the max_decode_packets value
Payload.max_decode_packets = 100

# Add here the provided docker URL
URL = 'http://localhost:5000/' 


# Init socket
sio = socketio.Client()


@sio.event
def connect():
	print('[!] connection established')

@sio.event
def disconnect():
	print('[!] disconnected from server')


# Event handler that prints the packets emitted from the server
@sio.on('endpoint')
def on_endpoint(data):
	print(data)


print("[!] Connecting to server..")


# Connect to the network
sio.connect(URL) 


# Give a packet as an argument
try: 	
	packet = sys.argv[1]
except:
	pass

print("[!] Sending packets..")


while True:
	# Send data to the server 
	try: 
		sio.emit('endpoint', packet)

	except:
		pass

	# Do NOT remove. Use sleep in between each packet transmission
	# In case of issues with the connection try increasing the sleep time value
	time.sleep(0.1) 

# Close connection
# sio.disconnect() 