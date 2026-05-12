class Ring:

    def __init__(self, num_process=5):
        self.num_process = num_process
        self.active_processes = set(range(1, num_process + 1))
        self.coordinator = num_process

    def election(self, process_id):

        if process_id not in self.active_processes:
            print(f"Process {process_id} is not active")
            return

        print(f"\nProcess {process_id} starts election")

        current = process_id
        next_process = (current % self.num_process) + 1
        highest_id = process_id

        while next_process != process_id:

            if next_process in self.active_processes:

                print(f"Process {current} passes message to Process {next_process}")

                if next_process > highest_id:
                    highest_id = next_process

                current = next_process

            else:
                print(f"Process {next_process} is DOWN")

            next_process = (next_process % self.num_process) + 1

        self.coordinator = highest_id

        print(f"\nProcess {self.coordinator} becomes COORDINATOR")

    def start_election(self, process_id):
        self.election(process_id)

    def bring_up_process(self, process_id):

        if process_id in self.active_processes:
            print(f"Process {process_id} already UP")

        else:
            self.active_processes.add(process_id)
            print(f"Process {process_id} is now UP")

    def bring_down_process(self, process_id):

        if process_id not in self.active_processes:
            print(f"Process {process_id} already DOWN")

        else:
            self.active_processes.remove(process_id)
            print(f"Process {process_id} is now DOWN")

            if self.coordinator == process_id:

                print("Coordinator failed! Starting election...")

                if self.active_processes:
                    starter = min(self.active_processes)
                    self.election(starter)

                else:
                    self.coordinator = None
                    print("No active processes remaining")

    def print_active_processes(self):

        print("\nActive Processes:")

        for process_id in sorted(self.active_processes):
            print(f"Process {process_id}")

    def print_coordinator(self):

        if self.coordinator:
            print(f"\nCoordinator: Process {self.coordinator}")

        else:
            print("\nNo coordinator present")


if __name__ == "__main__":

    ring = Ring()

    while True:

        print("\n-----------------------------")
        print("1) Start Election")
        print("2) Bring Up Process")
        print("3) Bring Down Process")
        print("4) Print Active Processes")
        print("5) Print Coordinator")
        print("6) Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            process_id = int(input("Enter process id: "))
            ring.start_election(process_id)

        elif choice == 2:

            process_id = int(input("Enter process id: "))
            ring.bring_up_process(process_id)

        elif choice == 3:

            process_id = int(input("Enter process id: "))
            ring.bring_down_process(process_id)

        elif choice == 4:

            ring.print_active_processes()

        elif choice == 5:

            ring.print_coordinator()

        elif choice == 6:
            break