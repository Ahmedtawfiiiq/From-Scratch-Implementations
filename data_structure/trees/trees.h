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
    struct node *left, *right;
    uint64 data;
} node;

typedef struct queueNode
{
    node *n;
    struct queueNode *next;
} queueNode;

typedef struct
{
    queueNode *front, *rear;
} queue;

node *create_node(uint64 value);
void pre_order(node *root);
void in_order(node *root);
void post_order(node *root);
queue *queue_init(uint8 size);
queueNode *create_queue_node(node *t);
uint8 isEmpty(queue *q);
void enqueue(queue *q, node *t);
node *dequeue(queue *q);
void bfs(node *root);
node *copy(node *root);
node *flip(node *root);
uint8 isIdentical(node *a, node *b);
int8 max(int8 num1, int8 num2);
int8 height(node *root);
uint8 count(node *root);
uint8 count_even(node *root);
uint8 count_leaves(node *root);
uint8 count_leaf_sum(node *root);
void swap(uint64 *a, uint64 *b);
