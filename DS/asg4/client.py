import socket
import time
import json

HOST = "127.0.0.1"
PORT = 5000

def get_time():
    return int(time.time() * 1000)

def show(t):
    return time.strftime("%H:%M:%S", time.localtime(t / 1000))

c = socket.socket()
c.connect((HOST, PORT))

local_time = get_time()

print("Connected to Server")
print("Initial Client Time:", show(local_time))

while True:
    data = json.loads(c.recv(1024).decode())

    if data["op"] == "time_req":

        c.send(json.dumps({
            "time":local_time
        }).encode())

    elif data["op"] == "adjust":

        adj = data["value"]

        print("Adjustment Received:", adj, "ms")

        local_time += adj

        print("Final Time:", show(local_time))

        break

c.close()