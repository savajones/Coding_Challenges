# SUM LISTS

class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

class SumLists:
    def sumLists(self,list1,list2):
        tmp = 0
        result = []
        while True:
            if (list1 is not None) and (list2 is not None):
                sumList = list1.val + list2.val + tmp
                if sumList >= 10:
                    tmp = 1
                    sumList -= 10
                result.append(sumList)
                list1 = list1.next
                list2 = list2.next
            elif (list1 is None) and (list2 is not None):
                result.append(list2.val + tmp)
                tmp = 0
                list2 = list2.next
            elif (list1 is not None) and (list2 is None):
                result.append(list1.val + tmp)
                tmp = 0
                list1 = list1.next
            else: 
                break

        result1 = None
        for digit in reversed(result):
            result1 = ListNode(val=digit, next=result)

        return result1

tmp1 = ListNode(7, ListNode(1, ListNode(6)))
tmp2 = ListNode(5, ListNode(9, ListNode(2)))
    
# STACK MIN

from collections import deque

class stackMin:
    # Stack
    def __init__(self):
        self.stack = deque()
        self.min = None
 
    # Push
    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.min = val
        elif val > self.min:
            self.stack.append(val)
        else:
            self.stack.append(2*val - self.min)
            self.min = val
 
    # Pop
    def pop(self):
        if not self.stack:
            exit(-1)
        top = self.stack[-1]
        if top < self.min:
            self.min = 2*self.min - top
        self.stack.pop()
 
    # Minimum
    def getMin(self):
        return self.min

if __name__ == '__main__': 
    stack = stackMin()
    stack.push(6)
    stack.push(7)
    print(stack.getMin())
    stack.push(5)
    stack.push(3)
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())