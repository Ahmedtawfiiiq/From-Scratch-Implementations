#pragma once
#include "trees.h"

// find maximum value in a tree
node *findMax(node *root);
// find minimum value in a tree
node *findMin(node *root);

node *insert(node *root, uint64 data);
node *search_recursively(node *root, uint64 data);
node *search_iteratively(node *root, uint64 data);
node *delete_node(node *root, uint64 data);
uint8 count_bst(node *root, uint64 data);

// find predecessor for a given node
node *getPredecessor(node *n);
// find successor for a given node
node *getSuccessor(node *n);

void descending_transversal(node *root);

// binary search trees with strings
stringNode *insert_string(stringNode *root, uint8 *data);
stringNode *search_string(stringNode *root, uint8 *data);
void in_order_string(stringNode *root);
