#pragma once
#include <stdio.h>

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
    uint64 key;
    struct node *next;
} node;

// separate chaining
node *hash_node(uint64 key);
node **hash_list_init(uint8 size);
void separate_chaining(node **hash, uint64 key);
void hash_list_display(node **hash, uint8 size);

// open addressing
uint64 *hash_init(uint8 size);
void linear_probing(uint64 *hash, uint64 key);
void quadratic_probing(uint64 *hash, uint64 key);
void double_hashing(uint64 *hash, uint64 key);
void hash_display(uint64 *hash, uint8 size);

uint64 find_first_repeating(uint64 *arr, uint8 size);
