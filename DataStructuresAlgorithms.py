from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None

#----------------Tree Traversal Methods---------------------
#---------------------------------------------------------------------
### BFS

#O(n) time/space
    def breadth_first_search(self):
        if not self.root:
            raise Exception("Tree is empty")
        queue = deque()
        queue.append(self.root)
        visited = []
        while queue:
            current = queue.popleft()
            visited.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return visited

#O(n) Simpler
    def level_order_traversal(root):
        if not root:
            return
        queue = deque([root])
        while queue:
            current = queue.popleft()
            print(current.data, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

#---------------------------------------------------------------------
### Preorder Traversal

#O(n) time/space-----Iterative
    def dfs_pre_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty")
        stack = [self.root]
        visited = []
        while stack:
            visited_node = stack.pop()
            visited.append(visited_node.data)
            if visited_node.left:
                queue.append(visited_node.left)
            if visited_node.right:
                queue.append(visited_node.right)
        return visited

#O(n) time/space------Recursive
    def dfs_pre_order_recursive(self):
        if not self.root:
            raise Exception("Tree is empty")
        visited = []
        def traverse(node):
            if node:
                visited.append(node.data)
                traverse(node.left)
                traverse(node.right)
            return
        traverse(self.root)
        return visited
    
#O(n) Simpler---------Recursive
    def preorder_traversal(root):
        if root is None:
            return
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
    
#----------------------------------------------------------------------
### Inorder Traversal

#O(n) time/space-------Iterative
    def dfs_in_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty")
        current_node = self.root
        stack = []
        visited = []
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                visited_node = stack.pop()
                visited.append(visited_node)
                if not visited_node.right:
                    continue
                current_node = visited_node.right
        return visited
    
#O(n) time/space-------Recursive
    def dfs_in_order_recursive(self):
        if not self.root:
            raise Exception("Tree is empty")
        visited = []
        def traverse(node):
            if node:
                traverse(node.left)
                visited.append(node.data)
                traverse(node.right)
            return
        

#O(n) Simple---------Recursive
    def inorder_traversal(root):
        if root is None:
             return
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

#---------------------------------------------------------------------------------
### Postorder Traversal

#O(n)------------Iterative
    def dfs_post_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty")
        current = previous = self.root
        stack = []
        visited = []
        while current:
            while current.left:
                stack.append(current)
                current = current.left
            while not current.right or current.right == previous:
                visited.append(current.data)
                previous = current
                if not stack:
                    return visited
                current = stack.pop()
            stack.append(current)
            current = current.right

#O(n)-----------Recursive
    def dfs_post_order_recursive(self):
        if not self.root:
            raise Exception("Tree is empty")
        visited = []
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                visited.append(node.data)
            return        
        traverse(self.root)
        return visited

    

#O(n)Simpler---------Recursive
    def postorder_traversal(root):
        if root is None:
            return
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ') 


# Initialize the binary tree
tree = Binary_Tree()

# Create and assign nodes
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# --------Perform function call----------
# Replace function call with any functions defined above
tree.breadth_first_search()
print(tree.breadth_first_search())