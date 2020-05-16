class Empty(Exception):
    """Error attempting to access an element from an empty queue"""
    pass


class Queue(object):

    DEFAULT_CAPACITY = 5

    def __init__(self):
        self._front = 0
        self._que = [None] * self.DEFAULT_CAPACITY
        self._size = 0

    def is_empty(self):
        """Return if queue is empty"""
        return self._size == 0

    def __len__(self):
        """Return length of queue"""
        return self._size

    def resize_queue(self):
        old = self._que
        index = [j % self.__len__() for j in range(self._front, self.__len__())]
        j = 0
        self.DEFAULT_CAPACITY *= 2
        self._que = [None] * self.DEFAULT_CAPACITY
        for i in index:
            self._que[j] = old[i]
            j += 1

    def enqueue(self, data):
        """Add element to the back of queue"""
        if self.__len__() == self.DEFAULT_CAPACITY:
                self.resize_queue()
        index = (self._front + self._size) % self.DEFAULT_CAPACITY
        self._que[index] = data
        self._size += 1

    def dequeue(self):
        """Remove element from the front of queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            data = self._que[self._front]
            self._que[self._front] = None
            self._size -= 1
            self._front = (self._front + 1) % self.DEFAULT_CAPACITY
            return data

    def first(self):
        """Return element at front"""
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self._que[self._front]


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()