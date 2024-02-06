#include <stdio.h>
#include <stdlib.h>
#include "ll.h"

SLL *SLL_init()
{
    SLL *l = (SLL *)malloc(sizeof(SLL));
    l->head = NULL;
    l->tail = NULL;
    return l;
}

node *create_node(uint8 value)
{
    node *n = (node *)malloc(sizeof(node));
    n->data = value;
    n->next = NULL;
    n->prev = NULL;
    return n;
}

uint8 isEmpty_LL(SLL *l)
{
    if (l->head == NULL)
        return 1;
    else
        return 0;
}
