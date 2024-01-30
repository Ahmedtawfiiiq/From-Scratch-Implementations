typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef signed long int64;
typedef signed int int32;
typedef signed short int16;
typedef signed char int8;

typedef struct
{
    uint8 *items;
    uint8 top;
    uint8 size;
} stack;

// standard functions
stack *stack_init(uint8 size);
void push(stack *s, uint8 value);
uint8 pop(stack *s);
uint8 isEmptyStack(stack *s);
uint8 isFullStack(stack *s);
uint8 top(stack *s);

void displayStack(stack *s, uint8 maxSize);
uint8 count(stack *s, uint8 maxSize);
uint8 sum(stack *s, uint8 maxSize);
void deleteAt(stack *s, uint8 k, uint8 maxSize);
void pushSorted(stack *s, uint8 value, uint8 maxSize);
// check if the sum of the first half of the stack is equal to the sum of the second half
uint8 isSumEqual(stack *s, uint8 maxSize);
uint8 isPalindrome(uint8 *str);
uint8 *decimalToBinary(uint8 n);
stack* sort(stack *s1, stack* s2);

// check priority of the given operator
uint8 priority(uint8 symbol);
uint8 *infixToPostfix(uint8 *infix);
// evaluate postfix expression
uint8 evaluatePostfix(uint8 *postfix);
