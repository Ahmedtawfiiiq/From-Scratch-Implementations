#include <stdio.h>

void merge(int *arr, int l, int mid, int r)
{
    int t[r - l + 1];
    int i = l, j = mid + 1;
    int k = 0;

    while ((i <= mid) && (j <= r))
    {
        if (arr[i] < arr[j])
            t[k++] = arr[i++];
        else
            t[k++] = arr[j++];
    }
    while (i <= mid)
        t[k++] = arr[i++];
    while (j <= r)
        t[k++] = arr[j++];
    for (int i = l, index = 0; i <= r; i++)
        arr[i] = t[index++];
}

void merge_sort(int *arr, int l, int r)
{
    if (l < r)
    {
        int mid = (l + r) / 2;
        merge_sort(arr, l, mid);
        merge_sort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }
}
