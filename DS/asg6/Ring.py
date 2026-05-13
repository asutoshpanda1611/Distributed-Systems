num_process=5
active_processes=set(range(1,num_process+1))
coordinator=num_process

def election(process_id):
    global coordinator

    if process_id not in active_processes:
        print(f"Process {process_id} is not active")
        return

    print(f"\nProcess {process_id} starts election")

    current=process_id
    next_process=(current%num_process)+1
    highest_id=process_id

    while next_process!=process_id:

        if next_process in active_processes:

            print(f"Process {current} passes message to Process {next_process}")

            if next_process>highest_id:
                highest_id=next_process

            current=next_process

        else:
            print(f"Process {next_process} is DOWN")

        next_process=(next_process%num_process)+1

    coordinator=highest_id
    print(f"\nProcess {coordinator} becomes COORDINATOR")

def bring_up_process(process_id):

    if process_id in active_processes:
        print(f"Process {process_id} already UP")

    else:
        active_processes.add(process_id)
        print(f"Process {process_id} is now UP")

def bring_down_process(process_id):
    global coordinator

    if process_id not in active_processes:
        print(f"Process {process_id} already DOWN")

    else:
        active_processes.remove(process_id)
        print(f"Process {process_id} is now DOWN")

        if coordinator==process_id:
            print("Coordinator failed! Starting election...")

            if active_processes:
                starter=min(active_processes)
                election(starter)

            else:
                coordinator=None
                print("No active processes remaining")

def print_active_processes():

    print("\nActive Processes:")
    for process_id in sorted(active_processes):
        print(f"Process {process_id}")

def print_coordinator():

    if coordinator:
        print(f"\nCoordinator: Process {coordinator}")

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

    choice=int(input("Enter choice: "))

    if choice==1:

        process_id=int(input("Enter process id: "))
        election(process_id)

    elif choice==2:

        process_id=int(input("Enter process id: "))
        bring_up_process(process_id)

    elif choice==3:

        process_id=int(input("Enter process id: "))
        bring_down_process(process_id)

    elif choice==4:
        print_active_processes()

    elif choice==5:
        print_coordinator()

    elif choice==6:
        break
