
class Node :

    def __init__(self,data):
        self.data = data
        self.next = None


class Stack :

    def __init__(self):
        self.top = None


    def isEmpty(self):
        if self.top == None :
            return True
        else :
            return False

    def push(self,newNode):
        if self.top == None:
            self.top = newNode
            return id(self.top)
        else:
            newNode.next = self.top
            self.top = newNode
            return id(self.top)

    def pop(self):
        if self.top == None :
            print("stack is empty ")
            return 
        else :
            popNode = self.top
            self.top = self.top.next 
            popNode.next = None
            return popNode.data


    def displyStack(self):
        topCopy = self.top

        while topCopy :
            print(topCopy.data)
            topCopy = topCopy.next 

    def revesrString(self):
        li = []
        if self.top == None:
            return "stack is empty "
        else :
            while self.top:
               char =  self.pop()
               li.append(char)

            return li

    def revesUsingstack(self,prevStack):
        stack  = Stack()

        while prevStack.top != None:
            stack.push(Node(prevStack.top.data))
            prevStack.top = prevStack.top.next 

        print("printing value freom another stack ")

        stack.displyStack()
        

        pass
        


# stack1 = Stack()

# name = "shivam"

# for i in name:
#     newNode = Node(i)
#     stack1.push(newNode)

# stack1.revesUsingstack(stack1)


# Queu 

class Queu:

    def __init__(self):
        self.front = None
        self.rear = None

    def displayFront(self):
        if self.front ==  None :
           print(f" front points None ")
        else:
            print(self.front.data ," : front value")


    def enQueue(self,newNode):

        if self.front == None and self.rear == None :
            self.front = newNode
            self.rear = newNode

            return 
            
        self.rear.next = newNode
        self.rear = newNode

    def deQueu(self):

        if self.front == None :
             return f"{self.front}  is pointing none its empty "

        frontCopy = self.front
        self.front = self.front.next
        frontCopy.next  = None
        return frontCopy.data 


    def revesrUsingStack(self,preQueu):
        internalStack = Stack()
        reversedStackVal = []
        while preQueu.front != preQueu.rear:
            data = preQueu.deQueu()
            internalStack.push(Node(data))

        while internalStack != None:
            data = internalStack.pop()
            reversedStackVal.append(data)
            print(reversedStackVal)
        return reversedStackVal






queue = Queu()

name = "shivam"

for i in name:
    newNode = Node(i)
    queue.enQueue(i)

queue.displayFront()

