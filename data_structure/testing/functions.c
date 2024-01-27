#include <stdio.h>
#include <stdlib.h>
#include "structure.h"

employee *readEmployee(uint8 n)
{
    employee *e = (employee *)malloc(n * sizeof(employee));
    for (uint8 i = 0; i < n; i++)
    {
        printf("\nemployee: %d\n", i + 1);
        printf("salary: ");
        scanf("%hhd", &e->salary);
        printf("date of birth: ");
        scanf("%hhd%hhd%hd", &e->birthDate.day, &e->birthDate.month, &e->birthDate.year);
    }
    return e;
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
    uint8 min_i = 0;
    for (uint8 i = 0; i < n; i++)
    {
        if (e[i].birthDate.year < e[min_i].birthDate.year)
        {
            min_i = i;
        }
        else if (e[i].birthDate.year == e[min_i].birthDate.year)
        {
            if (e[i].birthDate.month < e[min_i].birthDate.month)
            {
                min_i = i;
            }
            else if (e[i].birthDate.month == e[min_i].birthDate.month)
            {
                if (e[i].birthDate.day < e[min_i].birthDate.day)
                {
                    min_i = i;
                }
            }
        }
    }

    printf("\nEmployee of youngest age:\n");
    printf("Salary: %d\n", e[min_i].salary);
    printf("Date of Birth: %d-%d-%d\n", e[min_i].birthDate.day, e[min_i].birthDate.month, e[min_i].birthDate.year);
}
