#include <stdio.h>

#define N 5
int queue[N];
int front = -1;
int rear = -1;
void enqueue(int x)
{
    if (rear == N - 1)
    {
        printf("Queue Overflow\n");
    }
    else if (front == -1 && rear == -1)
    {
        front = rear = 0;
        queue[rear] = x;
    }
    else
    {
        rear++;
        queue[rear] = x;
    }
}
void dequeue()
{
    if (front == -1 && rear == -1)
    {
        printf("Queue Underflow\n");
    }
    else if (front == rear)
    {
        front = rear = -1;
    }
    else
    {
        printf("Removed element is %d\n", queue[front]);
        front++;
    }
}
void peek()
{
    if (front == -1 && rear == -1)
    {
        printf("Queue Underflow\n");
    }
    else
    {
        printf("Top element is %d\n", queue[front]);
    }
}
void display(){
    printf("\nElements from front: \n");
    for(int i = front; i <= rear; i++)
    {
        printf("%d\n", queue[i]);
    }
}
int main()
{
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    display();
    dequeue();
    display();
    peek();
    enqueue(5);
    enqueue(6);
    return 0;
}
