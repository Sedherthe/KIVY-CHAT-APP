import socket

HEADERSIZE = 10

s = socket.socket()
s.connect((socket.gethostbyname('localhost'), 1234))

while True:

	full_msg = ''
	new_msg = True

	while True:
		
		msg = s.recv(16) # Receive the 16 len strings.
		msg = msg.decode('utf-8')
		print(f'Message received is : {msg}')

		if new_msg:
			print(f'New message lengthgs: {msg[:HEADERSIZE]}')
			msglen = int(msg[:HEADERSIZE]) # The message length is send in the first 10 bits of the string.
			new_msg = False
		
		full_msg += msg # The encoding scheme used.
		
		if len(full_msg) - HEADERSIZE == msglen:
			print("Full message received")
			print(full_msg[HEADERSIZE:]) # First headersize bits contain the size of the message at max.
			new_msg = True
			full_msg = ''
		
	print(f'The Final message received is : {full_msg}.')