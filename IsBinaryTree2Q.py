#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    def inOrder():
        index = 0
        stack = []
        result = []
        prev_value = -float('inf')  # Keeps track of the previous node's value
        prev_index = -1  # Keeps track of the previous index (node position)
        while True:
            if index != -1:
                stack.append(index)
                index = tree[index][1]  # Traverse left subtree
            elif stack:
                index = stack.pop()
                key, left, right = tree[index]
                if prev_index != -1:
                    # Ensure no integer overflow by using valid range checks
                    if key < prev_value or (key == prev_value and index <= prev_index):
                        return False  # invalid BST if current node key is smaller or equal (with invalid ordering)
                prev_value = key
                prev_index = index
                index = right  # Traverse right subtree
            else:
                break
        return True

    if not tree:  # If the tree is empty, it's a valid BST
        return True

    return inOrder()  # Perform in-order traversal to check the tree


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


# Use a separate thread to avoid recursion limits
threading.Thread(target=main).start()
