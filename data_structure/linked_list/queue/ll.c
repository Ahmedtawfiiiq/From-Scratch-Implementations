#include <stdio.h>
#include "ll.h"

node *create_node(uint64 value)
{
    node *n = (node *)malloc(sizeof(node));
    n->data = value;
    n->next = NULL;
    return n;
}

queue *queue_init(uint8 size)
{
    queue *q = (queue *)malloc(sizeof(queue));
    q->front = NULL;
    q->rear = NULL;
    return q;
}

uint8 isEmpty_queue(queue *q)
{
    if (q->front == NULL)
        return 1;
    else
        return 0;
}

void enqueue(queue *q, uint64 value)
{
    node *n = create_node(value);
    if (isEmpty_queue(q))
    {
        q->front = n;
        q->rear = n;
    }
    else
    {
        q->rear->next = n;
        q->rear = n;
    }
}

uint64 dequeue(queue *q)
{
    if (isEmpty_queue(q))
    {
        printf("Queue is empty\n");
        return -1;
    }
    else
    {
        uint64 value = q->front->data;
        node *d = q->front;
        q->front = q->front->next;
        if (isEmpty_queue(q))
            q->rear = NULL;
        free(d);
        return value;
    }
}
