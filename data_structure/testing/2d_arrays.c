#include <stdio.h>
#include <stdlib.h>

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

int main()
{
    uint8 arr[2][2] = {{1, 2}, {3, 4}};
    // uint8 *ptr = arr[0];
    // printf("%d\n", ptr[1]);
    // printf("%d\n", *(ptr + 1));
    // uint8(*ptr_arr)[2] = NULL;
    // ptr_arr = arr;
    // printf("%d\n", (*ptr_arr)[1]);
    // printf("%d\n", *(*ptr_arr + 1));
    // printf("%d\n", *(ptr_arr[0] + 1));
    // printf("%d\n", ptr_arr[0][1]);

    // printf("%d\n", ptr_arr[1][1]);
    // printf("%d\n", (*(ptr_arr + 1))[1]);
    // printf("%d\n", *(*(ptr_arr + 1) + 1));
    // printf("%d\n", *(ptr_arr[1] + 1));

    // uint8 (*ptr_arr)[2] = NULL;
    // ptr_arr = arr;
    // using pointer to pointer to point to 2D array
    uint8 **ptr = NULL;
    ptr = (uint8 **)malloc(2 * sizeof(uint8 *));
    for (uint8 i = 0; i < 2; i++)
    {
        ptr[i] = (uint8 *)malloc(2 * sizeof(uint8));
    }
    for (uint8 i = 0; i < 2; i++)
    {
        for (uint8 j = 0; j < 2; j++)
        {
            ptr[i][j] = arr[i][j];
        }
    }
    for (uint8 i = 0; i < 2; i++)
    {
        for (uint8 j = 0; j < 2; j++)
        {
            printf("%d ", ptr[i][j]);
        }
        printf("\n");
    }
    return 0;
}
