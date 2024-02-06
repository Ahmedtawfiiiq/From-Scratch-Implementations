#include "../ll.h"

void insert_start_sgll(SLL *l, uint8 value);
void insert_end_sgll(SLL *l, uint8 value);
void delete_start_sgll(SLL *l);
void delete_end_sgll(SLL *l);
void traverse_g(node *head);

uint8 count_g(node *head);
node *search_recursively(node *head, uint8 value);
node *search_iteratively(node *head, uint8 value);

void delete_node_sgll(SLL *l, uint8 value);
node *delete_node_sgll_recursively(SLL *l, node *head, uint8 value);
void delete_kth_node_sgll(SLL *l, uint8 k);
void reverse_sgll(SLL *l);

void insert_node(node *n, uint8 value);

SLL *sort(SLL *l1, SLL *l2);
node *get_tail(node *head);
node *deleteAfter(node *n);
uint8 sum_recursively(node *head);
uint8 sum_iteratively(node *head);
