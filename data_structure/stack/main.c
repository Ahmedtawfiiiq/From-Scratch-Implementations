#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack.h"

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef signed long int64;
typedef signed int int32;
typedef signed short int16;
typedef signed char int8;

int main()
{
    stack *s;
    s = stack_init(100);
    // push(s, 2);
    // push(s, 7);
    // push(s, 4);
    // push(s, 3);
    // push(s, 9);
    // display(s, 100);
    // printf("%d\n", count(s, 100));
    // printf("%d\n", sum(s, 100));
    // deleteAt(s, 2, 100);
    // display(s, 100);
    // pushSorted(s, 2, 100);
    // pushSorted(s, 7, 100);
    // pushSorted(s, 4, 100);
    // pushSorted(s, 3, 100);
    // pushSorted(s, 9, 100);
    // display(s, 100);
    // pushSorted(s, 6, 100);
    // pushSorted(s, 12, 100);
    // display(s, 100);

    // push elements to stack such that
    // first half sum is equal to second half sum
    // push(s, 1);
    // push(s, 2);
    // push(s, 3);
    // push(s, 4);
    // push(s, 5);
    // push(s, 6);
    // push(s, 5);
    // push(s, 4);
    // push(s, 3);
    // push(s, 2);
    // push(s, 1);
    // display(s, 100);
    // if (isSumEqual(s, 100))
    //     printf("Sum is equal\n");
    // else
    //     printf("Sum is not equal\n");
    // if (isPalindrome("baam"))
    //     printf("Palindrome\n");
    // else
    //     printf("Not palindrome\n");
    // uint8 *binary = decimalToBinary(10);
    // printf("%s\n", binary);
    uint8 *infix = "(a+b*(c-d))/e"; // abcd-*+e/
    // uint8 *infix = "a+b*c/d-e"; // abc*d/+e-
    uint8 *postfix = infixToPostfix(infix);
    printf("%s\n", postfix);
    // uint8 *postfix = "45+42-*73*+";
    // printf("%d\n", evaluatePostfix(postfix));
    return 0;
}
