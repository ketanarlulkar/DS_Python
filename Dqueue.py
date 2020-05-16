class Empty(Exception):
    """Error attempting to access an element from an empty queue"""
    pass


class DQueue(object):

    def __init__(self):
        self._que = []

    def is_empty(self):
        """Return if queue is empty"""
        return len(self) == 0

    def __len__(self):
        """Return length of queue"""
        return len(self._que)

    def first(self):
        """Return (but do not remove) the first element of deque D; 
        an error occurs if the deque is empty."""
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self._que[0]

    def last(self):
        """Return (but do not remove) the last element of deque D;
        an error occurs if the deque is empty."""
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self._que[-1]

    def add_last(self, data):
        """Add element to the back of queue"""
        self._que.append(data)

    def delete_first(self):
        """Remove element from the front of queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self._que.pop(0)

    def add_first(self, data):
        self._que.insert(0, data)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
           return self._que.pop()


def check_palindrome(string):
    q = DQueue()
    for each in string:
        q.add_last(each)
    length = len(q)//2
    while length:
        if q.delete_first() != q.delete_last():
            return False
        length -= 1

    if len(q) <= 1:
        return True


if __name__ == "__main__":
    q = DQueue()
    q.add_first(10)
    q.add_last(20)
    q.add_first(30)
    q.add_last(40)
    q.delete_first()
    q.delete_last()
    q.delete_first()
    q.delete_last()

    # Palindrome Checker
    strings = ["palin", "dad", "mom", "funggnuf"]
    for each in strings:
        str = "" if check_palindrome(each) else "not"
        print("{0} is {1} palindrome".format(each, str))
