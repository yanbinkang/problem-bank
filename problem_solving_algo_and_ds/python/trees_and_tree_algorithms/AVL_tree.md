### Balanced Binary Search Trees
**AVL tree** is named for its inventors: G.M. Adelson-Velskii and E.M. Landis.


An AVL tree implements the Map abstract data type just like a regular binary search tree, the only difference is in how the tree performs. To implement our AVL tree we need to keep track of a **balance factor** for each node in the tree. We do this by looking at the heights of the left and right subtrees for each node. More formally, we define the balance factor for a node as the difference between the height of the left subtree and the height of the right subtree.

> _balanceFactor=height(leftSubTree)−height(rightSubTree)_

Using the definition for balance factor given above we say that **a subtree is left-heavy if the balance factor is greater than zero**. If the balance factor **is less than zero then the subtree is right heavy**. If the balance factor is zero then the tree is perfectly in balance. For purposes of implementing an AVL tree, and gaining the benefit of having a balanced tree we will define a tree to be in balance if the balance factor is -1, 0, or 1.

Once the balance factor of a node in a tree is outside this range we will need to have a procedure to bring the tree back into balance.
