"""
Heaps - 1/2
Medium

Implement a Min Heap class. The class should support 
insertion, 
removal(of the minimum / root value), 
peeking(of the minimum / root value), 
as well as sifting a value up and down the heap and 
building the heap from an input array. 
The heap should be represented in the form of an array.

Sample Input: [48,12,24,7,8,-5,24,391,24,56,2,6,8,41]
->buildHeap(array)
->insert(76)
->remove()
->remove()
->insert(87)

Sample Output:
->[-5,2,6,7,8,8,24,391,24,56,12,24,48,41]
->[-5,2,6,7,8,8,24,391,24,56,12,24,48,41,76]
->[2,7,6,24,8,8,24,391,76,56,12,24,48.41]
->[6,7,8,24,8,24,24,391,76,56,12,41,48]
->[6,7,8,24,8,24,24,391,76,56,12,41,48,87]
"""

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        p = (len(array)-2) // 2
        for i in reversed(range(p+1)):
            self.siftDown(i, array)
        return array

    def siftDown(self, idx, heap):
        """
        find the lower of both children.
        swap if the lower children is lower.
        """
        length = len(heap)
        c1 = idx * 2 + 1
        while c1 < length:
            c2 = idx * 2 + 2 if idx * 2 + 2 < length else None
            si = c2 if c2 is not None and heap[c2] < heap[c1] else c1
            if heap[si] < heap[idx]:
                heap[si], heap[idx] = heap[idx], heap[si]
                idx = si
                c1 = idx * 2 + 1
            else:
                break

    def siftUp(self, idx, heap):
        """
        Check against the parent value.
        swap if parent is greater.
        """
        p = (idx-1) // 2
        while idx > 0 and heap[p] > heap[idx]:
            heap[p], heap[idx] = heap[idx], heap[p]
            idx = p
            p = (idx-1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        """
        Swap the root and the final num in heap.
        remove and save the final num for return value.
        siftdown on the new root value.
        """
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        old_root = self.heap.pop()
        self.siftDown(0, self.heap)
        return old_root

    def insert(self, value):
        """
        append the value into the heap.
        siftup.
        """
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)
