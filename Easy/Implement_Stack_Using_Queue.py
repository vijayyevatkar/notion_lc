class MyQueue:
    
    stack = []
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
    

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tempStack = []
        self.copyFromSourceToTarget(self.stack,tempStack)
        answer = None
        if len(tempStack):
            answer = tempStack.pop()
        self.copyFromSourceToTarget(tempStack,self.stack)
        return answer
            
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        tempStack = []
        self.copyFromSourceToTarget(self.stack, tempStack)
        if len(tempStack):
            answer = tempStack.pop()
            tempStack.append(answer)
        self.copyFromSourceToTarget(tempStack,self.stack)
        return answer
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0        
        
    def copyFromSourceToTarget(self, source: List[int], target: List[int]) -> None:
        while len(source):
            target.append(source.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()