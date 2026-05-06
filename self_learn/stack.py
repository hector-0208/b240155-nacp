stack = []
N = 5

def push(x):
    if len(stack) >= N:
        print("Stack Overlow")
    else:
        stack.append(x)
def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print(f"Removed element is {stack[-1]}")
        del stack[-1]
        # or just write
        # stack.pop()
def peek():
    if not stack:
        print("Stack Underflow")
    else:
        print(f"Top element is {stack[-1]}")
def display():
    print("\nDisplaying from top: ")
    for i in reversed(stack):
        print(i)
        
push(10)
push(20)
push(30)
display()
pop()
peek()
display()
push(10)
push(20)
push(30)
push(10)

