# -*- encoding:utf-8 -*-
import socket
import argparse

host = 'localhost'

def echo_client(port):
    """
    A simpole echo client
    :param port:
    :return:
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    while True:
        message = str(input("send message: "))

        try:
            print("sending: %s" % message)
            sock.sendall(bytes(message, "utf-8"))
            amount_received = 0
            amount_excepted = len(message)
            return_msg = ""

            # 1 message send area
            while amount_received < amount_excepted:
                data = sock.recv(16)
                amount_received += len(data)
                return_msg += str(data, "utf-8") # 출력을 위한 변수hi
            print(return_msg)
            buf = ""
            while True:
                redata = sock.recv(16)
                # print("readata:",redata)
                # print("re stat:",redata)
                buf += str(redata, "utf-8")
                # print(redata, type(redata), len(redata))
                if len(redata) < 16:
                    break

            print("server:", buf)

        except socket.errno:
            print("socket error: %s" % str(socket.errno))
        except Exception:
            print("other exception: %s" % str(Exception))
        finally:
            print("")
    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='socket server example')
    parser.add_argument('--port', action="store", dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)