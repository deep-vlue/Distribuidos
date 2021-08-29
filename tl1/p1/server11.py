

import socket


server_address = (('0.0.0.0', 8090))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_address)
server.listen()

message = 'I am SERVER\n'

while True:
	print('Server disponible!')
	connection, client_address = server.accept()
	from_client = ''

	while True:
		data = connection.recv(4096)

		from_client += data.decode()
		if not data: break
		connection.send(from_client.encode('utf-8'))

	print(from_client)

	connection.close()
	print('cliente desconectado \n')

