typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef signed long int64;
typedef signed int int32;
typedef signed short int16;
typedef signed char int8;

typedef struct node
{
    uint8 data;
    struct node *next, *prev;
} node;

typedef struct
{
    node *head, *tail;
} SLL;

SLL *SLL_init();
node *create_node(uint8 value);
uint8 isEmpty_LL(SLL *l);
