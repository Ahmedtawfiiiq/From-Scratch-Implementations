#include "ll.h"

node *create_node(uint64 value)
{
    node *n = (node *)malloc(sizeof(node));
    n->data = value;
    n->next = NULL;
    return n;
}

stack *stack_init(uint8 size)
{
    stack *s = (stack *)malloc(sizeof(stack));
    s->top = NULL;
    return s;
}

uint8 isEmpty(stack *s)
{
    if (s->top == NULL)
        return 1;
    else
        return 0;
}

void push(stack *s, uint64 value)
{
    node *n = create_node(value);
    if (isEmpty(s))
        s->top = n;
    else
    {
        n->next = s->top;
        s->top = n;
    }
}

uint64 pop(stack *s)
{
    if (!isEmpty(s))
    {
        uint64 value = s->top->data;
        node *d = s->top;
        s->top = s->top->next;
        free(d);
        return value;
    }
    else
    {
        printf("Stack is empty\n");
        return -1;
    }
}
