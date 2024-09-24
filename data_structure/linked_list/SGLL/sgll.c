#include <stdio.h>
#include <stdlib.h>
#include "sgll.h"

// complexity: O(1)
void insert_start_sgll(SLL *l, uint8 value)
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
        l->head = n;
    }
}

// complexity: O(1)
void insert_end_sgll(SLL *l, uint8 value)
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
        l->tail = n;
    }
}

// complexity: O(1)
void delete_start_sgll(SLL *l)
{
    if (!isEmpty_LL(l))
    {
        node *n = l->head;
        l->head = l->head->next;
        free(n);
        if (isEmpty_LL(l))
            l->tail = NULL;
    }
}

// complexity: O(n)
void delete_end_sgll(SLL *l)
{
    // there are more than one node
    if (!isEmpty_LL(l) && l->head != l->tail)
    {
        node *n = l->head;
        while (n->next != l->tail)
            n = n->next;
        free(l->tail);
        l->tail = n;
        l->tail->next = NULL;
    }

    // there is only one node
    else if (!isEmpty_LL(l) && l->head == l->tail)
    {
        free(l->head);
        l->head = NULL;
        l->tail = NULL;
    }
}

void traverse_g(node *head)
{
    if (head != NULL)
    {
        printf("%d ", head->data);
        traverse_g(head->next);
    }
    else
        printf("\n");
}

uint8 count_g(node *head)
{
    uint8 c = 0;
    node *n = head;
    while (n != NULL)
    {
        n = n->next;
        c += 1;
    }
    return c;
}

node *search_recursively(node *head, uint8 value)
{
    if (head == NULL)
        return NULL;
    else
    {
        if (head->data == value)
            return head;
        else
            return search_recursively(head->next, value);
    }
}

node *search_iteratively(node *head, uint8 value)
{
    node *n = head;
    while (n != NULL)
    {
        if (n->data == value)
            return n;
        else
            n = n->next;
    }
    return n;
}

void delete_node_sgll(SLL *l, uint8 value)
{
    node *prev = NULL;
    node *current = l->head;
    while (current != NULL)
    {
        if (current->data == value)
        {
            if (prev == NULL) // remove first node
            {
                l->head = current->next;
                if (l->head == NULL) // if it was only one node
                    l->tail = NULL;
            }
            else if (current->next == NULL) // remove last node
            {
                l->tail = prev;
                l->tail->next = NULL;
            }
            else
                prev->next = current->next;
            free(current);
            break;
        }
        prev = current;
        current = current->next;
    }
}

node *delete_node_sgll_recursively(SLL *l, node *head, uint8 value)
{
    if (head == NULL)
        return NULL;
    if (head->data == value)
    {
        node *n = head->next;
        free(head);
        head = n;
        return head;
    }
    head->next = delete_node_sgll_recursively(l, head->next, value);
    if (head->next == NULL)
        l->tail = head;
    return head;
}

// k is 0-based
void delete_kth_node_sgll(SLL *l, uint8 k)
{
    uint8 count = 0;
    node *prev = NULL;
    node *current = l->head;
    while (current != NULL)
    {
        if (count == k)
        {
            if (prev == NULL) // remove first node
            {
                l->head = current->next;
                if (l->head == NULL) // if it was only one node
                    l->tail = NULL;
            }
            else if (current->next == NULL) // remove last node
            {
                l->tail = prev;
                l->tail->next = NULL;
            }
            else
                prev->next = current->next;
            free(current);
            break;
        }
        prev = current;
        current = current->next;
        count += 1;
    }
}

// reverse in place
void reverse_sgll(SLL *l)
{
    node *prev = NULL;
    node *current = l->head;
    node *next = NULL;
    while (current != NULL)
    {
        // store next
        next = current->next;
        // reverse current node's pointer
        current->next = prev;
        // move pointers one position ahead
        prev = current;
        current = next;
    }
    l->tail = l->head;
    l->head = prev;
}

// insert a new node with data (value)
// after the given node *n
void insert_node(node *n, uint8 value)
{
    node *nn = create_node(value);
    nn->next = n->next;
    n->next = nn;
}

SLL *sort(SLL *l1, SLL *l2)
{
    SLL *l = SLL_init();
    node *h1 = l1->head;
    node *h2 = l2->head;
    while (h1 && h2)
    {
        if (h1->data < h2->data)
        {
            insert_end_sgll(l, h1->data);
            h1 = h1->next;
        }
        else if (h1->data > h2->data)
        {
            insert_end_sgll(l, h2->data);
            h2 = h2->next;
        }
        else
        {
            insert_end_sgll(l, h1->data);
            insert_end_sgll(l, h2->data);
            h1 = h1->next;
            h2 = h2->next;
        }
    }
    while (h1)
    {
        insert_end_sgll(l, h1->data);
        h1 = h1->next;
    }
    while (h2)
    {
        insert_end_sgll(l, h2->data);
        h2 = h2->next;
    }
    return l;
}

node *get_tail(node *head)
{
    if (head == NULL)
        return NULL;
    else
    {
        if (head->next != NULL)
            return get_tail(head->next);
        else
            return head;
    }
}

node *deleteAfter(node *n)
{
    if (n != NULL)
    {
        node *d = n->next;
        n->next = n->next->next;
        free(d);
        return n;
    }
}

uint8 sum_recursively(node *head)
{
    if (head == NULL)
        return 0;
    else
        return head->data + sum_recursively(head->next);
}

uint8 sum_iteratively(node *head)
{
    uint8 sum = 0;
    node *n = head;
    while (n != NULL)
    {
        sum += n->data;
        n = n->next;
    }
    return sum;
}
