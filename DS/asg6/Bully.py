import random

num_process=5
state=[True]*num_process
leader=num_process

def election(process_id):
    global leader
    print(f"\nProcess {process_id} starts election")
    coordinator=process_id

    for i in range(process_id+1,num_process+1):
        if state[i-1]:
            print(f"Process {process_id} sends ELECTION to Process {i}")
            print(f"Process {i} replies OK")
            coordinator=i

    print(f"Process {coordinator} sends COORDINATOR message")
    leader=coordinator
    print(f"Process {leader} is now coordinator")

def up(process_id):
    if state[process_id-1]:
        print(f"Process {process_id} already UP")

    else:
        state[process_id-1]=True
        print(f"Process {process_id} is now UP")
        election(process_id)

def down(process_id):
    global leader
    if not state[process_id-1]:
        print(f"Process {process_id} already DOWN")

    else:
        state[process_id-1]=False
        print(f"Process {process_id} is now DOWN")

        if leader==process_id:
            print("Coordinator failed! Starting election...")
            active=[i+1 for i,s in enumerate(state) if s]

            if active:
                election(random.choice(active))

            else:
                leader=None
                print("No active processes remaining")

def message(process_id):
    if not state[process_id-1]:
        print(f"Process {process_id} is DOWN")
        return

    print(f"\nProcess {process_id} sends message")

    if leader and state[leader-1]:
        print(f"Coordinator {leader} is alive -> OK")

    else:
        print("Coordinator not responding")
        election(process_id)

print("Processes UP: p1 p2 p3 p4 p5")
print(f"Initial Coordinator: Process {leader}")

while True:

    print("\n----------------------")
    print("1) UP a process")
    print("2) DOWN a process")
    print("3) Send Message")
    print("4) Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        pid=int(input("Enter process id: "))
        up(pid)

    elif choice==2:
        pid=int(input("Enter process id: "))
        down(pid)

    elif choice==3:
        pid=int(input("Enter process id: "))
        message(pid)

    elif choice==4:
        break
