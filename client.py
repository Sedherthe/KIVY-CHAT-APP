import socket

s = socket.socket()
s.connect((socket.gethostbyname('localhost'), 1234))

full_msg = ''
while True:
	msg = s.recv(8)
	if len(msg) <= 0:
		break
	full_msg += msg.decode('utf-8') # The encoding scheme used.
	print(f'Message received is : {msg}')
print(f'The message received is : {full_msg}.')