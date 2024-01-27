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

typedef struct {
    uint8 y;
    uint16 x;
    uint8 z;
    uint16 a;
} Point;

int main()
{
    printf("%ld\n", sizeof(Point));
    return 0;
}
