class node :

    def __init__(self,data,priority):
        self.data = data
        self.priority = priority
        self.next = None

class priorityQueue:

    def __init__(self):
        self.front = self.rear =None


    def enqueue(self,newNode):
        if self.front == None:
            self.front = newNode
            return

        if self.front.priority >   newNode.priority:
            newNode.next  = self.front
            self.front = newNode
            return
        else:    
            temp = self.front

            while temp.next:
                if temp.priority >=  newNode.priority:
                    break
                else:
                    prev = temp
                    temp = temp.next
            prev.next  = newNode
            newNode.next = temp


    def display(self):
        temp = self.front

        while temp :
            print(f"{temp.data} - {temp.priority} --> " ,  end="")
            temp= temp.next



pq = priorityQueue()

pq.enqueue(node(1,1))
pq.enqueue(node(2,2))
pq.enqueue(node(3,3))
pq.enqueue(node(4,5))
pq.enqueue(node(5,4))
pq.enqueue(node(6,6))
pq.enqueue(node(7,7))
pq.enqueue(node(8,8))
pq.enqueue(node(9,9))
pq.enqueue(node(10,10))
pq.enqueue(node(11,11))

pq.display()

            
                
                

