### The Structure Property

In order to make a heap work efficiently, we'll take advantange of the logarithmic nature of the binary tree. In order to guarantee logarithmic performance, we must keep out tree balanced. A balanced binary tree has roughly the same number of nodes on the left and right subtrees of the root. In implementing a heap we must keep our tree balanced by creating a *complete binary tree*. A complete binary tree is a tree in which each level has all of its nodes. The exception to this is the bottom level of the tree, which we fill in from left to right.


Another interesting property of a complete tree is that we can represent it using a single list. We do not need to use nodes and references or even lists of lists. **Because the tree is complete, the left child of a parent (at position p) is the node that is found in position 2p in the list. Similarly, the right child of the parent is at position 2p+1 in the list. To find the parent of any node in the tree, we can simply use Python’s integer division. Given that a node is at position n in the list, the parent is at position n/2.**


### The Heap Order Property

**The heap order property is as follows: In a heap, for every node *x* with parent *p*, the key in *p* is smaller than or equal to the key in *x*.**
