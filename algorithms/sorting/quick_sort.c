#include <stdio.h>
#include "quick_sort.h"

void swap(int *arr, int i, int j)
{
    int t = arr[i];
    arr[i] = arr[j];
    arr[j] = t;
}

int min_partition(int *arr, int l, int r)
{
    int pivot = arr[r];
    int p = l - 1;
    int i = l;
    while (i <= r)
    {
        if (arr[i] <= pivot)
        {
            p++;
            if (arr[p] >= pivot)
                swap(arr, p, i);
        }
        i++;
    }
    return p;
}

int max_partition(int *arr, int l, int r)
{
    int pivot = arr[r];
    int p = l - 1;
    int i = l;
    while (i <= r)
    {
        if (arr[i] >= pivot)
        {
            p++;
            if (arr[p] <= pivot)
                swap(arr, p, i);
        }
        i++;
    }
    return p;
}

// in-place
void quick_sort(int *arr, int l, int r)
{
    if (l <= r)
    {
        // divide
        int p = min_partition(arr, l, r);
        // int p = max_partition(arr, l, r);
        // conquer
        quick_sort(arr, l, p - 1);
        quick_sort(arr, p + 1, r);
    }
}

// k is 0-indexed
// kth smallest element
int quick_select(int *arr, int l, int r, int k)
{
    if (l <= r)
    {
        int p = min_partition(arr, l, r);
        if (k == p)
            return arr[p];
        else if (k < p)
            return quick_select(arr, l, p - 1, k);
        else
            return quick_select(arr, p + 1, r, k);
    }
}

float get_median(int *arr, int l, int r)
{
    int n = r - l + 1;
    int k = n / 2;
    if (n % 2 != 0)
        return quick_select(arr, l, r, k);
    else
        return (quick_select(arr, l, r, k - 1) + quick_select(arr, l, r, k)) / 2.0;
}
