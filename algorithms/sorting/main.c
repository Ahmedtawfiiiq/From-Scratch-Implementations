#include <stdio.h>
// #include "sort.h"
// #include "merge_sort.h"
#include "quick_sort.h"

int main()
{
    int data[] = {8, 1, 6, 4, 0, 3, 9, 5};
    int n = sizeof(data) / sizeof(*data);

    // selection_sort(data, n);
    // bubble_sort(data, n);
    // insertion_sort(data, n);
    // merge_sort(data, n);
    // quick_sort(data, n);
    // print_array(data, n);

    // merge_sort(data, 0, n - 1);
    // int value = quick_select(data, 0, n - 1, 3);
    // int value = max_quick_select(data, 0, n - 1, 2);
    int p = min_partition(data, 0, n - 1);
    // printf("%d\n", value);
    // float median = get_median(data, 0, n - 1);
    // printf("%0.2f\n", median);
    // quick_sort(data, 0, n - 1);
    for (int i = 0; i < n; i++)
        printf("%d ", data[i]);
    printf("\n");
}
