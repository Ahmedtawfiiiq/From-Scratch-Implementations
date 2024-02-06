#include <stdio.h>
#include <stdlib.h>
#include "scll.h"

void insert_start_scll(SLL *l, uint8 value)
{
    node *n = create_node(value);
    if (isEmpty_LL(l))
    {
        n->next = n;
        l->head = n;
        l->tail = n;
    }
    else
    {
        n->next = l->head;
        l->head = n;
        l->tail->next = n;
    }
}

void insert_end_scll(SLL *l, uint8 value)
{
    node *n = create_node(value);
    if (isEmpty_LL(l))
    {
        n->next = n;
        l->head = n;
        l->tail = n;
    }
    else
    {
        l->tail->next = n;
        n->next = l->head;
        l->tail = n;
    }
}

void delete_start_scll(SLL *l)
{
    if (!isEmpty_LL(l))
    {
        node *n = l->head;
        // has more than one node
        if (l->head != l->tail)
        {
            l->head = l->head->next;
            l->tail->next = l->head;
        }
        // has only one node
        else
        {
            l->head = NULL;
            l->tail = NULL;
        }
        free(n);
    }
}

void delete_end_scll(SLL *l)
{
    if (!isEmpty_LL(l))
    {
        // has more than one node
        if (l->head != l->tail)
        {
            node *n = l->head;
            while (n->next != l->tail)
                n = n->next;
            free(l->tail);
            l->tail = n;
            l->tail->next = l->head;
        }
        // has only one node
        else
        {
            free(l->head);
            l->head = NULL;
            l->tail = NULL;
        }
    }
}

void traverse_c(node *head)
{
    node *n = head;
    while (n->next != head)
    {
        printf("%d ", n->data);
        n = n->next;
    }
    printf("%d\n", n->data);
}

uint8 count_c(node *head)
{
    if (head == NULL)
        return 0;
    else if (head == head->next)
        return 1;
    else
    {
        uint8 count = 1;
        node *n = head;
        while (n->next != head)
        {
            count++;
            n = n->next;
        }
        return count;
    }
}

node *search_recursively(node *head, uint8 value)
{
    if (head == NULL)
        return NULL;
    else if (head->data == value)
        return head;
    else if (head->next == head)
        return NULL;
    else
        return search_recursively(head->next, value);
}
