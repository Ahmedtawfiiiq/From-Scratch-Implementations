#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    uint8 data;
} node;

node *create(uint8 data)
{
    node *new_node = (node *)malloc(sizeof(node));
    new_node->data = data;
    return new_node;
}

void swap1(node *a, node *b)
{
    node *temp = a;
    a = b;
    b = temp;
}

void swap2(node **a, node **b)
{
    node *temp = *a;
    *a = *b;
    *b = temp;
}

void update1(node a)
{
    a.data += 5;
}

void update2(node *a)
{
    a->data += 5;
}

int main()
{
    // node *a = create(1);
    // node *b = create(2);
    // swap1(a, b);
    // printf("%d\n", a->data);
    // printf("%d\n", b->data);
    // swap2(&a, &b);
    // printf("%d\n", a->data);
    // printf("%d\n", b->data);

    // node a = {1};
    // update1(a);
    // printf("%d\n", a.data);
    // update2(&a);
    // printf("%d\n", a.data);

    // node *a = create(1);
    // update1(*a);
    // printf("%d\n", a->data);
    // update2(a);
    // printf("%d\n", a->data);
    return 0;
}
