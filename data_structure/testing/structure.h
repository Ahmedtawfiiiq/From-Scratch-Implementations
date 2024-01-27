#include <stdio.h>

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

typedef struct
{
    uint8 day;
    uint8 month;
    uint16 year;
} DOB;

typedef struct
{
    DOB birthDate;
    uint8 salary;
} employee;

employee *readEmployee(uint8 n);
void displayMaxSalary(employee *e, uint8 n);
void displayYoungestEmployee(employee *e, uint8 n);
