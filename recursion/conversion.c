#include <stdio.h>
#include <string.h>

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef signed long int64;
typedef signed int int32;
typedef signed short int16;
typedef signed char int8;

// binary to decimal (left to right)
// unknown number of bits
// horner's algorithm
int foo(uint8 *s, uint8 sum)
{
    if (*s == '\0')
        return sum;
    sum *= 2;
    sum += *s - '0';
    return foo(s + 1, sum);
}

// binary to decimal (right to left)
// known number of bits
int bar(uint8 *s)
{
    int sum = 0;
    int e = 1;
    int n = strlen(s);
    for (int i = n - 1; i >= 0; i--, e *= 2)
        sum += (s[i] - '0') * e;
    return sum;
}

int main()
{
    uint8 *s = "10011";
    printf("%d\n", foo(s, 0));
    printf("%d\n", bar(s));
    return 0;
}
