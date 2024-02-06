#include "trees.h"
#include "bst.h"
#include "heap.h"

// gcc main.c ../stack/stack.c trees.c bst.c heap.c

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
    // root = insert(root, 12);
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
    // root = delete_node(root, 12);
    // bfs(root);
    // printf("%d\n", height(root));
    // printf("%d\n", count(root));

    // node *root = NULL;
    // root = insert(root, 15);
    // root = insert(root, 6);
    // root = insert(root, 18);
    // root = insert(root, 3);
    // root = insert(root, 7);
    // root = insert(root, 17);
    // root = insert(root, 20);
    // root = insert(root, 2);
    // root = insert(root, 4);
    // root = insert(root, 13);
    // root = insert(root, 9);

    // node *n = search_recursively(root, 20);
    // node *p = getPredecessor(n);
    // if (p)
    //     printf("predecessor: %ld\n", p->data);
    // node *s = getSuccessor(n);
    // if (s)
    //     printf("successor: %ld\n", s->data);

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
    // uint64 data[] = {0, 5, 9, 11, 14, 19, 21, 33, 17, 27};
    // uint8 size = sizeof(data) / sizeof(*data);
    // for (uint8 i = 0; i < 3; i++)
    // delete_root(data, size - i);
    // node *root = construct_heap(data, size - 3);
    // bfs(root);
    // uint64 *heap = heap_insert(data, size - 3, 15);
    // for (uint8 i = 0; i < size - 2; i++)
    // printf("%ld ", heap[i]);
    // node *root = construct_heap(heap, size - 2);
    // bfs(root);
    // bottom_up(data, size);

    // preorder: root, left, right
    // uint64 preorder[] = {3, 9, 20, 15, 7};
    // uint8 preorderSize = sizeof(preorder) / sizeof(*preorder);
    // inorder: left, root, right
    // uint64 inorder[] = {9, 3, 15, 20, 7};
    // uint8 inorderSize = sizeof(inorder) / sizeof(*inorder);
    // postorder: left, right, root
    // uint64 postorder[] = {9, 15, 7, 20, 3};
    // uint8 postorderSize = sizeof(postorder) / sizeof(*postorder);
    // node *root;
    // root = pre_in_construction(preorder, preorderSize, inorder, inorderSize);
    // bfs(root);
    // root = in_post_construction(inorder, inorderSize, postorder, postorderSize);
    // bfs(root);

    // expression tree
    // uint8 *infix = "((a+b)*(c-d))/(e+f)";
    // node *root = expression_tree(infix);
    // bfs(root, 1);

    // depth, height, isBalanced, count_unbalanced
    // node *root = create_node(13);

    // root->left = create_node(10);
    // root->right = create_node(25);

    // root->left->left = create_node(2);
    // root->left->right = create_node(12);
    // root->right->left = create_node(19);
    // root->right->right = create_node(20);

    // root->left->left->left = create_node(29);
    // root->left->left->right = create_node(30);
    // root->left->right->left = create_node(31);
    // root->left->right->right = create_node(32);
    // root->right->left->left = create_node(33);
    // root->right->left->right = create_node(34);
    // root->right->right->left = create_node(35);
    // root->right->right->right = create_node(36);

    // printf("count unbalanced: %d\n", count_unbalanced(root));

    // descending order traversal of bst
    // node *root = create_node(13);
    // root->left = create_node(3);
    // root->right = create_node(14);
    // root->left->left = create_node(1);
    // root->left->left->right = create_node(2);
    // root->left->right = create_node(4);
    // root->right->right = create_node(18);
    // root->left->right->right = create_node(12);
    // root->left->right->right->left = create_node(10);
    // root->left->right->right->left->right = create_node(11);
    // root->left->right->right->left->left = create_node(5);
    // root->left->right->right->left->left->right = create_node(8);
    // root->left->right->right->left->left->right->left = create_node(7);
    // root->left->right->right->left->left->right->right = create_node(9);
    // root->left->right->right->left->left->right->left->left = create_node(6);

    // height of the tree
    // printf("height: %d\n", height(root));
    // in_order(root);

    // descending_transversal(root);
    // printf("\n");
    // printf("count even: %d\n", count_even(root));

    // max heap
    // uint64 data[] = {100, 19, 36, 17, 3, 25, 1, 2, 7};
    // uint8 size = sizeof(data) / sizeof(*data);
    // top_down(data, size);
    // uint64 *heap = heap_insert(data, size, 21);
    // size++;
    // delete_root(heap, size);
    // size--;
    // node *root = construct_heap(heap, size);
    // bfs(root, 0);

    // heap duplicates
    // uint64 duplicates[] = {3, 2, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4};
    // uint8 size = sizeof(duplicates) / sizeof(*duplicates);
    // uint64 unique[] = {3, 2, 1, 4};
    // uint8 size = sizeof(unique) / sizeof(*unique);
    // top_down(duplicates, size);
    // printf("most frequent: %d\n", mostFrequent(unique, size));
    // node *root = construct_heap(unique, size);
    // bfs(root, 0);

    // general ordered trees
    // generalOrderedNode *root = create_general_ordered_node(1, 3);
    // root->children[0] = create_general_ordered_node(2, 3);
    // root->children[1] = create_general_ordered_node(3, 3);
    // root->children[2] = create_general_ordered_node(4, 3);
    // root->children[2]->children[0] = create_general_ordered_node(5, 3);
    // root->children[2]->children[1] = create_general_ordered_node(6, 3);
    // root->children[2]->children[2] = create_general_ordered_node(7, 3);
    // root->children[2]->children[1]->children[0] = create_general_ordered_node(8, 3);
    // root->children[2]->children[1]->children[1] = create_general_ordered_node(9, 3);
    // root->children[2]->children[2]->children[2] = create_general_ordered_node(10, 3);
    // root->children[2]->children[2]->children[2]->children[0] = create_general_ordered_node(11, 3);
    // root->children[2]->children[2]->children[2]->children[1] = create_general_ordered_node(12, 3);
    // root->children[2]->children[2]->children[2]->children[2] = create_general_ordered_node(13, 3);

    // generalOrderedNode *root = create_general_ordered_node(1, 3);

    // root->children[0] = create_general_ordered_node(2, 3);
    // root->children[1] = create_general_ordered_node(3, 3);
    // root->children[2] = create_general_ordered_node(4, 3);

    // root->children[0]->children[0] = create_general_ordered_node(5, 3);
    // root->children[0]->children[1] = create_general_ordered_node(6, 3);
    // root->children[0]->children[2] = create_general_ordered_node(7, 3);

    // root->children[1]->children[0] = create_general_ordered_node(8, 3);
    // root->children[1]->children[1] = create_general_ordered_node(9, 3);
    // root->children[1]->children[2] = create_general_ordered_node(8, 3);

    // root->children[2]->children[0] = create_general_ordered_node(9, 3);
    // root->children[2]->children[1] = create_general_ordered_node(10, 3);
    // root->children[2]->children[2] = create_general_ordered_node(10, 3);

    // root->children[2]->children[1]->children[0] = create_general_ordered_node(11, 3);

    // node *bt = general_to_binary(root);
    // bfs(bt, 0);
    // pre_order(bt);
    // printf("\n");
    // in_order(bt);
    // printf("\n");
    // post_order(bt);
    // printf("\n");

    // uint64 heap[] = {2, 3, 5, 5, 4, 6, 5, 26, 23, 10, 24, 7, 8, 6};
    // uint8 size = sizeof(heap) / sizeof(*heap);
    // insert 1 into the heap
    // uint64 *new_heap = heap_insert(heap, size, 1);
    // size++;
    // delete the root
    // delete_root(heap, size);
    // size--;
    // node *root = construct_heap(heap, size);
    // uint8 result = 0;
    // printf("longest path: %d\n", longestPath(root, &result));
    // printf("result: %d\n", result);

    // binary search trees with strings
    stringNode *root = NULL;
    root = insert_string(root, "ahmad");
    root = insert_string(root, "baher");
    root = insert_string(root, "ciao");
    root = insert_string(root, "d");
    root = insert_string(root, "eagle");
    root = insert_string(root, "fawzi");
    root = insert_string(root, "zein");

    in_order_string(root); // left root right
    printf("\n");
    return 0;
}
