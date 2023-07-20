class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def balanceBST(root):

    def inorder(root):
        if root is None:
            return []
        return inorder(root.left) + [root.data] + inorder(root.right)
    
    nums = inorder(root)

    def list_to_BST(nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return BSTNode(nums[0])
        
        mid = len(nums) // 2
        new_node = BSTNode(nums[mid])
        new_node.left = list_to_BST(nums[:mid])
        new_node.right = list_to_BST(nums[mid+1:])


        return new_node
    
    return list_to_BST(nums)


def traverse(node): 
    if node is None: 
        return      
    print(node.data)
    traverse(node.left) 
    traverse(node.right)   

root = BSTNode(5)
root.left = BSTNode(3)
root.right = BSTNode(7)
root.right.left = BSTNode(6)
root.right.right = BSTNode(8)
root.right.right.right = BSTNode(9)
root.right.right.right.right = BSTNode(10)
print("Original node:")
print(traverse(root)) # 5, 3, 7, 6, 8, 9, 10

root = balanceBST(root)
print("After Balancing")
print(traverse(root)) # 7, 5, 3, 6, 9, 8, 10
