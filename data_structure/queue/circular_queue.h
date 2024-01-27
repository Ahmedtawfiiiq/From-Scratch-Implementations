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
    uint8 front, rear;
    uint8 capcity;
    uint8 *items;
    uint8 n; // to solve the problem of isFull() and isEmpty() have the same condition
} queue;

queue *queue_init(uint8 size);
void enqueue(queue *q, uint8 value);
uint8 dequeue(queue *q);
uint8 isEmpty(queue *q);
uint8 isFull(queue *q);
void dispose(queue *q);
uint8 getFirst(queue *q);
uint8 getLast(queue *q);
void display(queue *q);
uint8 getMinimum(queue *q);
