#pragma once
#include "trees.h"

int8 left_index(int8 index);
int8 right_index(int8 index);
int8 parent_index(int8 index);
void bottom_up(uint64 *heap, uint8 size);
void max_heapify_bottom(uint64 *heap, uint8 size, int8 index);
void min_heapify_bottom(uint64 *heap, uint8 size, int8 index);
void max_heapify_up(uint64 *heap, int8 index);
void min_heapify_up(uint64 *heap, int8 index);
void top_down(uint64 *heap, uint8 size);
uint64 *heap_insert(uint64 *heap, uint8 size, uint64 value);
void delete_root(uint64 *heap, uint8 size);
void heap_sort(uint64 *heap, uint8 size);
node *construct_heap(uint64 *heap, uint8 size);
uint8 mostFrequent(uint64 *heap, uint8 size);
