#include <stdio.h>
#include "../queue/circular_queue.h"
#include "../stack/stack.h"

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
    queue *s = queue_init(100);
    enqueue(s, 1);
    enqueue(s, 2);
    enqueue(s, 3);
    enqueue(s, 4);
    enqueue(s, 5);
    enqueue(s, 6);
    enqueue(s, 7);
    reverse(s);
    while (!isEmptyQueue(s))
        printf("%ld ", dequeue(s));
    printf("\n");
    return 0;
}
