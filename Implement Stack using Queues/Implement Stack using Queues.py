class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyStack:

    def __init__(self):
        self.top_node = None


    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.top_node
        self.top_node = new_node


    def pop(self) -> int:
        if self.empty():
            return None
        value = self.top_node.value
        self.top_node = self.top_node.next
        return value


    def top(self) -> int:
        if self.empty():
            return None
        return self.top_node.value


    def empty(self) -> bool:
        return self.top_node is None



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
