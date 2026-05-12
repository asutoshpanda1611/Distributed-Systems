import socket
import time
import json

HOST = "127.0.0.1"
PORT = 5000

def get_time():
    return int(time.time() * 1000)

def show(t):
    return time.strftime("%H:%M:%S", time.localtime(t / 1000))

s = socket.socket()
s.bind((HOST, PORT))
s.listen(5)

server_time = get_time()

print("Server Started")
print("Server Time:", show(server_time))

clients = []

while True:
    c, addr = s.accept()
    print("Connected:", addr)

    clients.append(c)

    ch = input("Add more clients? (y/n): ")
    if ch == "n":
        break

times = []

for c in clients:
    c.send(json.dumps({"op":"time_req"}).encode())

    data = json.loads(c.recv(1024).decode())
    t = data["time"]

    times.append(t)

    print("Client Time:", show(t))

avg = (server_time + sum(times)) // (len(times) + 1)

print("Synchronized Time:", show(avg))

for i, c in enumerate(clients):
    adjust = avg - times[i]

    c.send(json.dumps({
        "op":"adjust",
        "value":adjust
    }).encode())

    print("Adjustment Sent:", adjust, "ms")

    c.close()

s.close()