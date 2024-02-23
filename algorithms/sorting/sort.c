#include <stdio.h>
#include <stdlib.h>
#include "sort.h"

void print_array(int32 *arr, int32 n)
{
    for (int32 i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void swap(int32 *a, int32 *b)
{
    int32 temp = *a;
    *a = *b;
    *b = temp;
}

// in-place sorting
void bubble_sort(int32 *arr, int32 n)
{
    for (int32 i = 0; i < n - 1; i++)
    {
        for (int32 j = n - 1; j > i; j--)
        {
            if (arr[j] < arr[j - 1])
                swap(&arr[j], &arr[j - 1]);
        }
    }
}

// in-place sorting
void selection_sort(int32 *arr, int32 n)
{
    for (int32 i = 0; i < n - 1; i++)
    {
        int32 min_index = i;
        for (int32 j = n - 1; j > i; j--)
        {
            if (arr[j] < arr[min_index])
                min_index = j;
        }
        swap(&arr[i], &arr[min_index]);
    }
}

// in-place sorting
void insertion_sort(int32 *arr, int32 n)
{
    for (int32 i = 1; i < n; i++)
    {
        for (int32 j = i; j > 0 && arr[j] < arr[j - 1]; j--)
            swap(&arr[j], &arr[j - 1]);
    }
}

int32 *merge_sort(int32 *arr, int32 n)
{
    if (n < 2)
        return arr;

    // divide
    int32 mid = n / 2;
    int32 ln = mid, rn = n - mid;
    int32 left[ln], right[rn];

    for (int32 i = 0; i < mid; i++)
        left[i] = arr[i];
    for (int32 i = mid, j = 0; i < n; i++, j++)
        right[j] = arr[i];

    // conquer
    int32 *sorted_left = merge_sort(left, ln);
    int32 *sorted_right = merge_sort(right, rn);

    // combine
    for (int32 i = 0, l = 0, r = 0; i < n; i++)
    {
        if (l < ln && r < rn)
        {
            if (sorted_left[l] < sorted_right[r])
                arr[i] = sorted_left[l++];
            else
                arr[i] = sorted_right[r++];
        }
        else if (l < ln)
            arr[i] = sorted_left[l++];
        else
            arr[i] = sorted_right[r++];
    }

    return arr;
}

int32 *quick_sort(int32 *arr, int32 n)
{
    if (n < 2)
        return arr;

    // divide
    int32 pivot = arr[n - 1];
    int32 left[n], right[n];
    int32 l = 0, r = 0;

    for (int32 i = 0; i < n - 1; i++)
    {
        if (arr[i] < pivot)
            left[l++] = arr[i];
        else
            right[r++] = arr[i];
    }

    // conquer
    int32 *sorted_left = quick_sort(left, l);
    int32 *sorted_right = quick_sort(right, r);

    // combine
    for (int32 i = 0; i < l; i++)
        arr[i] = sorted_left[i];
    arr[l] = pivot;
    for (int32 i = l + 1, j = 0; i < n; i++, j++)
        arr[i] = sorted_right[j];

    return arr;
}
