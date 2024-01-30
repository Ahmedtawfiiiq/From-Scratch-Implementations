#include <stdio.h>
#include "trees.h"

node *create_node(uint64 value)
{
    node *n = (node *)malloc(sizeof(node));
    n->data = value;
    n->left = NULL;
    n->right = NULL;
    return n;
}

void pre_order(node *root)
{
    if (root != NULL)
    {
        printf("%ld ", root->data);
        pre_order(root->left);
        pre_order(root->right);
    }
}

void in_order(node *root)
{
    if (root != NULL)
    {
        in_order(root->left);
        printf("%ld ", root->data);
        in_order(root->right);
    }
}

void post_order(node *root)
{
    if (root != NULL)
    {
        post_order(root->left);
        post_order(root->right);
        printf("%ld ", root->data);
    }
}

queue *queue_init(uint8 size)
{
    queue *q = (queue *)malloc(sizeof(queue));
    q->front = NULL;
    q->rear = NULL;
    return q;
}

queueNode *create_queue_node(node *t)
{
    queueNode *n = (queueNode *)malloc(sizeof(queueNode));
    n->n = t;
    n->next = NULL;
    return n;
}

uint8 isEmpty(queue *q)
{
    if (q->front == NULL)
        return 1;
    else
        return 0;
}

void enqueue(queue *q, node *t)
{
    queueNode *n = create_queue_node(t);
    if (isEmpty(q))
    {
        q->front = n;
        q->rear = n;
    }
    else
    {
        q->rear->next = n;
        q->rear = n;
    }
}

node *dequeue(queue *q)
{
    node *t = (node *)malloc(sizeof(node));
    t = q->front->n;
    queueNode *n = q->front;
    q->front = q->front->next;
    if (isEmpty(q))
        q->rear = NULL;
    free(n);
    return t;
}

void bfs(node *root)
{
    if (root == NULL)
    {
        printf("Tree is empty\n");
        return;
    }
    queue *q = queue_init(100);
    enqueue(q, root);
    while (!isEmpty(q))
    {
        node *t = dequeue(q);
        printf("%ld ", t->data);
        if (t->left != NULL)
            enqueue(q, t->left);
        if (t->right != NULL)
            enqueue(q, t->right);
    }
    printf("\n");
}

node *copy(node *root)
{
    if (root == NULL)
        return NULL;
    else
    {
        node *n = create_node(root->data);
        n->left = copy(root->left);
        n->right = copy(root->right);
        return n;
    }
}

node *flip(node *root)
{
    if (root == NULL)
        return NULL;
    else
    {
        node *n = create_node(root->data);
        n->left = flip(root->right);
        n->right = flip(root->left);
        return n;
    }
}

uint8 isIdentical(node *a, node *b)
{
    if (!a && !b)
        return 1;
    else
        return (a && b) &&
               (a->data == b->data) &&
               isIdentical(a->left, b->left) &&
               isIdentical(a->right, b->right);
}

int8 max(int8 num1, int8 num2)
{
    return (num1 > num2) ? num1 : num2;
}

int8 height(node *root)
{
    if (!root)
        return -1;
    else
        return 1 + max(height(root->left), height(root->right));
}

uint8 count(node *root)
{
    if (!root)
        return 0;
    else
        return 1 + count(root->left) + count(root->right);
}

uint8 count_even(node *root)
{
    if (root == NULL)
        return 0;
    else
    {
        if (root->data % 2 == 0)
            return 1 + count_even(root->left) + count_even(root->right);
        else
            return count_even(root->left) + count_even(root->right);
    }
}

uint8 count_leaves(node *root)
{
    if (!root)
        return 0;
    else if (!root->left && !root->right)
        return 1;
    else
        return count_leaves(root->left) + count_leaves(root->right);
}

uint8 count_leaf_sum(node *root)
{
    if (!root)
        return 0;
    else if (!root->left && !root->right)
        return root->data;
    else
        return count_leaf_sum(root->left) + count_leaf_sum(root->right);
}

void swap(uint64 *a, uint64 *b)
{
    uint64 temp = *a;
    *a = *b;
    *b = temp;
}
