#include <stdio.h>
#include <stdlib.h>

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

int main()
{
    uint8 arr[4] = {1, 2, 3, 4};
    // contains the address of the first element of the array
    // uint8 *ptr = NULL;
    // ptr = arr;
    // ptr = &arr[0];
    // printf("%d\n", ptr[1]);
    // printf("%d\n", *(ptr + 1));
    // pointer to an array
    // uint8 (*ptr_arr)[4] = NULL;
    // ptr_arr = &arr;
    // printf("%d\n", (*ptr_arr)[1]);
    // printf("%d\n", (*(*ptr_arr + 1)));
    // array of pointers
    // uint8 *ptr[4];
    // for (uint8 i = 0; i < 4; i++)
    // {
    //     ptr[i] = &arr[i];
    // }
    // printf("%d\n", *ptr[1]);
    // printf("%d\n", *(ptr[0] + 1));
    // printf("%d\n", *(*ptr + 1));
    return 0;
}
