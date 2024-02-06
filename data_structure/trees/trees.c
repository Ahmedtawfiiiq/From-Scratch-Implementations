#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "trees.h"

////////////////////// stack //////////////////////
// stack
stackP *stack_init_node()
{
    stackP *s = (stackP *)malloc(sizeof(stackP));
    s->top = NULL;
    return s;
}

stackNode *create_stack_node(node *t)
{
    stackNode *n = (stackNode *)malloc(sizeof(stackNode));
    n->n = t;
    n->next = NULL;
    return n;
}

uint8 isStackEmpty(stackP *s)
{
    return s->top == NULL;
}

void pushNode(stackP *s, node *t)
{
    stackNode *n = create_stack_node(t);
    if (isStackEmpty(s))
        s->top = n;
    else
    {
        n->next = s->top;
        s->top = n;
    }
}

node *popNode(stackP *s)
{
    if (isStackEmpty(s))
        return NULL;
    else
    {
        node *t = s->top->n;
        stackNode *n = s->top;
        s->top = s->top->next;
        free(n);
        return t;
    }
}

node *peek(stackP *s)
{
    if (isStackEmpty(s))
        return NULL;
    else
        return s->top->n;
}

////////////////////// queue //////////////////////
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

////////////////////// tree //////////////////////
node *create_node(uint64 value)
{
    node *n = (node *)malloc(sizeof(node));
    n->data = value;
    n->left = NULL;
    n->right = NULL;
    n->parent = NULL;
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

// height of a node
// the number of edges in the longest path from the node to the deepest leaf
int8 height(node *root)
{
    if (!root)
        return -1;
    else
        return 1 + max(height(root->left), height(root->right));
}

// depth of a node
// the number of edges in the path from the root to the node
int8 depth(node *root, node *n)
{
    // if the tree is empty
    if (root == NULL)
        return -1;

    // if the node is the root
    else if (root == n)
        return 0;
    else
    {
        int8 l = depth(root->left, n);
        int8 r = depth(root->right, n);

        // if the node is not in the tree
        if (l == -1 && r == -1)
            return -1;
        else // if the node is in the tree
            return 1 + max(l, r);
    }
}

// a tree is balanced if the height of the left and right subtrees of every node differ by at most 1
uint8 isBalancedTree(node *root)
{
    if (!root)
        return 1; // an empty tree is balanced
    else
    {
        int8 l = height(root->left);
        int8 r = height(root->right);
        return (abs(l - r) <= 1) &&
               isBalancedTree(root->left) &&
               isBalancedTree(root->right);
    }
}

int8 count_unbalanced(node *root)
{
    if (!root)
        return 0; // an empty tree is balanced
    else
    {
        int8 l = height(root->left);
        int8 r = height(root->right);
        return (abs(l - r) > 1) +
               count_unbalanced(root->left) +
               count_unbalanced(root->right);
    }
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

node *pre_in_construction(uint64 *preorder, uint8 preorderSize, uint64 *inorder, uint8 inorderSize)
{
    // post-order: root-left-right
    // in-order: left-root-right
    node *root = create_node(preorder[0]);
    uint8 ln = 0;
    while (inorder[ln] != preorder[0])
        ln++;
    uint8 rn = ln + 1;
    while (rn < inorderSize)
        rn++;
    rn -= ln + 1;
    if (ln != 0)
        root->left = pre_in_construction(preorder + 1, ln, inorder, ln);
    if (rn != 0)
        root->right = pre_in_construction(preorder + ln + 1, rn, inorder + ln + 1, rn);
    return root;
}

node *in_post_construction(uint64 *inorder, uint8 inorderSize, uint64 *postorder, uint8 postorderSize)
{
    node *root = create_node(postorder[postorderSize - 1]);
    int ln = 0;
    while (inorder[ln] != postorder[postorderSize - 1] && ln < inorderSize)
        ln++;
    int rn = ln + 1;
    while (rn < inorderSize)
        rn++;
    rn -= ln + 1;
    if (rn)
        root->right = in_post_construction(inorder + ln + 1, rn, postorder, postorderSize - 1);
    if (ln)
        root->left = in_post_construction(inorder, ln, postorder, postorderSize - rn - 1);
    return root;
}

node *expression_tree(uint8 *infix)
{
    uint8 *postfix = infixToPostfix(infix);
    stackP *s = stack_init_node();
    for (uint8 i = 0; postfix[i] != '\0'; i++)
    {
        if (isalpha(postfix[i]) || isdigit(postfix[i]))
            pushNode(s, create_node(postfix[i]));
        else
        {
            node *t = create_node(postfix[i]);
            t->right = popNode(s);
            t->left = popNode(s);
            pushNode(s, t);
        }
    }
    return peek(s);
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

uint8 longestPath(node *root, uint8 *result)
{
    if (root == NULL)
        return 0;
    uint8 left = longestPath(root->left, result);
    uint8 right = longestPath(root->right, result);
    *result = max(*result, 1 + left + right);
    return 1 + max(left, right);
}

// binary trees with strings
stringNode *create_string_node(uint8 *value)
{
    stringNode *n = (stringNode *)malloc(sizeof(stringNode));
    n->data = (uint8 *)malloc(strlen(value) + 1);
    strcpy(n->data, value);
    n->left = NULL;
    n->right = NULL;
    return n;
}
