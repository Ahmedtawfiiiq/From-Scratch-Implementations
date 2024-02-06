#include <stdio.h>
#include <stdlib.h>

enum bool
{
    false = 0,
    true = 1
};

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

uint8 *foo(uint8 size)
{
    uint8 *result = (uint8 *)malloc(size * sizeof(uint8));
    for (uint8 i = 0; i < size; i++)
        result[i] = 0;
    return result;
}

void add(uint8 data[], uint8 size, uint8 value)
{
    for (uint8 i = 0; i < size; i++)
    {
        data[i] += value;
    }
}

int main()
{
    uint8 *data = foo(5);
    uint8 size = sizeof(data) / sizeof(*data);
    add(*data, size, 5);
    for (uint8 i = 0; i < size; i++)
    {
        printf("%d ", data[i]);
    }
    printf("\n");
    return 0;
}
