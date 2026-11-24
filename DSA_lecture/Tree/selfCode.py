class Node:

    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None



class Tree:

    def __init__(self):
        self.root = None

    def insertionOfNode(self,root, newNode):
        if self.root is None:
            self.root = newNode
            return

        copyRoot = root

    

        if newNode.data < copyRoot.data and copyRoot.left is None:
            copyRoot.left = newNode
            return
        
        if newNode.data >=  copyRoot.data and copyRoot.right is None:
            copyRoot.right = newNode
            return


        if newNode.data < copyRoot.data and copyRoot.left is not None:
            self.insertionOfNode(copyRoot.left,newNode)
            return



        if newNode.data >=  copyRoot.data and copyRoot.right is not None:
                    self.insertionOfNode(copyRoot.right,newNode)
                    return




    def inOrderTravel(self,rootRef):
         

         if rootRef is None:
              return

         self.inOrderTravel(rootRef.left)
         print(f"{rootRef.data} ",end="")
         self.inOrderTravel(rootRef.right)

         

           
        



li = [54,23,145,154,13,53,24,654,24,76]
tr = Tree()

for i in li:
    tr.insertionOfNode(tr.root,Node(i))

tr.inOrderTravel(tr.root)


        