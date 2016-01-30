# -*- encoding:utf-8 -*-
import socket
import sys
import argparse

host = 'localhost'
data_payload = 1024 * 2
back_log = 5

def echo_server(port):
    """
    a simple echo server
    :param port:
    :return:
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address =(host,port)
    print("Starting up echo server on %s port %s" %(server_address))
    sock.bind(server_address)
    sock.listen(back_log)
    client, address = sock.accept()

    while True:
        print("waiting to receive message from client")
        #receive from client
        data = client.recv(data_payload)

        if data:
            print("Data: %s" % data) #only message from client
            # print("Data: %s" % str(data,"utf-8") #only message from client
            client.send(data)
            reply = str(input("reply: "))
            receive_amount = 0
            excepted_amount = len(reply)
            while receive_amount < excepted_amount:
                receive_amount += len(reply)
                client.sendall(bytes(reply,"utf-8"))
            # 여기서부터 추가해야함
            print("sent %s bytes back to %s" %(data, address))
    client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='socket server Example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)