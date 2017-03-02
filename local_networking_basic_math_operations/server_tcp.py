import socket


def execute():
    host = '127.0.0.1'
    port = 4000

    my_socket = socket.socket()
    my_socket.bind((host, port))

    my_socket.listen(1)
    c, address = my_socket.accept()

    print('Get connection from: ' + str(address))

    data1 = c.recv(1024).decode('utf-8')
    data2 = c.recv(1024).decode('utf-8')

    print('From client data received: ' + str(data1) + ' & ' + str(data2))
    total = int(data2) + int(data1)
    print('total of the two data is: ' + str(total))
    total = str(total)
    c.send(total.encode('utf-8'))
    c.close()

execute()
