n=5
active=set(range(1,n+1))
coord=n

def election(pid):
    global coord

    if pid not in active:
        print(f"Process {pid} is not active")
        return

    print(f"\nProcess {pid} starts election")

    curr=pid
    nxt=(curr%n)+1
    high=pid

    while nxt!=pid:

        if nxt in active:

            print(f"Process {curr} passes message to Process {nxt}")

            if nxt>high:
                high=nxt

            curr=nxt

        else:
            print(f"Process {nxt} is DOWN")

        nxt=(nxt%n)+1

    coord=high
    print(f"\nProcess {coord} becomes COORDINATOR")

def up(pid):

    if pid in active:
        print(f"Process {pid} already UP")

    else:
        active.add(pid)
        print(f"Process {pid} is now UP")

def down(pid):
    global coord

    if pid not in active:
        print(f"Process {pid} already DOWN")

    else:
        active.remove(pid)
        print(f"Process {pid} is now DOWN")

        if coord==pid:
            print("Coordinator failed! Starting election...")

            if active:
                start=min(active)
                election(start)

            else:
                coord=None
                print("No active processes remaining")

def print_active():
    print("\nActive Processes:")

    for pid in sorted(active):
        print(f"Process {pid}")

def print_coord():

    if coord:
        print(f"\nCoordinator: Process {coord}")

    else:
        print("\nNo coordinator present")

while True:

    print("\n-----------------------------")
    print("1) Start Election")
    print("2) Bring Up Process")
    print("3) Bring Down Process")
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
