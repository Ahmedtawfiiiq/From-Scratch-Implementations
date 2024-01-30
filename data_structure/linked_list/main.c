#include <stdio.h>
#include "ll.h"

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
    node *h1 = create_node(6);
    h1 = insert_start(h1, 4);
    h1 = insert_start(h1, 2);
    h1 = insert_start(h1, 0);
    node *h2 = create_node(5);
    h2 = insert_start(h2, 3);
    h2 = insert_start(h2, 1);
    h2 = insert_start(h2, 0);
    node *h = sort(h1, h2);
    trav_iteratively(h);
    return 0;
}
