class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
def hotpotato(liste,num):
    s = Queue()
    for name in liste:
        s.enqueue(name)
    while s.size() > 1:
        for i in range(num):
            s.enqueue(s.dequeue())
        s.dequeue()
    return s.dequeue()
print(hotpotato(["tulin","sevde","naciye","hulya"],9))    
