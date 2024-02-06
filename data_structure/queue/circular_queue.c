#include <stdio.h>
#include <stdlib.h>
#include "circular_queue.h"

queue *queue_init(uint8 size)
{
    queue *q = (queue *)malloc(sizeof(queue));
    q->items = (uint64 *)malloc(size * sizeof(uint64));
    q->front = 0;
    q->rear = 0;
    q->capcity = size;
    q->n = 0;
    return q;
}

void enqueue(queue *q, uint64 value)
{
    if (isFullQueue(q))
    {
        printf("Queue is full\n");
    }
    else
    {
        q->items[q->rear] = value;
        q->rear += 1;
        q->rear %= q->capcity; // circular queue
        q->n += 1;
    }
}

uint64 dequeue(queue *q)
{
    if (isEmptyQueue(q))
    {
        printf("Queue is empty\n");
        return -1;
    }
    else
    {
        uint64 value = q->items[q->front];
        q->front += 1;
        q->front %= q->capcity; // circular queue
        q->n -= 1;
        return value;
    }
}

uint8 isEmptyQueue(queue *q)
{
    if (q->n == 0)
        return 1;
    else
        return 0;
}

uint8 isFullQueue(queue *q)
{
    if (q->n == q->capcity)
        return 1;
    else
        return 0;
}

void dispose(queue *q)
{
    free(q->items);
    free(q);
}

uint64 getFirst(queue *q)
{
    return q->items[q->front];
}

uint64 getLast(queue *q)
{
    if (q->rear == 0)
        return q->items[q->capcity - 1];
    else
        return q->items[q->rear - 1];
}

void displayQueue(queue *q)
{
    queue *c = queue_init(q->n);
    while (!isEmptyQueue(q))
    {
        uint64 value = dequeue(q);
        printf("%ld ", value);
        enqueue(c, value);
    }
    printf("\n");
    while (!isEmptyQueue(c))
        enqueue(q, dequeue(c));
}

uint64 getMinimum(queue *q)
{
    queue *c = queue_init(q->n);
    uint64 min = dequeue(q);
    enqueue(c, min);
    while (!isEmptyQueue(q))
    {
        uint64 value = dequeue(q);
        if (value < min)
            min = value;
        enqueue(c, value);
    }
    while (!isEmptyQueue(c))
        enqueue(q, dequeue(c));
    return min;
}

void reverse(queue *q)
{
    if (!isEmptyQueue(q))
    {
        uint8 value = dequeue(q);
        reverse(q);
        enqueue(q, value);
    }
}

void enqueue_stack(stack *s, uint8 value)
{
    s->items[s->top] = value;
    s->top++;
}

uint8 dequeue_stack(stack *s)
{
    stack *c = stack_init(100);
    while (!isEmptyStack(s))
        push(c, pop(s));
    uint8 x = pop(c);
    while (!isEmptyStack(c))
        push(s, pop(c));
    return x;
}
