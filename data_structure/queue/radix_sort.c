#include <stdio.h>
#include <stdlib.h>
#include "circular_queue.h"

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef signed long int64;
typedef signed int int32;
typedef signed short int16;
typedef signed char int8;

void radix_sort(uint64 *arr, uint8 size, uint8 radix);

int main()
{
    uint64 data[] = {20903, 980, 99999, 111, 42, 1111, 21, 997, 1, 1111};
    uint8 radix = 10;
    uint8 size = sizeof(data) / sizeof(*data);
    radix_sort(data, size, radix);
    for (int8 i = 0; i < size; i++)
        printf("%ld ", data[i]);
    printf("\n");
    return 0;
}

void radix_sort(uint64 *arr, uint8 size, uint8 radix)
{
    queue **q = (queue **)malloc(radix * sizeof(queue *));
    for (int8 i = 0; i < radix; i++)
        q[i] = queue_init(size);

    // get max value
    uint64 mx = *arr;
    for (int8 i = 1; i < size; i++)
        if (arr[i] > mx)
            mx = arr[i];

    // get number of digits of max value
    int8 count = 0;
    while (mx)
    {
        count++;
        mx /= radix;
    }

    uint32 exp = 1;
    while (count)
    {
        for (int8 i = 0; i < size; i++)
            enqueue(q[(arr[i] / exp) % radix], arr[i]);
        int8 i = 0;
        for (int8 j = 0; j < radix; j++)
            while (!isEmptyQueue(q[j]))
                arr[i++] = dequeue(q[j]);
        exp *= radix;
        count -= 1;
    }
    for (uint8 i = 0; i < radix; i++)
    {
        dispose(q[i]);
    }
}
