import socket


def process():
    host = '127.0.0.1'
    port = 4000

    my_socket = socket.socket()
    my_socket.connect((host, port))

    raw_data1 = input('please give your first value ->  ')
    raw_data2 = input('please give your second value ->  ')

    my_socket.send(raw_data1.encode('utf-8'))
    my_socket.send(raw_data2.encode('utf-8'))
    data = my_socket.recv(1024).decode('utf-8')
    print('the total of your both input is: ' + data)
    my_socket.close()

process()
