# Queue is FIFO First inserted element will remove first
# Queue supports two operations Enqueue (Adding element ) Dequeue (Removing element)
queue  = []

def enqueue():
    e = input("Enter the element :")
    queue.append(e)

def dequeue():
    if len(queue) == 0:
        print("queue is empty")
    else:
       queue.pop(0)

def display():
    print(queue)


while True:
    print("Enter the operation 1 for enqueue and 2 for dequeue 3 for quit 4 for display the queue")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        print("End of the program")
        break
    elif choice == 4:
        display()

    else:
        print("Kindly enter the valid number")