import random

class Bully:

    def __init__(self, num_process=5):
        self.num_process = num_process
        self.state = [True] * num_process
        self.leader = num_process

    def election(self, process_id):

        print(f"\nProcess {process_id} starts election")

        coordinator = process_id

        for i in range(process_id + 1, self.num_process + 1):

            if self.state[i - 1]:
                print(f"Process {process_id} sends ELECTION to Process {i}")
                print(f"Process {i} replies OK")
                coordinator = i

        print(f"Process {coordinator} sends COORDINATOR message")
        self.leader = coordinator

        print(f"Process {self.leader} is now coordinator")

    def up(self, process_id):

        if self.state[process_id - 1]:
            print(f"Process {process_id} already UP")

        else:
            self.state[process_id - 1] = True
            print(f"Process {process_id} is now UP")

            self.election(process_id)

    def down(self, process_id):

        if not self.state[process_id - 1]:
            print(f"Process {process_id} already DOWN")

        else:
            self.state[process_id - 1] = False
            print(f"Process {process_id} is now DOWN")

            if self.leader == process_id:

                print("Coordinator failed! Starting election...")

                active = [i + 1 for i, s in enumerate(self.state) if s]

                if active:
                    self.election(random.choice(active))

                else:
                    self.leader = None
                    print("No active processes remaining")

    def message(self, process_id):

        if not self.state[process_id - 1]:
            print(f"Process {process_id} is DOWN")
            return

        print(f"\nProcess {process_id} sends message")

        if self.leader and self.state[self.leader - 1]:
            print(f"Coordinator {self.leader} is alive -> OK")

        else:
            print("Coordinator not responding")
            self.election(process_id)


if __name__ == "__main__":

    bully = Bully()

    print("Processes UP: p1 p2 p3 p4 p5")
    print(f"Initial Coordinator: Process {bully.leader}")

    while True:

        print("\n----------------------")
        print("1) UP a process")
        print("2) DOWN a process")
        print("3) Send Message")
        print("4) Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            pid = int(input("Enter process id: "))
            bully.up(pid)

        elif choice == 2:

            pid = int(input("Enter process id: "))
            bully.down(pid)

        elif choice == 3:

            pid = int(input("Enter process id: "))
            bully.message(pid)

        elif choice == 4:
            break