class MinHeap:
    def __init__(self):
        self.heap=[]

    # Time Complexity : O(1)
    def getMin(self):
        return self.heap[0]

    # Time Complexity : O(1)
    def size(self):
        return len(self.heap)
    #Time Complexity : O(log(n))
    def insert(self, num):
        self.heap.append(num)
        self.bubbleUp(self.size() - 1)
        return self.heap

    # Time Complexity : O(log(n))
    def remove(self):
        self.heap[0], self.heap[self.size() - 1] = self.heap[self.size() - 1], self.heap[0]
        temp = self.heap.pop()

        self.bubbleDown(0)
        return temp

    def bubbleUp(self,ind):
        if ind == 0:
            return

        par = (ind - 1) // 2

        if par >= 0 and self.heap[ind] < self.heap[par]:
            self.heap[ind], self.heap[par] = self.heap[par], self.heap[ind]
            self.bubbleUp(par)

    def bubbleDown(self,ind):
        left = 2*ind + 1
        right = 2*ind +2
        temp = ind
        if left < self.size() and self.heap[left] < self.heap[temp]:
            temp = left
        if right< self.size() and self.heap[right] < self.heap[temp]:
            temp = right
        if temp == ind:
            return
        self.heap[ind], self.heap[temp] = self.heap[temp], self.heap[ind]
        self. bubbleDown(temp)
obi = MinHeap()
print(obi.insert(7))
print(obi.insert(10))
print(obi.insert(18))
print(obi.insert(26))
print(obi.insert(1))
print(obi.insert(11))
print(obi.size())
print(obi.remove())
print(obi.remove())
print(obi.remove())
print(obi.getMin())