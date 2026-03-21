# features add message to file and show all logs
def add_log():
    msg = input("Enter message: ")
    with open("log.txt", "a") as file:
        file.write(msg + "\n")

def view_logs():
    with open("log.txt", "r") as file:
        print(file.read())

while True:
    print("\n1 Add Log")
    print("2 View Logs")
    print("3 Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_log()
    elif choice == "2":
        view_logs()
    elif choice == "3":
        break