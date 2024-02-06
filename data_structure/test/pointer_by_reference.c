#include <stdio.h>
#include <stdlib.h>

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
    uint8 data;
    struct node *next;
} node;

node *create_node(uint8 data)
{
    node *new_node = (node *)malloc(sizeof(node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

// pass a pointer by value
void foo1(node *head)
{
    head = head->next;
}

// pass a pointer by reference
void foo2(node **head)
{
    *head = (*head)->next;
}

int main()
{
    node *head = create_node(1);
    head->next = create_node(2);
    foo1(head);
    printf("%d\n", head->data);
    foo2(&head);
    printf("%d\n", head->data);
    return 0;
}
