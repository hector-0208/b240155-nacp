# Initialize an empty list and set the maximum capacity
queue = []
N = 5

def enqueue(x):
    # Check if the queue has reached its maximum capacity
    if len(queue) >= N:
        print("Queue Overflow")
    else:
        # .append() adds the item to the "rear" (end) of the list
        queue.append(x)

def dequeue():
    # Check if the queue is empty
    if not queue:
        print("Queue Underflow")
    else:
        # In a queue, we remove from the "front" (index 0)
        item = queue[0]
        del queue[0] 
        print(f"Removed element is {item}")
        
        # Alternatively, you can use the built-in pop method with index 0:
        # item = queue.pop(0)
        # print(f"Removed element is {item}")

def peek():
    if not queue:
        print("Queue Underflow")
    else:
        # The front of the queue is always at index 0
        print(f"Top (front) element is {queue[0]}")

def display():
    print("\nElements from front:")
    # We can just iterate through the list normally, as index 0 is the front
    for item in queue:
        print(item)

if __name__ == "__main__":
    enqueue(1)
    enqueue(2)
    enqueue(3)
    enqueue(4)
    display()
    
    dequeue()
    display()
    
    peek()
    
    enqueue(5)
    enqueue(6) # This will trigger the overflow since capacity is 5 and we have 4 items
