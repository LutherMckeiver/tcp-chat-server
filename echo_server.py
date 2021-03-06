import socket


def setup_server():
    echo_server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP,
        )


# Bind an endpoint (HOST, PORT) to the socket
    echo_server.bind(('127.0.0.1', 8000))
# Activate the listener for the socket
    echo_server.listen(1)

    return echo_server, echo_server.accept()


if __name__ == '__main__':
    server, (conn, addr) = setup_server()
    print(f'Receieved a client connections for {addr}')

    buffer_length = 16
    message_complete = False
    message = ''

    while not message_complete:
        part = conn.recv(buffer_length)
        message += part.decode()
        if len(part) < buffer_length:
            break

    conn.sendall(message.encode())

    conn.close()
    server.close()
