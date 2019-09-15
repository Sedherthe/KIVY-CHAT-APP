import socket

    ## Create a socket for server role ##
# The address family, kind of socket to use. STREAM here.
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	print('Server Socket successfully created')
except socket.error as err:
	print(f'Socket creating failed with {err}')

# Bind assigns a local protocol address to a socket.It is a combination of IPv4 + Port (16bit) address.
s.bind((socket.gethostbyname('localhost'), 1234))
s.listen(5) # Called by the TCP server.Int indicates max num of connections kernel should queue.

while True:
	# Accept the connection reqeust from a client socket
	clientsocket, address = s.accept()
	print(f'Connection from {address} established!!')
	# It is byte stream by default.
	clientsocket.send(bytes("Welcome to the Server", 'utf-8'))
	clientsocket.close()