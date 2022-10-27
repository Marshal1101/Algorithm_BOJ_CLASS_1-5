import sys

input = sys.stdin.readline

class MinHeap :
    def __init__(self) :
        self.items = []
    
    def __comp(self, a, b) :
        return a < b

    def size(self) :
        return len(self.items)

    def __swap_value(self, a, b) :
        temp = self.items[a]
        self.items[a] = self.items[b]
        self.items[b] = temp

    def __parent_idx(self, index) :
        return ((index - 1) // 2)
    def __left_child_idx(self, index) :
        return ((index * 2 + 1))
    def __right_child_idx(self, index) :
        return ((index * 2 + 2))
    
    def peak(self) :
        return self.items[0]

    def add(self, item) :
        self.items.append(item)
        index = self.size() - 1
        parent_idx = self.__parent_idx(index)
        while parent_idx >= 0 and self.__comp(self.items[index], self.items[parent_idx]) :
            self.__swap_value(index, parent_idx)
            index = parent_idx
            parent_idx = self.__parent_idx(index)

    def poll(self) :
        if self.size() == 0 : return 0
        if self.size() == 1 : return self.items.pop()

        item = self.peak()
        self.items[0] = self.items.pop()

        index = 0
        left_idx = self.__left_child_idx(index)
        right_idx = self.__right_child_idx(index)

        while left_idx < self.size() :
            target = 0
            if right_idx < self.size() and self.__comp(self.items[right_idx], self.items[left_idx]) :
                target = right_idx
            else :
                target = left_idx
            if self.__comp(self.items[index], self.items[target]) : break
            else : self.__swap_value(index, target)

            index = target
            left_idx = self.__left_child_idx(index)
            right_idx = self.__right_child_idx(index)
        
        return item

N = int(input())
min_heap = MinHeap()
res = []
for _ in range(N) :
    order = int(input())
    if order == 0 :
        res.append(str(min_heap.poll()))
    else :
        min_heap.add(order)
print('\n'.join(res))