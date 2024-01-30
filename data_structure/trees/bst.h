#include "trees.h"

node *insert(node *root, uint64 data);
node *search_recursively(node *root, uint64 data);
node *search_iteratively(node *root, uint64 data);
node *delete_node(node *root, uint64 data);
uint8 count_bst(node *root, uint64 data);

// find predecessor for a node of a given key
node *getPredecessor(node *root, uint64 data);

// find successor for a node of a given key
node *getSuccessor(node *root, uint64 data);
