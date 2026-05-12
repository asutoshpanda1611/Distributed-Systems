import socket,time

SERVER=("localhost",8080)
BUFFER_SIZE=1024

s=socket.socket()
s.connect(SERVER)

while True:
    try:
        data=s.recv(BUFFER_SIZE).decode()

        if data=="TOKEN":
            print("Token received")
            print("Working on resource...")
            time.sleep(2)

            print("Releasing token\n")
            s.send("TOKEN".encode())

    except:
        break

s.close()