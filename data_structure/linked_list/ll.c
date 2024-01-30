#include "ll.h"

node *create_node(uint8 value)
{
    node *n = (node *)malloc(sizeof(node));
    n->data = value;
    n->next = NULL;
    return n;
}

node *insert_start(node *head, uint8 value)
{
    node *n = create_node(value);
    n->next = head;
    head = n;
    return head;
}

node *delete_start(node *head)
{
    if (head != NULL)
    {
        node *n = head;
        head = head->next;
        free(n);
        return head;
    }
}

void delete_end(node *head)
{
    if (head != NULL)
    {
        node *tail = head;
        node *prev = NULL;
        while (tail->next != NULL)
        {
            prev = tail;
            tail = tail->next;
        }
        free(tail);
        if (prev != NULL)
            prev->next = NULL;
        else
            head = NULL;
    }
}

void trav_recursively(node *head)
{
    if (head != NULL)
    {
        printf("%d ", head->data);
        trav_recursively(head->next);
    }
    else
        printf("\n");
}

void trav_iteratively(node *head)
{
    node *n = head;
    while (n != NULL)
    {
        printf("%d ", n->data);
        n = n->next;
    }
    printf("\n");
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

// insert a new node with data (value)
// after the given node *n
void insert_node(node *n, uint8 value)
{
    node *nn = create_node(value);
    nn->next = n->next;
    n->next = nn;
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

uint8 count(node *head)
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

node *sort(node *h1, node *h2)
{
    node *h;
    if (h1->data < h2->data)
    {
        h = create_node(h1->data);
        h1 = h1->next;
    }
    else if (h1->data > h2->data)
    {
        h = create_node(h2->data);
        h2 = h2->next;
    }
    else
    {
        h = create_node(h1->data);
        h = insert_start(h, h2->data);
        h1 = h1->next;
        h2 = h2->next;
    }
    while (h1 != NULL && h2 != NULL)
    {
        if (h1->data < h2->data)
        {
            h = insert_start(h, h1->data);
            h1 = h1->next;
        }
        else if (h1->data > h2->data)
        {
            h = insert_start(h, h2->data);
            h2 = h2->next;
        }
        else
        {
            h = insert_start(h, h1->data);
            h = insert_start(h, h2->data);
            h1 = h1->next;
            h2 = h2->next;
        }
    }
    while (h1 != NULL)
    {
        h = insert_start(h, h1->data);
        h1 = h1->next;
    }
    while (h2 != NULL)
    {
        h = insert_start(h, h2->data);
        h2 = h2->next;
    }
    return h;
}
