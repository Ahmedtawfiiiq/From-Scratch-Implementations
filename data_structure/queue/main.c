#include <stdio.h>
#include "circular_queue.h"

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef signed long int64;
typedef signed int int32;
typedef signed short int16;
typedef signed char int8;

int main()
{
    // queue *q = queue_init(5);
    // enqueue(q, 2);
    // enqueue(q, 1);
    // enqueue(q, 4);
    // enqueue(q, 3);
    // enqueue(q, 9);
    // dequeue(q);
    // dequeue(q);
    // enqueue(q, 5);
    // printf("%d\n", getMinimum(q));
    // display(q);
    // printf("front index: %d\n", q->front);
    // printf("rear index: %d\n", q->rear);
    // queue *s = queue_init(100);
    // enqueue(s, 1);
    // enqueue(s, 2);
    // enqueue(s, 3);
    // enqueue(s, 4);
    // enqueue(s, 5);
    // enqueue(s, 6);
    // enqueue(s, 7);
    // reverse(s);
    // while (!isEmptyQueue(s))
    //     printf("%ld ", dequeue(s));
    // printf("\n");

    stack *s = stack_init(10);
    enqueue_stack(s, 1);
    enqueue_stack(s, 2);
    enqueue_stack(s, 3);
    enqueue_stack(s, 4);
    enqueue_stack(s, 5);
    printf("%d\n", dequeue_stack(s));
    printf("%d\n", dequeue_stack(s));
    return 0;
}
