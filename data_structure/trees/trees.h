#pragma once
#include <stdio.h>
#include <stdlib.h>
#include "../stack/stack.h"

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
    struct node *parent;
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

typedef struct stackNode
{
    node *n;
    struct stackNode *next;
} stackNode;

typedef struct
{
    stackNode *top;
} stackP;

typedef struct generalOrderedNode
{
    uint64 data;
    struct generalOrderedNode **children;
} generalOrderedNode;

typedef struct stringNode
{
    uint8 *data;
    struct stringNode *left, *right;
} stringNode;

// stack
stackP *stack_init_node();
stackNode *create_stack_node(node *t);
uint8 isStackEmpty(stackP *s);
void pushNode(stackP *s, node *t);
node *popNode(stackP *s);
node *peek(stackP *s);

// queue
queue *queue_init();
queueNode *create_queue_node(node *t);
uint8 isEmpty(queue *q);
void enqueue(queue *q, node *t);
node *dequeue(queue *q);
uint8 count_queue(queue *q);

node *create_node(uint64 value);
void pre_order(node *root);
void in_order(node *root);
void post_order(node *root);
void bfs(node *root, uint8 isString); // uses a queue
int8 height(node *root);
int8 depth(node *root, node *n);
uint8 isBalancedTree(node *root);
int8 count_unbalanced(node *root);

node *copy(node *root);
node *flip(node *root);
uint8 isIdentical(node *a, node *b);
int8 max(int8 num1, int8 num2);
uint8 count(node *root);
uint8 count_even(node *root);
uint8 count_leaves(node *root);
uint8 count_leaf_sum(node *root);
void swap(uint64 *a, uint64 *b);
node *pre_in_construction(uint64 *preorder, uint8 preorderSize, uint64 *inorder, uint8 inorderSize);
node *in_post_construction(uint64 *inorder, uint8 inorderSize, uint64 *postorder, uint8 postorderSize);

node *expression_tree(uint8 *infix); // uses a stack

// general ordered tree
generalOrderedNode *create_general_ordered_node(uint64 data, uint8 childrenCount);
node *general_to_binary(generalOrderedNode *root);

uint8 longestPath(node *root, uint8 *result);

// binary tree with strings
stringNode *create_string_node(uint8 *value);
