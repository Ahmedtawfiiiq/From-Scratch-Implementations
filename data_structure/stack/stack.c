#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "stack.h"

stack *stack_init(uint8 size)
{
    stack *s = (stack *)malloc(sizeof(stack));
    s->items = (uint8 *)malloc(size * sizeof(uint8));
    s->top = 0;
    s->size = size;
    return s;
}

void push(stack *s, uint8 value)
{
    s->items[s->top] = value;
    s->top += 1;
}

uint8 pop(stack *s)
{
    s->top -= 1;
    return s->items[s->top];
}

uint8 isEmpty(stack *s)
{
    if (s->top == 0)
        return 1;
    else
        return 0;
}

uint8 top(stack *s)
{
    return s->items[s->top - 1];
}

uint8 isFull(stack *s)
{
    if (s->top == s->size)
        return 1;
    else
        return 0;
}

// if top of stack is known
// void display(stack *s)
// {
//     for (int8 i = (s->top) - 1; i >= 0; i--)
//         printf("%d ", s->items[i]);
//     printf("\n");
// }

// if top of stack is not known
void display(stack *s, uint8 maxSize)
{
    stack *c = stack_init(maxSize);
    while (!isEmpty(s))
    {
        uint8 v = pop(s);
        printf("%d ", v);
        push(c, v);
    }
    while (!isEmpty(c))
    {
        push(s, pop(c));
    }
    printf("\n");
}

uint8 count(stack *s, uint8 maxSize)
{
    uint8 i = 0;
    stack *c = stack_init(maxSize);
    while (!isEmpty(s))
    {
        i += 1;
        push(c, pop(s));
    }
    while (!isEmpty(c))
        push(s, pop(c));
    return i;
}

uint8 sum(stack *s, uint8 maxSize)
{
    uint8 result = 0;
    stack *c = stack_init(maxSize);
    while (!isEmpty(s))
    {
        uint8 value = pop(s);
        result += value;
        push(c, value);
    }
    while (!isEmpty(c))
        push(s, pop(c));
    return result;
}

// from the top (positions starts from 1, 2, ..., size)
void deleteAt(stack *s, uint8 k, uint8 maxSize)
{
    stack *c = stack_init(maxSize);
    uint8 i = 1;
    while (i != k)
    {
        push(c, pop(s));
        i += 1;
    }
    pop(s);
    while (!isEmpty(c))
        push(s, pop(c));
}

// top of the stack contains the smallest element
void pushSorted(stack *s, uint8 value, uint8 maxSize)
{
    if (isEmpty(s) || value <= top(s))
        push(s, value);
    else
    {
        stack *c = stack_init(maxSize);
        while (!isEmpty(s) && value > top(s))
        {
            push(c, pop(s));
        }
        push(s, value);
        while (!isEmpty(c))
        {
            push(s, pop(c));
        }
    }
}

uint8 isSumEqual(stack *s, uint8 maxSize)
{
    uint8 n = count(s, maxSize);
    uint8 first = 0, second = 0, i = 0, t;
    stack *c = stack_init(maxSize);

    // check first half
    while (i != n / 2)
    {
        t = pop(s);
        first += t;
        push(c, t);
        i += 1;
    }

    // skip middle element in case of odd length
    if (n % 2 != 0)
        push(c, pop(s));

    // check second half
    while (!isEmpty(s))
    {
        t = pop(s);
        second += t;
        push(c, t);
    }

    while (!isEmpty(c))
    {
        push(c, pop(s));
    }

    if (first == second)
        return 1;
    else
        return 0;
}

uint8 isPalindrome(uint8 *str)
{
    uint8 n = strlen(str);
    uint8 i = 0;
    stack *s = stack_init(n + 1);

    while (i != n / 2)
    {
        push(s, str[i]);
        i += 1;
    }

    if (n % 2 != 0)
        i += 1;

    while (!isEmpty(s))
    {
        if (pop(s) != str[i])
            return 0;
        i += 1;
    }
    return 1;
}

uint8 *decimalToBinary(uint8 n)
{
    stack *s = stack_init(100);
    uint8 i = 0;
    while (n != 0)
    {
        i += 1;
        push(s, n % 2);
        n /= 2;
    }

    uint8 *result = (uint8 *)malloc((i) * sizeof(uint8));
    for (uint8 j = 0; j < i; j++)
    {
        result[j] = pop(s) + '0';
    }
    result[i] = '\0';
    return result;
}

uint8 priority(uint8 symbol)
{
    if (symbol == '+' || symbol == '-')
        return 1;
    else if (symbol == '*' || symbol == '/')
        return 2;
    else
        return 0;
}

uint8 *infixToPostfix(uint8 *infix)
{
    stack *s = stack_init(100);
    uint8 *postfix = (uint8 *)malloc(strlen(infix) * sizeof(uint8));
    uint8 i = 0;
    uint8 j = 0;
    while (infix[i] != '\0')
    {
        if (isalpha(infix[i]))
        {
            postfix[j] = infix[i];
            j += 1;
        }
        else if (infix[i] == '(')
        {
            push(s, infix[i]);
        }
        else if (*(infix + i) == ')')
        {
            while (!isEmpty(s) && top(s) != '(')
            {
                postfix[j] = pop(s);
                j += 1;
            }
            pop(s); // pop left parenthesis
        }
        else // operator
        {
            while (!isEmpty(s) && priority(top(s)) >= priority(infix[i]) && top(s) != '(')
            {
                postfix[j] = pop(s);
                j += 1;
            }
            push(s, infix[i]);
        }
        i += 1;
    }
    while (!isEmpty(s))
    {
        postfix[j] = pop(s);
        j += 1;
    }
    return postfix;
}

uint8 evaluatePostfix(uint8 *postfix)
{
    stack *s = stack_init(100);
    uint8 i = 0;
    while (postfix[i] != '\0')
    {
        if (isdigit(postfix[i]))
        {
            push(s, postfix[i] - '0');
        }
        else // operator
        {
            uint8 op1 = pop(s);
            uint8 op2 = pop(s);
            switch (postfix[i])
            {
            case '+':
                push(s, op2 + op1);
                break;
            case '-':
                push(s, op2 - op1);
                break;
            case '*':
                push(s, op2 * op1);
                break;
            case '/':
                push(s, op2 / op1);
                break;
            }
        }
        i += 1;
    }
    return pop(s);
}
