import socket,threading

TOKEN="TOKEN"
PORT=8080
BUFFER_SIZE=1024

class TokenRingServer:
    def __init__(self):
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.clients=[]
        self.running=True

    def start(self):
        self.server_socket.bind(("localhost",PORT))
        self.server_socket.listen()

        print("Server Started")

        while self.running:
            client_socket,addr=self.server_socket.accept()

            name=f"Client-{len(self.clients)+1}"
            self.clients.append((client_socket,name))

            print(f"{name} connected")

            if len(self.clients)==1:
                print(f"Sending token to {name}")
                client_socket.send(TOKEN.encode())

            threading.Thread(
                target=self.handle_client,
                args=(client_socket,name)
            ).start()

    def handle_client(self,client_socket,name):
        while self.running:
            try:
                data=client_socket.recv(BUFFER_SIZE).decode()

                if not data:
                    raise Exception()

                i=[c[0] for c in self.clients].index(client_socket)

                next_client,next_name=self.clients[
                    (i+1)%len(self.clients)
                ]

                if data=="TOKEN":
                    print(f"Sending token to {next_name}")
                    next_client.send(TOKEN.encode())

            except:
                print(f"{name} disconnected")

                if (client_socket,name) in self.clients:
                    self.clients.remove((client_socket,name))

                client_socket.close()
                break

if __name__=="__main__":
    TokenRingServer().start()