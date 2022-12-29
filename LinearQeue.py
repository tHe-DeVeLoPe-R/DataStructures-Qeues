class Element():
    def __init__(self, data):
        self.data = data
        self.next = None
class LinearQeue():
    front = None
    rear = None

    def enqeue(self, data):
        print("Enqueing - ",data)
        newElement = Element(data)
        if self.front  == None and self.rear == None:
            self.front = newElement
            self.rear = newElement
            return
        
        self.rear.next = newElement
        self.rear = newElement
        return
    
    def displayQeue(self):
        print("Displaying final qeue:")
        if self.front == None:
            print("Qeue is empty")
            return
        temp = self.front

        if(temp.next == None):
            print(temp.data)

        while(temp.next!=None):
            print(temp.data," -> ", end="")
            temp = temp.next
            if(temp.next == None):
                print(temp.data)
        return
    
    def deqeue(self):
        if self.front == None:
            print("Qeue is empty")
            return
        print(self.front.data,"Deqeued")
        if(self.front.next == None):
            self.front = None
            return
        self.front = self.front.next
        
    
    def peak(self):
        if(self.front == None):
            print("Qeue is empty")
            return
        print(self.front.data," is the peak of qeue")


def driver():
    lq = LinearQeue()
    lq.enqeue(2)
    lq.enqeue(3)
    lq.enqeue(4)
    lq.deqeue()
    lq.peak()
    lq.displayQeue()

driver()


        