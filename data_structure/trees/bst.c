#include "bst.h"

node *insert(node *root, uint64 data)
{
    if (!root)
    {
        node *n = create_node(data);
    }
    else
    {
        if (data < root->data)
            root->left = insert(root->left, data);
        else if (data > root->data)
            root->right = insert(root->right, data);
        return root;
    }
}

node *search_recursively(node *root, uint64 data)
{
    if (root == NULL)
        return NULL;
    else
    {
        if (data < root->data)
            return search_recursively(root->left, data);
        else if (data > root->data)
            return search_recursively(root->right, data);
        else
            return root;
    }
}

node *search_iteratively(node *root, uint64 data)
{
    if (root == NULL)
        return NULL;
    else
    {
        node *n = root;
        while (n != NULL)
        {
            if (data < n->data)
                n = n->left;
            else if (data > n->data)
                n = n->right;
            else
                return n;
        }
        return NULL;
    }
}

node *findMin(node *root)
{
    if (!root->left)
        return root;
    else
        return findMin(root->left);
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
                node *m = findMin(root->right);
                root = delete_node(root, m->data);
                root->data = m->data;
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
node *getPredecessor(node *root, uint64 data)
{
    node *s = search_recursively(root, data);
    if (!s)
    {
        printf("Node not found\n");
        return s;
    }
    else
    {
        node *n = s->left;
        while (n->right != NULL)
        {
            n = n->right;
        }
        return n;
    }
}

// one step right and then left till you can
node *getSuccessor(node *root, uint64 data)
{
    node *s = search_recursively(root, data);
    if (!s)
    {
        printf("Node not found\n");
        return s;
    }
    else
    {
        node *n = s->right;
        while (n->left != NULL)
        {
            n = n->left;
        }
        return n;
    }
}
