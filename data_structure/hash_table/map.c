#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "map.h"

node *create_node(uint8 key, uint8 value)
{
    node *n = (node *)malloc(sizeof(node));
    n->value = value;
    n->key = key;
    n->left = NULL;
    n->right = NULL;
    return n;
}

node *insert_node(node *root, uint8 key, uint8 value)
{
    if (root == NULL)
    {
        printf("-1 ");
        return create_node(key, value);
    }
    if (key < root->key)
        root->left = insert_node(root->left, key, value);
    else if (key > root->key)
        root->right = insert_node(root->right, key, value);
    else
    {
        printf("%c\n", root->value);
        root->value = value;
    }
    return root;
}

node *search_node(node *root, uint8 key)
{
    if (root == NULL || root->key == key)
        return root;
    if (key < root->key)
        return search_node(root->left, key);
    else
        return search_node(root->right, key);
}

void inorder_traversal(node *root)
{
    if (root != NULL)
    {
        inorder_traversal(root->left);
        printf("%d: %c ", root->key, root->value);
        inorder_traversal(root->right);
    }
    else
        printf("NULL ");
}
