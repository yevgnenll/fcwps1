import socket

def get_remote_machine_info(host):
    try:
        print("ip address of %s: %s" %(host, socket.gethostbyname(host)))
    except socket.error:
        print("%s: %s" %(host, socket.error))

#
# if __name__ == '__main__':
#     get_remote_machine_info()


get_remote_machine_info('www.fastcampus.co.kr')
get_remote_machine_info('www.google.co.kr')
get_remote_machine_info('www.naver.com')
# ip 는bin 값으로 변환해야한다


def convert_integer():
    data = 1234
    # 32bit
    print("original: %s -> long byte order: %x, network byte order: %x" %(data, socket.ntohl(data), socket.htonl(data)))

    # 16bit
    print("original: %s -> short byte order: %x, network byte order: %x" %(data, socket.ntohs(data), socket.htons(data)))

    # 32bit
    print("original: %s -> long byte order: %s, network byte order: %s" %(data, socket.ntohl(data), socket.htonl(data)))

    # 16bit
    print("original: %s -> short byte order: %s, network byte order: %s" %(data, socket.ntohs(data), socket.htons(data)))


convert_integer()

