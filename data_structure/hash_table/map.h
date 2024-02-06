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
    uint8 key;
    uint8 value;
    struct node *left, *right;
} node;

// map using binary search trees
node *create_node(uint8 key, uint8 value);
node *insert_node(node *root, uint8 key, uint8 value);
node *search_node(node *root, uint8 key);
void inorder_traversal(node *root);
