#include <stdio.h>

#define N 5
int stack[N];
int top = -1;

void push(int x)
{
    if (top == N - 1)
    {
        printf("Stack Overflow\n");
    }
    else
    {
        top++;
        stack[top] = x;
    }
}
void pop()
{
    if (top == -1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        printf("Removed element is %d\n", stack[top]);
        top--;
    }
}
void peek()
{
    if (top == -1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        printf("Top element is %d\n", stack[top]);
    }
}
void display()
{
    printf("\nElements from the top: \n");
    for (int i = top; i >= 0; i--)
    {
        printf("%d\n", stack[i]);
    }
}

int main()
{
    push(10);
    push(20);
    push(30);
    display();
    pop();
    peek();
    display();
    push(10);
    push(20);
    push(30);
    push(10);
    return 0;
}
