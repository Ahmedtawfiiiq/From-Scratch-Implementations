#include <stdio.h>
#include <stdlib.h>
#include "circular_queue.h"

queue *queue_init(uint8 size)
{
    queue *q = (queue *)malloc(sizeof(queue));
    q->items = (uint8 *)malloc(size * sizeof(uint8));
    q->front = 0;
    q->rear = 0;
    q->capcity = size;
    q->n = 0;
    return q;
}

void enqueue(queue *q, uint8 value)
{
    if (isFull(q))
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

uint8 dequeue(queue *q)
{
    if (isEmpty(q))
    {
        printf("Queue is empty\n");
        return -1;
    }
    else
    {
        uint8 value = q->items[q->front];
        q->front += 1;
        q->front %= q->capcity; // circular queue
        q->n -= 1;
        return value;
    }
}

uint8 isEmpty(queue *q)
{
    if (q->n == 0)
        return 1;
    else
        return 0;
}

uint8 isFull(queue *q)
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

uint8 getFirst(queue *q)
{
    return q->items[q->front];
}

uint8 getLast(queue *q)
{
    if (q->rear == 0)
        return q->items[q->capcity - 1];
    else
        return q->items[q->rear - 1];
}

void display(queue *q)
{
    queue *c = queue_init(q->n);
    while (!isEmpty(q))
    {
        uint8 value = dequeue(q);
        printf("%d ", value);
        enqueue(c, value);
    }
    printf("\n");
    while (!isEmpty(c))
        enqueue(q, dequeue(c));
}

uint8 getMinimum(queue *q)
{
    queue *c = queue_init(q->n);
    uint8 min = dequeue(q);
    enqueue(c, min);
    while (!isEmpty(q))
    {
        uint8 value = dequeue(q);
        if (value < min)
            min = value;
        enqueue(c, value);
    }
    while (!isEmpty(c))
        enqueue(q, dequeue(c));
    return min;
}
