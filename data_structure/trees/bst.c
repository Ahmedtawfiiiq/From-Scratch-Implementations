#include <string.h>
#include "bst.h"

node *findMax(node *root)
{
    if (root->right != NULL)
        return findMax(root->right);
    else
        return root;
}

node *findMin(node *root)
{
    if (root->left != NULL)
        return findMin(root->left);
    else
        return root;
}

node *insert(node *root, uint64 data)
{
    if (!root)
        root = create_node(data);
    else
    {
        if (data < root->data)
        {
            root->left = insert(root->left, data);
            root->left->parent = root;
        }
        else if (data > root->data)
        {
            root->right = insert(root->right, data);
            root->right->parent = root;
        }
    }
    return root;
}

node *search_recursively(node *root, uint64 data)
{
    if (root == NULL || root->data == data)
        return root;
    if (data < root->data)
        return search_recursively(root->left, data);
    else
        return search_recursively(root->right, data);
}

node *search_iteratively(node *root, uint64 data)
{
    node *n = root;
    while (n != NULL && n->data != data)
    {
        if (data < n->data)
            n = n->left;
        else
            n = n->right;
    }
    return n;
}

node *delete_node(node *root, uint64 data)
{
    if (!root)
        return root;
    else
    {
        // delete root
        if (root->data == data)
        {
            // leaf node
            if (!root->left && !root->right)
                return NULL;
            // has a left child
            else if (root->left && !root->right)
                return root->left;
            // has a right child
            else if (!root->left && root->right)
                return root->right;
            // has both left and right children
            else
            {
                // 1. find the minimum node in the right subtree
                // 2. replace the root with the minimum node
                // 3. delete the minimum node
                node *min = findMin(root->right);
                root->data = min->data;
                root->right = delete_node(root->right, min->data);
                return root;
            }
        }
        // search for a node with key equals to data
        else
        {
            if (data < root->data) // search left
                root->left = delete_node(root->left, data);
            else // search right
                root->right = delete_node(root->right, data);
            return root;
        }
    }
}

// counts the number of nodes in a bst containing
// values that are greater than or equal to data
uint8 count_bst(node *root, uint64 data)
{
    if (root == NULL)
        return 0;
    else
    {
        if (root->data < data)
            return count_bst(root->right, data);
        else
            return 1 + count_bst(root->left, data) + count_bst(root->right, data);
    }
}

// one step left and then right till you can
node *getPredecessor(node *n)
{
    if (n->left != NULL)
        return findMax(n->left);
    node *p = n->parent;
    while (p != NULL && n == p->left)
    {
        n = p;
        p = p->parent;
    }
    return p;
}

// one step right and then left till you can
node *getSuccessor(node *n)
{
    if (n->right != NULL)
        return findMin(n->right);
    node *p = n->parent;
    while (p != NULL && n == p->right)
    {
        n = p;
        p = p->parent;
    }
    return p;
}

// right, root, left
void descending_transversal(node *root)
{
    if (root)
    {
        descending_transversal(root->right);
        printf("%ld ", root->data);
        descending_transversal(root->left);
    }
}

// binary search trees with strings
// strcmp:
// 0 if the strings are equal
// < 0 if the first string is less than the second
// > 0 if the first string is greater than the second
stringNode *insert_string(stringNode *root, uint8 *data)
{
    if (!root)
        return create_string_node(data);
    if (strcmp(data, root->data) < 0)
        root->left = insert_string(root->left, data);
    else
        root->right = insert_string(root->right, data);
    return root;
}

stringNode *search_string(stringNode *root, uint8 *data)
{
    if (root == NULL || strcmp(root->data, data) == 0)
        return root;
    if (strcmp(data, root->data) < 0)
        return search_string(root->left, data);
    return search_string(root->right, data);
}

void in_order_string(stringNode *root)
{
    if (root)
    {
        in_order_string(root->left);
        printf("%s ", root->data);
        in_order_string(root->right);
    }
    else
        printf("NULL ");
}
