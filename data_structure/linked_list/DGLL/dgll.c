#include <stdio.h>
#include <stdlib.h>
#include "dgll.h"

void insert_start_dgll(SLL *l, uint8 value)
{
    node *n = create_node(value);
    if (isEmpty_LL(l))
    {
        l->head = n;
        l->tail = n;
    }
    else
    {
        n->next = l->head;
        l->head->prev = n;
        l->head = n;
    }
}
void insert_end_dgll(SLL *l, uint8 value)
{
    node *n = create_node(value);
    if (isEmpty_LL(l))
    {
        l->head = n;
        l->tail = n;
    }
    else
    {
        l->tail->next = n;
        n->prev = l->tail;
        l->tail = n;
    }
}
void delete_start_dgll(SLL *l)
{
    if (!isEmpty_LL(l))
    {
        node *temp = l->head;
        l->head = l->head->next;
        l->head->prev = NULL;
        free(temp);
        if (l->head == NULL)
            l->tail = NULL;
        else
            l->head->prev = NULL;
    }
}
void delete_end_dgll(SLL *l)
{
    if (!isEmpty_LL(l))
    {
        if (l->head->next == NULL)
        {
            free(l->head);
            l->head = NULL;
            l->tail = NULL;
        }
        else
        {
            node *temp = l->tail;
            l->tail = l->tail->prev;
            l->tail->next = NULL;
            free(temp);
        }
    }
}
