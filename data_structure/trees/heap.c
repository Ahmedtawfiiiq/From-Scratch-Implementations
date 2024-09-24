#include "trees.h"

int8 left_index(int8 index)
{
    return (2 * index) + 1;
}

int8 right_index(int8 index)
{
    return (2 * index) + 2;
}

int8 parent_index(int8 index)
{
    return (index - 1) / 2;
}

// complexity: O(log n)
void max_heapify_bottom(uint64 *heap, uint8 size, int8 index)
{
    int8 l = left_index(index);
    int8 r = right_index(index);
    int8 largest = index;
    if (l < size && heap[l] > heap[index])
        largest = l;
    if (r < size && heap[r] > heap[largest])
        largest = r;
    if (largest != index)
    {
        swap(&heap[index], &heap[largest]);
        max_heapify_bottom(heap, size, largest);
    }
}

// complexity: O(log n)
void min_heapify_bottom(uint64 *heap, uint8 size, int8 index)
{
    int8 l = left_index(index);
    int8 r = right_index(index);
    int8 smallest = index;
    if (l < size && heap[l] < heap[index])
        smallest = l;
    if (r < size && heap[r] < heap[smallest])
        smallest = r;
    if (smallest != index)
    {
        swap(&heap[index], &heap[smallest]);
        min_heapify_bottom(heap, size, smallest);
    }
}

// complexity: O(n)
void bottom_up(uint64 *heap, uint8 size, uint8 isMax)
{
    int8 i = parent_index(size - 1); // parent of last leaf node
    for (; i >= 0; i--)
    {
        if (isMax)
            max_heapify_bottom(heap, size, i);
        else
            min_heapify_bottom(heap, size, i);
    }
}

// complexity: O(log n)
void max_heapify_up(uint64 *heap, int8 index)
{
    if (index != 0)
    {
        int8 p = parent_index(index);
        if (heap[p] < heap[index]) // max heap
        {
            swap(&heap[p], &heap[index]);
            max_heapify_up(heap, p);
        }
    }
}

// complexity: O(log n)
void min_heapify_up(uint64 *heap, int8 index)
{
    if (index != 0)
    {
        int8 p = parent_index(index);
        if (heap[p] > heap[index]) // min heap
        {
            swap(&heap[p], &heap[index]);
            min_heapify_up(heap, p);
        }
    }
}

// complexity: O(n log n)
void top_down(uint64 *heap, uint8 size, uint8 isMax)
{
    for (uint8 i = 0; i < size; i++)
    {
        if (isMax)
            max_heapify_up(heap, i);
        else
            min_heapify_up(heap, i);
    }
}

// complexity: O(log n)
// same as max_heapify_up
// ignoring the complexity of copying the array
// assume that the size of the heap large enough to hold the new value
uint64 *heap_insert(uint64 *heap, uint8 size, uint64 value, uint8 isMax)
{
    uint64 *new_heap = (uint64 *)malloc((size + 1) * sizeof(uint64));
    for (uint8 i = 0; i < size; i++)
        new_heap[i] = heap[i];
    new_heap[size] = value;

    uint8 new_index = size;
    if (isMax)
        max_heapify_up(new_heap, new_index);
    else
        min_heapify_up(new_heap, new_index);
    return new_heap;
}

// complexity: O(log n)
void delete_root(uint64 *heap, uint8 size, uint8 isMax)
{
    swap(&heap[0], &heap[size - 1]);
    if (isMax)
        max_heapify_bottom(heap, size - 1, 0);
    else
        min_heapify_bottom(heap, size - 1, 0);
}

// complexity: O(n log n)
void heap_sort(uint64 *heap, uint8 size, uint8 isMax)
{
    bottom_up(heap, size, isMax);
    // top_down(heap, size);
    while (size > 1)
        delete_root(heap, size--, isMax);
}

node *construct_heap(uint64 *heap, uint8 size)
{
    node *root = create_node(heap[0]);
    queue *q = queue_init(size);
    enqueue(q, root);
    uint8 i = 1;
    while (i < size)
    {
        node *t = dequeue(q);
        t->left = create_node(heap[i++]);
        enqueue(q, t->left);
        if (i < size)
        {
            t->right = create_node(heap[i++]);
            enqueue(q, t->right);
        }
    }
    return root;
}

uint8 mostFrequent(uint64 *heap, uint8 size)
{
    bottom_up(heap, size, 1);
    uint8 count = 1;
    uint8 max = 1;
    while (size > 1)
    {
        swap(&heap[0], &heap[size - 1]);
        if (heap[0] == heap[size - 1])
        {
            count++;
            if (count > max)
                max = count;
        }
        else
            count = 1;
        max_heapify_bottom(heap, size - 1, 0);
        size--;
    }
    return max;
}

float getMedian(uint64 *heap, uint8 size, uint64 value)
{
    heap_sort(heap, size, 1); // ascending order
    uint8 maxHeapSize = size / 2;
    uint8 minHeapSize = size - maxHeapSize;
    uint64 *max = (uint64 *)malloc(maxHeapSize * sizeof(uint64));
    uint64 *min = (uint64 *)malloc(minHeapSize * sizeof(uint64));
    for (uint8 i = 0; i < maxHeapSize; i++)
        max[i] = heap[i];
    for (uint8 i = 0; i < minHeapSize; i++)
        min[i] = heap[i + maxHeapSize];
    for (uint8 i = 0; i < maxHeapSize; i++)
        max_heapify_up(max, i);
    for (uint8 i = 0; i < minHeapSize; i++)
        min_heapify_up(min, i);
    if (minHeapSize == maxHeapSize)
    {
        max = heap_insert(max, maxHeapSize, value, 1);
        min = heap_insert(min, minHeapSize, max[0], 0);
        delete_root(max, maxHeapSize, 1);
        minHeapSize++;
    }
    else
    {
        min = heap_insert(min, minHeapSize, value, 0);
        max = heap_insert(max, maxHeapSize, min[0], 1);
        delete_root(min, minHeapSize, 0);
        maxHeapSize++;
    }
    if (minHeapSize == maxHeapSize)
        return (max[0] + min[0]) / 2.0;
    return min[0];
}
