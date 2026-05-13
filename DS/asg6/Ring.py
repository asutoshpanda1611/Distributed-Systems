n=5
state=[True]*n
coord=n

def election(pid):
    global coord

    if not state[pid-1]:
        print(f"Process {pid} is not active")
        return

    print(f"\nProcess {pid} starts election")

    curr=pid
    next_process=(curr%n)+1
    coord_id=pid

    while next_process!=pid:
        if state[next_process-1]:
            print(f"Process {curr} passes ELECTION to Process {next_process}")

            if next_process>coord_id:
                coord_id=next_process

            curr=next_process

        else:
            print(f"Process {next_process} is DOWN")

        next_process=(next_process%n)+1

    print(f"\nProcess {coord_id} sends COORDINATOR message")

    coord=coord_id
    print(f"Process {coord} is now coordinator")

def up(pid):
    if state[pid-1]:
        print(f"Process {pid} already UP")

    else:
        state[pid-1]=True
        print(f"Process {pid} is now UP")

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
                election(active[0])

            else:
                coord=None
                print("No active processes remaining")

def print_active():
    print("\nActive Processes:")
    for i,s in enumerate(state):
        if s:
            print(f"Process {i+1}")

def print_coord():
    if coord and state[coord-1]:
        print(f"\nCoordinator: Process {coord}")

    else:
        print("\nNo coordinator present")

while True:

    print("\n----------------------")
    print("1) Start Election")
    print("2) UP a process")
    print("3) DOWN a process")
    print("4) Print Active Processes")
    print("5) Print Coordinator")
    print("6) Exit")

    ch=int(input("Enter choice: "))

    if ch==1:
        pid=int(input("Enter process id: "))
        election(pid)

    elif ch==2:
        pid=int(input("Enter process id: "))
        up(pid)

    elif ch==3:
        pid=int(input("Enter process id: "))
        down(pid)

    elif ch==4:
        print_active()

    elif ch==5:
        print_coord()

    elif ch==6:
        break
