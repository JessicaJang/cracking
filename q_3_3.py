# Chapter 3 Stacks and Queues
# Interview Questions 3.3 Stack of Plates

# Imagine a (literal) stack of plates. If the stack gets too high,
# it might topple. Therefore, in real life, we would likely start
# a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks
# should be composed of several stacks and should create a new stack once
# the previous one exceeds capacity.

# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a
# single stack (that is, pop() should return the same values as it would if
# there were just a single stack).

# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on 
# a specific sub-stack.

class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arrSet = []
        self.track = 0
    
    def isEmpty(self):
        if len(self.arrSet) == 0:
            return True
        return False
    
    def isFull(self):
        if len(self.arrSet[self.track]) == self.capacity:
            self.arrSet.append([])
            self.track += 1
    
    def push(self, item):
        if self.isEmpty():
            self.arrSet.append([item])
            return

        # check before adding item
        self.isFull()
        self.arrSet[self.track].append(item)
        print(self.arrSet)
    
    def pop(self):
        if self.isEmpty():
            print(self.arrSet)
            return
        
        tmp = self.arrSet[self.track].pop()
        if len(self.arrSet[self.track]) == 0:
            self.arrSet.pop()
            self.track -= 1
        
        print(self.arrSet)

        return tmp

if __name__ == "__main__":
    stack = SetOfStacks(5)
    print(stack.pop())
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(9)
    print(stack.pop())



            
        