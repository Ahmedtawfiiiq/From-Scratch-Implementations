#include <stdio.h>
#include <stdlib.h>
#include "hash.h"

node *hash_node(uint64 key)
{
    node *n = (node *)malloc(sizeof(node));
    n->key = key;
    n->next = NULL;
    return n;
}

node **hash_list_init(uint8 size)
{
    node **hash = (node **)malloc(size * sizeof(node *));
    for (uint8 i = 0; i < size; i++)
        hash[i] = NULL;
    return hash;
}

void separate_chaining(node **hash, uint64 key)
{
    uint8 index = key % 13;
    node *n = hash_node(key);
    if (hash[index] == NULL)
    {
        hash[index] = (node *)malloc(sizeof(node));
        hash[index] = n;
    }
    else
    {
        node *temp = hash[index];
        while (temp->next != NULL)
            temp = temp->next;
        temp->next = n;
    }
}

void hash_list_display(node **hash, uint8 size)
{
    for (uint8 i = 0; i < size; i++)
    {
        printf("index %d: ", i);
        node *n = hash[i];
        while (n != NULL)
        {
            printf("%ld ", n->key);
            n = n->next;
        }
        printf("\n");
    }
}

uint64 *hash_init(uint8 size)
{
    uint64 *hash = (uint64 *)malloc(size * sizeof(uint64));
    for (uint8 i = 0; i < size; i++)
        hash[i] = 0;
    return hash;
}

void linear_probing(uint64 *hash, uint64 key)
{
    if (hash[key % 13] == 0)
        hash[key % 13] = key;
    else
    {
        uint8 i = 1;
        while (hash[(key + i) % 13] != 0)
            i++;
        hash[(key + i) % 13] = key;
    }
}

void quadratic_probing(uint64 *hash, uint64 key)
{
    uint8 n = 10;
    uint8 h = key % n;
    uint8 i = 1;
    while (hash[h] != 0)
        h = (key + i * i++) % n;
    hash[h] = key;
}

void double_hashing(uint64 *hash, uint64 key)
{
    // h1(k) = k mod n
    // h2(k) = m - (k mod m)
    // h(k, i) = (h1(k) + i * h2(k)) mod 13 for i = 0, 1, ..., n - 1
    uint8 n = 13;
    uint8 h1 = key % n;
    uint8 h2 = 7 - (key % 7);
    uint8 i = 0;
    uint8 h = (h1 + i * h2) % n;
    while (hash[h] != 0)
        h = (h1 + ++i * h2) % n;
    hash[h] = key;
}

void hash_display(uint64 *hash, uint8 size)
{
    for (uint8 i = 0; i < size; i++)
        printf("%ld ", hash[i]);
    printf("\n");
}
