class Node:

    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def insertion(self,newNode):
        if self.root is None: # tree is empty
            self.root = newNode
        else:
            copyNode = self.root
            while True:
                if newNode.data < copyNode.data:
                    if copyNode.left is None:
                         copyNode.left = newNode
                         return 
                    else:
                        copyNode = copyNode.left
                else:
                    if copyNode.right is None:
                        copyNode.right = newNode
                        return 
                    else:
                        copyNode = copyNode.right



    def inOrderTravel(self,copyRoot):
        if copyRoot is None:
            return
        else:
            self.inOrderTravel(copyRoot.left) 
            print(f"{copyRoot.data}" ,end=" ")
            self.inOrderTravel(copyRoot.right)
        

    def preOrder(self,copyRoot):
        if copyRoot is None:
            return
        else:
            print(copyRoot.data , end=" ")
            self.preOrder(copyRoot.left)
            self.preOrder(copyRoot.right)

      

    def postOrder(self,copyNode):
        if copyNode is None:
            return
        else:
            self.postOrder(copyNode.left)
            self.postOrder(copyNode.right)
            print(copyNode.data , end=" ")

    def minValue(self):
        copyRoot = self.root

        while copyRoot.left:
            copyRoot = copyRoot.left
        print("\n Min value - ",copyRoot.data)

    def maxValue(self):
            copyRoot = self.root
    
            while copyRoot.right:
                copyRoot = copyRoot.right
            print(" Max value - ",copyRoot.data)

        

        
        


bst = BST()

bst.insertion(Node(100))
bst.insertion(Node(10))
bst.insertion(Node(450))
bst.insertion(Node(0))
bst.insertion(Node(65))
bst.insertion(Node(300))

bst.inOrderTravel(bst.root)
print()
bst.postOrder(bst.root)
print()
bst.preOrder(bst.root)

bst.minValue()
bst.maxValue()


