#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  def inOrder():
    index = 0
    stack = []
    result = []
    while True:
      if index != -1:
        stack.append(index)
        index = tree[index][1]
      elif stack:
        index = stack.pop()
        result.append(tree[index][0])
        index = tree[index][2]
      else:
        break
    return result

  if not tree:  # if the tree is empty
    return True
  traversal = inOrder()
  return all(traversal[i] < traversal[i+1] for i in range(len(traversal)-1))


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
