#include <stdio.h>
#include <stdlib.h>
// #include "structure.h"

typedef unsigned long uint64;
typedef unsigned int uint32;
typedef unsigned short uint16;
typedef unsigned char uint8;

enum boolean
{
    false = 0,
    true = 1
};

typedef struct
{
    uint8 day;
    uint8 month;
    uint16 year;
} birthDate;

typedef struct
{
    birthDate birthDate;
    uint8 salary;
} employee;

employee *readEmployee(uint8 n)
{
    employee *e = (employee *)malloc(n * sizeof(employee));
    for (uint8 i = 0; i < n; i++)
    {
        printf("\nemployee: %d\n", i + 1);
        printf("salary: ");
        scanf("%hhd", &e->salary);
        printf("date of birth: ");
        scanf("%hhd%hhd%hd", &e[i].birthDate.day, &e[i].birthDate.month, &e[i].birthDate.year);
    }
    return e;
}

void displayEmployees(employee *e, uint8 n)
{
    for (uint8 i = 0; i < n; i++)
    {
        printf("\nemployee: %d\n", i + 1);
        printf("salary: %d\n", e[i].salary);
        printf("date of birth: %d-%d-%d\n", e[i].birthDate.day, e[i].birthDate.month, e[i].birthDate.year);
    }
}

void displayMaxSalary(employee *e, uint8 n)
{
    uint8 maxSalary = 0;
    uint8 employeeIndex;
    for (uint8 i = 0; i < n; i++)
    {
        if (e[i].salary > maxSalary)
        {
            maxSalary = e[i].salary;
            employeeIndex = i;
        }
    }
    printf("\nEmployee of max salary:\n");
    printf("Salary: %d\n", e[employeeIndex].salary);
    printf("Date of Birth: %d-%d-%d\n", e[employeeIndex].birthDate.day, e[employeeIndex].birthDate.month, e[employeeIndex].birthDate.year);
}

void displayYoungestEmployee(employee *e, uint8 n)
{
    int i, min_i = 0;
    for (i = 0; i < n; i++)
    {
        if (e[i].birthDate.year > e[min_i].birthDate.year)
            min_i = i;
        else if (e[i].birthDate.year == e[min_i].birthDate.year)
        {

            if (e[i].birthDate.month > e[min_i].birthDate.month)
                min_i = i;
            else if (e[i].birthDate.month == e[min_i].birthDate.month)
            {

                if (e[i].birthDate.day > e[min_i].birthDate.day)
                    min_i = i;
            }
        }
    }

    printf("\nEmployee of youngest age:\n");
    printf("Salary: %d\n", e[min_i].salary);
    printf("Date of Birth: %d-%d-%d\n", e[min_i].birthDate.day, e[min_i].birthDate.month, e[min_i].birthDate.year);
}

int main()
{
    // uint8 n;
    // printf("Enter number of employees: ");
    // scanf("%hhd", &n);
    employee *e = readEmployee(3);
    // employee e[3] = {
    // {{1, 1, 2001}, 100},
    // {{12, 2, 2001}, 30},
    // {{3, 3, 2000}, 65},
    // };
    // displayEmployees(e, 3);
    displayMaxSalary(e, 3);
    displayYoungestEmployee(e, 3);
    return 0;
}
