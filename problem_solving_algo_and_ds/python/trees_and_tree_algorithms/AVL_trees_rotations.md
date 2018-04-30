### Left Rotation
---
* Promote the right child of the current root to be the _new root_ of the subtree.
* Move the old root to be the left child of the _new root_.
* If the new root had a left child make it the right child of the old root (which is now the new left child)

*Note:
Since the _new root_ was the right child of the old root, it means the right child of the old root is vaccant. This allows us to add a right child to the old root without any problems.*



            A                                       B
             \              =======>               / \
              B                                   /   \
               \                                 /     \
                C                               A       C




### Right Rotation
---
* Promote the left child to be the _new root_ of the subtree.
* Move the old root to be the right child of the _new root_.
* If the _new root_ already had a right child, then make it the left child of the old root (which is now the new right child)

*Note:
Since the _new root_ was the left child of the old root, the left child of the old root is guaranteed to be empty. This means we can add a left child to the old root without any issues.*

                E                               C
               / \                             / \
              C   F        =======>           B   E
             / \                             /   / \
            B   D                           A   D   F
           /
          A
