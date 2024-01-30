#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef signed long int64;
typedef signed int int32;
typedef signed short int16;
typedef signed char int8;

int func(int y)
{
    static int x = 0;
    x++;
    return x;
}
int main()
{
    printf("%d", func());
    printf("%d", func());
    return 0;
}
