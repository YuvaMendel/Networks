import socket

def SendBySize(socket, msg):
    if not int(msg[:4]) == 0:
        try:
            if type(msg) != bytes:
                msg = msg.encode()
            socket.sendall(msg)
        except OSError as err:
            print(err)

def RecvBySize(sock, size):
    try:
        buffer = b''
        while size:
            new_bufffer = sock.recv(size)
            if not new_bufffer:
                return b''
            buffer += new_bufffer
            size -= len(new_bufffer)
        return buffer
    except socket.error as e:
        print(f"socket does not exist, disconnecting it")
        return None