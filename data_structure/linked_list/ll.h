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

node *create_node(uint8 value);
node *insert_start(node *head, uint8 value);
node *delete_start(node *head);
void delete_end(node *head);
void trav_recursively(node *head);
void trav_iteratively(node *head);
node *get_tail(node *head);
node *search_recursively(node *head, uint8 value);
node *search_iteratively(node *head, uint8 value);
void insert_node(node *n, uint8 value);
node *deleteAfter(node *n);
uint8 sum_recursively(node *head);
uint8 sum_iteratively(node *head);
uint8 count(node *head);
node *sort(node *h1, node *h2);
