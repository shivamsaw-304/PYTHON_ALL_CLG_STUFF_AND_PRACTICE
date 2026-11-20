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

  

        

        
        


bst = BST()

bst.insertion(Node(100))
bst.insertion(Node(10))
bst.insertion(Node(450))
bst.insertion(Node(0))
bst.insertion(Node(65))
bst.insertion(Node(300))

bst.inOrderTravel(bst.root)



