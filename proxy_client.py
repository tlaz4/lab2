#!/usr/bin/env python3
import socket

HOST = "localhost"
PORT = 8081
BUFFER_SIZE = 1024

# had to change payload to this in order to not get a 404 error
payload = "GET / HTTP/1.0\r\n\r\n"

def conn_socket(addr_tup):
    (family, socktype, proto, canonname, sockaddr) = addr_tup
    try:
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())

        s.shutdown(socket.SHUT_WR)
        
        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data

        print("client data is: ", full_data)
    except e:
        print(e)
        pass
    finally:
        s.close()

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    #print(addr_info)
    for addr_tup in addr_info:
        conn_socket(addr_tup) 
        # only ipv4 I guess
        break

if __name__ == "__main__":
    main()

