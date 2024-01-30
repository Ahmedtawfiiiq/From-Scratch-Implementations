// #include "bst.h"
#include "heap.h"

int main()
{

    // node *root = create_node(13);
    // root->left = create_node(10);
    // root->right = create_node(25);
    // root->left->left = create_node(2);
    // root->left->right = create_node(12);
    // root->right->left = create_node(20);
    // root->right->right = create_node(31);
    // root->right->right->left = create_node(29);
    // pre_order(root);
    // printf("\n");
    // in_order(root);
    // printf("\n");
    // post_order(root);
    // printf("\n");
    // bfs(root);
    // node *c = copy(root);
    // node *f = flip(root);
    // printf("%d\n", isIdentical(root, c));
    // bfs(f);

    // binary search trees
    // node *root = NULL;
    // root = insert(root, 5);
    // root = insert(root, 2);
    // root = insert(root, 18);
    // root = insert(root, 1);
    // root = insert(root, 3);
    // root = insert(root, 9);
    // root = insert(root, 21);
    // root = insert(root, 19);
    // root = insert(root, 25);

    // root = insert(root, 5);
    // root = insert(root, 2);
    // root = insert(root, 6);
    // root = insert(root, 4);
    // root = insert(root, 7);

    // bfs(root);
    // node *s = search_recursively(root, 33);
    // printf("%ld\n", s->parent->data);
    // root = delete_node(root, 0);
    // bfs(root);
    // printf("%d\n", height(root));
    // printf("%d\n", count(root));

    // root = insert(root, 33);
    // root = insert(root, 25);
    // root = insert(root, 40);
    // root = insert(root, 11);
    // root = insert(root, 34);
    // root = insert(root, 7);
    // root = insert(root, 12);
    // root = insert(root, 36);

    // node *p = getPredecessor(root, 33);
    // printf("predecessor: %ld\n", p->data);
    // node *s = getSuccessor(root, 33);
    // printf("successor: %ld\n", s->data);

    // root = insert(root, 7);
    // root = insert(root, 4);
    // root = insert(root, 12);
    // root = insert(root, 2);
    // root = insert(root, 6);
    // root = insert(root, 9);
    // root = insert(root, 19);
    // root = insert(root, 3);
    // root = insert(root, 5);
    // root = insert(root, 8);
    // root = insert(root, 11);
    // root = insert(root, 15);
    // root = insert(root, 20);
    // bfs(root);
    // printf("count: %d\n", count_bst(root, 10));
    // printf("count leaves: %d\n", count_leaves(root));
    // printf("count leaf sum: %d\n", count_leaf_sum(root));

    // heap
    // uint64 data[] = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
    // uint8 size = sizeof(data) / sizeof(*data);
    // node *root = construct_heap(data, size);
    // bfs(root);

    // uint64 data[] = {14, 20, 2, 15, 10, 21};
    // uint8 size = sizeof(data) / sizeof(*data);
    // top_down(data, size);
    // delete_root(data, size);
    // node *root = construct_heap(data, size);
    // bfs(root);

    // heap sort
    // uint64 data[] = {59, 36, 58, 21, 41, 97, 31, 16, 26, 53};
    // uint8 size = sizeof(data) / sizeof(*data);
    // heap_sort(data, size);
    // node *root = construct_heap(data, size);
    // bfs(root);
    uint64 data[] = {0, 5, 9, 11, 14, 19, 21, 33, 17, 27};
    uint8 size = sizeof(data) / sizeof(*data);
    for (uint8 i = 0; i < 3; i++)
        delete_root(data, size - i);
    // node *root = construct_heap(data, size - 3);
    // bfs(root);
    uint64 *heap = heap_insert(data, size - 3, 15);
    for (uint8 i = 0; i < size - 2; i++)
        printf("%ld ", heap[i]);
    // node *root = construct_heap(heap, size - 2);
    // bfs(root);
    // bottom_up(data, size);
    return 0;
}
