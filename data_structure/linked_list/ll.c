#include "ll.h"

node *create_node(uint8 value)
{
    node *n = (node *)malloc(sizeof(node));
    n->data = value;
    n->next = NULL;
    return n;
}

linkedList *ll_init()
{
    linkedList *ll = (linkedList *)malloc(sizeof(linkedList));
    ll->head = NULL;
    ll->tail = NULL;
    return ll;
}

uint8 isEmpty(linkedList *ll)
{
    if (ll->head == NULL)
        return 1;
    else
        return 0;
}

void insert_start(linkedList *ll, uint8 value)
{
    node *n = create_node(value);
    if (isEmpty(ll))
    {
        ll->head = n;
        ll->tail = n;
    }
    else
    {
        n->next = ll->head;
        ll->head = n;
    }
}

void insert_end(linkedList *ll, uint8 value)
{
    node *n = create_node(value);
    if (isEmpty(ll))
    {
        ll->head = n;
        ll->tail = n;
    }
    else
    {
        ll->tail->next = n;
        ll->tail = n;
    }
}

void delete_start(linkedList *ll)
{
    if (!isEmpty(ll))
    {
        node *n = ll->head;
        ll->head = ll->head->next;
        free(n);
        if (isEmpty(ll))
        {
            ll->tail = NULL;
        }
    }
}

void trav_recursively(linkedList *ll)
{
    if (ll->head != NULL)
    {
        printf("%d ", ll->head->data);
        trav_recursively(ll->head->next);
    }
}

void trav_iteratively(linkedList *ll)
{
    while (ll->head != NULL)
    {
        printf("%d ", ll->head->data);
        ll->head = ll->head->next;
    }
}

node *get_tail(node *n)
{
    if (n == NULL)
        return NULL;
    else
    {
        if (n->next != NULL)
            return get_tail(n->next);
        else
            return n;
    }
}

node *search_recursively(linkedList *ll, uint8 value)
{
    if (ll->head == NULL)
        return NULL;
    else
    {
        if (ll->head->data == value)
            return ll->head;
        else
            return search(ll->head->next, value);
    }
}

node *search_iteratively(linkedList *ll, uint8 value)
{
    while (ll->head != NULL)
    {
        if (ll->head->data == value)
            return ll->head;
        else
            ll->head = ll->head->next;
    }
    return ll->head;
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
