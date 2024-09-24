#include "../stack/stack.h"

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef signed long int64;
typedef signed int int32;
typedef signed short int16;
typedef signed char int8;

typedef struct
{
    // capacity is the maximum number of elements that can be stored in the queue
    // n is the number of elements in the queue
    uint8 front, rear;
    uint8 capcity;
    uint64 *items;
    uint8 n; // to solve the problem of isFull() and isEmpty() have the same condition
} queue;

// standard functions
queue *queue_init(uint8 size);
void enqueue(queue *q, uint64 value);
uint64 dequeue(queue *q);
uint8 isEmptyQueue(queue *q);
uint8 isFullQueue(queue *q);
void dispose(queue *q);
uint64 getFirst(queue *q);
uint64 getLast(queue *q);

void displayQueue(queue *q);
uint64 getMinimum(queue *q);
void reverse(queue *q);

void enqueue_stack(stack *s, uint8 value);
uint8 dequeue_stack(stack *s);
