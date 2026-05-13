import random

n=5
state=[True]*n
coord=n

def election(pid):
    global coord
    print(f"\nProcess {pid} starts election")
    coord_id=pid

    for i in range(pid+1,n+1):
        if state[i-1]:
            print(f"Process {pid} sends ELECTION to Process {i}")
            print(f"Process {i} replies OK")
            coord_id=i

    print(f"Process {coord_id} sends COORDINATOR message")
    coord=coord_id
    print(f"Process {coord} is now coordinator")

def up(pid):
    if state[pid-1]:
        print(f"Process {pid} already UP")

    else:
        state[pid-1]=True
        print(f"Process {pid} is now UP")
        election(pid)

def down(pid):
    global coord
    if not state[pid-1]:
        print(f"Process {pid} already DOWN")

    else:
        state[pid-1]=False
        print(f"Process {pid} is now DOWN")

        if coord==pid:
            print("Coordinator failed! Starting election...")
            active=[i+1 for i,s in enumerate(state) if s]

            if active:
                election(random.choice(active))

            else:
                coord=None
                print("No active processes remaining")

def msg(pid):
    if not state[pid-1]:
        print(f"Process {pid} is DOWN")
        return

    print(f"\nProcess {pid} sends message")

    if coord and state[coord-1]:
        print(f"Coordinator {coord} is alive -> OK")

    else:
        print("Coordinator not responding")
        election(pid)

print("Processes UP: p1 p2 p3 p4 p5")
print(f"Initial Coordinator: Process {coord}")

while True:

    print("\n----------------------")
    print("1) UP a process")
    print("2) DOWN a process")
    print("3) Send Message")
    print("4) Exit")

    ch=int(input("Enter choice: "))

    if ch==1:
        pid=int(input("Enter process id: "))
        up(pid)

    elif ch==2:
        pid=int(input("Enter process id: "))
        down(pid)

    elif ch==3:
        pid=int(input("Enter process id: "))
        msg(pid)

    elif ch==4:
        break
