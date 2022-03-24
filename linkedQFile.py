# Node klass
class Node:
    # init metod för noden
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# LinkedQ klass
class LinkedQ:
    # init metod för LinkedQ, first och last declareras som None
    def __init__(self):
        self._first = None
        self._last = None

    # dequeue metoden som retunerar och tar bort första värdet från kön
    def dequeue(self):
        tmp2 = self._first.value
        self._first = self._first.next
        if self.isEmpty():
            self._last = None
        return tmp2

    # isEmpty retunerar True om kön är tom
    def isEmpty(self):
        if self._first is None:
            return True
        else:
            return False

    # enqueue tar in data och lägger det längst bak i kön
    def enqueue(self, value):
        if self.isEmpty():
            tmp = Node(value)
            self._first = tmp
            self._last = tmp

        else:
            tmp = self._last
            tmp.next = Node(value)
            self._last = tmp.next

    # retunerar längden på kön genom att loopa igenom länkade kön
    def size(self):
        n = self._first
        count = 0
        while n is not None:
            count = count + 1
            n = n.next
        return count

    def peek(self):
        if self._first is not None:
            return self._first.value
        return "#"

    def __str__(self):
        n = self._first
        q_str = ""

        while n is not None:
            q_str += str(n.value)
            n = n.next
        return q_str


