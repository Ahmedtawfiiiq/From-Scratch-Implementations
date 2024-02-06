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

typedef struct generalOrderedNode
{
    uint64 data;
    struct generalOrderedNode **children;
} generalOrderedNode;

queue *queue_init()
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
    return q->front == NULL;
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

node *create_node(uint64 value)
{
    node *n = (node *)malloc(sizeof(node));
    n->data = value;
    n->left = NULL;
    n->right = NULL;
    return n;
}

generalOrderedNode *create_general_ordered_node(uint64 data, uint8 childrenCount)
{
    generalOrderedNode *n = (generalOrderedNode *)malloc(sizeof(generalOrderedNode));
    n->data = data;
    n->children = (generalOrderedNode **)malloc(childrenCount * sizeof(generalOrderedNode *));
    for (uint8 i = 0; i < childrenCount; i++)
    {
        n->children[i] = (generalOrderedNode *)malloc(sizeof(generalOrderedNode));
        n->children[i] = NULL;
    }
    return n;
}

void pre_order_general(generalOrderedNode *root, uint8 childrenCount)
{
    if (root != NULL)
    {
        printf("%ld ", root->data);
        for (uint8 i = 0; i < childrenCount; i++)
            pre_order_general(root->children[i], childrenCount);
    }
}

node *general_to_binary(generalOrderedNode *root)
{
    if (root == NULL)
        return NULL;
    node *bt = create_node(root->data);
    node *temp = NULL;
    for (uint8 i = 0; i < 3; i++)
    {
        if (root->children[i] != NULL)
        {
            if (temp == NULL)
            {
                temp = general_to_binary(root->children[i]);
                bt->left = temp;
            }
            else
            {
                temp->right = general_to_binary(root->children[i]);
                temp = temp->right;
            }
        }
    }
    return bt;
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

uint8 count_queue(queue *q)
{
    uint8 count = 0;
    queueNode *n = q->front;
    while (n != NULL)
    {
        count++;
        n = n->next;
    }
    return count;
}

void bfs(node *root, uint8 isString)
{
    if (root == NULL)
    {
        printf("Tree is empty\n");
        return;
    }
    queue *q = queue_init();
    enqueue(q, root);
    uint8 level = 0;
    while (!isEmpty(q))
    {
        uint8 size = count_queue(q);
        printf("level %d: ", level);
        for (uint8 i = 0; i < size; i++)
        {
            node *t = dequeue(q);
            if (isString)
                printf("%c ", (int8)t->data);
            else
                printf("%ld ", t->data);
            if (t->left != NULL)
                enqueue(q, t->left);
            if (t->right != NULL)
                enqueue(q, t->right);
        }
        printf("\n");
        level++;
    }
}

int main()
{

    // general ordered trees
    generalOrderedNode *root = create_general_ordered_node(1, 3);

    root->children[0] = create_general_ordered_node(2, 3);
    root->children[1] = create_general_ordered_node(3, 3);
    root->children[2] = create_general_ordered_node(4, 3);

    root->children[2]->children[0] = create_general_ordered_node(5, 3);
    root->children[2]->children[1] = create_general_ordered_node(6, 3);
    root->children[2]->children[2] = create_general_ordered_node(7, 3);

    root->children[2]->children[1]->children[0] = create_general_ordered_node(8, 3);
    root->children[2]->children[1]->children[1] = create_general_ordered_node(9, 3);

    root->children[2]->children[2]->children[2] = create_general_ordered_node(10, 3);

    root->children[2]->children[2]->children[2]->children[0] = create_general_ordered_node(11, 3);
    root->children[2]->children[2]->children[2]->children[1] = create_general_ordered_node(12, 3);
    root->children[2]->children[2]->children[2]->children[2] = create_general_ordered_node(13, 3);

    // printf("pre order: ");
    // pre_order_general(root, 3);
    // printf("\n");
    node *bt = general_to_binary(root);
    bfs(bt, 0);
    return 0;
}
