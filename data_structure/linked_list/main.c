#include <stdio.h>
#include "SGLL/sgll.h"
// #include "SCLL/scll.h"

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
    // SGLL *l1 = SGLL_init();
    // insert_start(l1, 6);
    // insert_start(l1, 4);
    // insert_start(l1, 2);
    // insert_start(l1, 0);
    // SGLL *l2 = SGLL_init();
    // insert_start(l2, 5);
    // insert_start(l2, 3);
    // insert_start(l2, 1);
    // insert_start(l2, 0);
    // SGLL *l = sort(l1, l2);
    // trav_iteratively(l->head);
    // trav_recursively(l->head);

    SLL *list = SLL_init();
    insert_start_sgll(list, 5);
    insert_start_sgll(list, 7);
    insert_start_sgll(list, 8);
    insert_end_sgll(list, 4);
    insert_end_sgll(list, 3);
    insert_end_sgll(list, 1);
    traverse_g(list->head);
    // reverse_sgll(list);
    list->head = delete_node_sgll_recursively(list, list->head, 1);
    traverse_g(list->head);
    printf("tail: %d\n", list->tail->data);
    // printf("count: %d\n", count_g(list->head));
    // delete_start_sgll(list);
    // delete_end_sgll(list);
    // delete_kth_node_sgll(list, 3);
    // traverse_g(list->head);
    // printf("count: %d\n", count_g(list->head));

    // SLL *list = SLL_init();
    // insert_start_scll(list, 5);
    // insert_start_scll(list, 7);
    // insert_start_scll(list, 8);
    // insert_end_scll(list, 4);
    // insert_end_scll(list, 3);
    // insert_end_scll(list, 1);
    // traverse_c(list->head);
    // printf("count: %d\n", count_c(list->head));
    // delete_start_scll(list);
    // delete_end_scll(list);
    // traverse_c(list->head);
    // printf("count: %d\n", count_c(list->head));
    return 0;
}
