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

typedef struct
{
    node *head, *tail;
} linkedList;

node *create_node(uint8 value);
linkedList *ll_init();
uint8 isEmpty(linkedList *ll);
void insert_start(linkedList *ll, uint8 value);
void insert_end(linkedList *ll, uint8 value);
void delete_start(linkedList *ll);
void trav_recursively(linkedList *ll);
void trav_iteratively(linkedList *ll);
node *get_tail(node *n);
node *search(linkedList *ll, uint8 value);
node *search_iteratively(linkedList *ll, uint8 value);
void insert_node(node *n, uint8 value);
node *deleteAfter(node *n);
