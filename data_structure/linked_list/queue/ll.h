#include "../stack/ll.h"

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef signed long int64;
typedef signed int int32;
typedef signed short int16;
typedef signed char int8;

typedef struct node
{
    uint64 data;
    struct node *next;
} node;

typedef struct
{
    node *front, *rear;
} queue;

node *create_node(uint64 value);
queue *queue_init(uint8 size);
uint8 isEmpty_queue(queue *q);
void enqueue(queue *q, uint64 value);
uint64 dequeue(queue *q);
