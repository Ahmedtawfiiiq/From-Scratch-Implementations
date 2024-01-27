#include <stdio.h>
#include <stdlib.h>

typedef unsigned char uint8;
typedef unsigned short uint16;
typedef unsigned int uint32;
typedef unsigned long uint64;

int main()
{
    // dynamic allocation
    // type 1: 1D array
    // uint8 *ptr1 = NULL;
    // // allocate 10 bytes of memory
    // ptr1 = (uint8 *)malloc(10 * sizeof(uint8));
    // for (uint8 i = 0; i < 10; i++)
    // {
    //     ptr1[i] = i;
    // }
    // for (uint8 i = 0; i < 10; i++)
    // {
    //     printf("%d ", ptr1[i]);
    // }
    // printf("\n");
    // type 2: 2D array
    uint8 **ptr2 = NULL;
    // allocate 5*2 bytes of memory
    ptr2 = (uint8 **)malloc(5 * sizeof(uint8 *));
    for (uint8 i = 0; i < 5; i++)
    {
        ptr2[i] = (uint8 *)malloc(2 * sizeof(uint8));
    }
    uint8 cnt = 0;
    for (uint8 i = 0; i < 5; i++)
    {
        for (uint8 j = 0; j < 2; j++)
        {
            ptr2[i][j] = cnt++;
        }
    }
    for (uint8 i = 0; i < 5; i++)
    {
        for (uint8 j = 0; j < 2; j++)
        {
            printf("%d ", ptr2[i][j]);
        }
        printf("\n");
    }
    return 0;
}
