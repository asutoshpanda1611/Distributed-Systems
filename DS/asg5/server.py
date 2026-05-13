import socket,threading

TOKEN="TOKEN"
PORT=8080
BUFFER_SIZE=1024

clients=[]
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def start_server():

    server_socket.bind(("localhost",PORT))
    server_socket.listen()
    print("Server Started")

    while True:

        client_socket,addr=server_socket.accept()
        name=f"Client-{len(clients)+1}"
        clients.append((client_socket,name))
        print(f"{name} connected")

        if len(clients)==1:
            print(f"Sending token to {name}")
            client_socket.send(TOKEN.encode())

        threading.Thread(
            target=handle_client,
            args=(client_socket,name)
        ).start()

def handle_client(client_socket,name):
    global clients

    while True:
        try:
            data=client_socket.recv(BUFFER_SIZE).decode()

            if not data:
                raise Exception()

            i=[c[0] for c in clients].index(client_socket)

            next_client,next_name=clients[
                (i+1)%len(clients)
            ]

            if data=="TOKEN":
                print(f"Sending token to {next_name}")

                next_client.send(TOKEN.encode())

        except:
            print(f"{name} disconnected")

            if (client_socket,name) in clients:
                clients.remove((client_socket,name))

            client_socket.close()
            break

start_server()
