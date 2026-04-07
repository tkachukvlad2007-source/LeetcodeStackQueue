class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class MyQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, x: int) -> None:
        new_node = Node(x)

        if self.empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def pop(self) -> int:
        if self.empty():
            return None

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def peek(self) -> int:
        if self.empty():
            return None

        return self.front.value

    def empty(self) -> bool:
        return self.front is None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
