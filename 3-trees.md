# Trees

A Tree data structure has many similarities to a linked list. Trees also have nodes that are connected to each other. The difference is that the nodes in a tree can connect to multiple different nodes. 

A binary tree is called such because each node can connect to two child nodes. It is easiest to visualize this by thinking of an upside down tree. The top node is called the root. The nodes at the bottom that do not have any child nodes are called leaf nodes. 

![https://camo.githubusercontent.com/28113782284110eee2c00eb7acad5d376f2d3c5a3c588a3bd48539cf5fce6717/68747470733a2f2f7777772e6261656c64756e672e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031372f31322f547265652d312e6a7067](binary-tree.jpg)

The next step of tree is called a binary search tree (BST). The only difference between a binary tree and a binary search tree is where on the tree the data is stored. A binary tree does not care what order the data is stored, as long as it is stored on the tree. A BST will look at the value of the node and assign it a place either lower, to the left, or higher, to the right, of the parent nodes. The picture above is a BST. These trees are sorted making it easier to access the data found within a tree. 

## Balance in BST

In order for a BST to perform at an O(log n), it needs to be balanced. A balanced binary search tree is unique in that any one side of the tree is not significantly larger than the other. To solve this issue, the tree needs to be reorganized. The picture below demonstrates what an unbalanced tree might look like (on the left) and how to organize it to make it balanced (either picture on the right).

![https://leetcode.com/problems/balance-a-binary-search-tree/](unbalanced-BST.png)


## Functions of a tree

There are 

## Inserting



## Traversing

## Removing



## Why use a tree?

While a linked list can be used to store most any kind of data, a tree is best used with numerical values. A tree data structure performes slightly worse to a linked list with its main functions resulting in a O(log n) rather than an O(1). However, binary search trees have many advantages. First, a BST is automatically sorted when inserting new data. This makes it much easier to find the data we have stored. The binary element of a BST means that we can also use binary when searching through the tree. If we want to see if a value is in the tree, we just have to check if the value is higher or lower than the current node and move accordingly.


## Completed problem solved with a Tree

## Tutorial problem for student to complete

You can check your code with the solution here: [Solution](problem3.py)

[Back to Welcome Page](0-welcome.md)
