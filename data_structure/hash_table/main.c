#include <stdio.h>
// #include "hash.h"
#include "map.h"

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef signed long int64;
typedef signed int int32;
typedef signed short int16;
typedef signed char int8;

int main()
{
    // uint8 size = 13;
    // node **ht = hash_list_init(size);
    // separate_chaining(ht, 18);
    // separate_chaining(ht, 41);
    // separate_chaining(ht, 22);
    // separate_chaining(ht, 44);
    // separate_chaining(ht, 59);
    // separate_chaining(ht, 32);
    // separate_chaining(ht, 31);
    // separate_chaining(ht, 73);
    // hash_list_display(ht, size);

    // uint64 keys[] = {18, 41, 22, 44, 59, 32, 31, 73};
    // uint64 keys[] = {89, 18, 49, 58, 9};
    // uint8 size = sizeof(keys) / sizeof(*keys);
    // uint8 n = 10;
    // uint64 *ht = hash_init(n);
    // for (uint8 i = 0; i < size; i++)
    // double_hashing(ht, keys[i]);
    // quadratic_probing(ht, keys[i]);
    // hash_display(ht, n);

    // map
    node *root = NULL;
    root = insert_node(root, 3, 'A');
    root = insert_node(root, 1, 'B');
    root = insert_node(root, 8, 'C');
    root = insert_node(root, 2, 'D');
    root = insert_node(root, 6, 'E');
    root = insert_node(root, 7, 'F');
    root = insert_node(root, 5, 'Z');
    printf("\n");
    root = insert_node(root, 3, 'G');

    // inorder_traversal(root);
    // printf("\n");
    return 0;
}
