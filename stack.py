class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class ArrayStack(object):
    """LIFO stack implimentation"""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        else:
            return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        else:
            return self._data[-1]


def validateExpression(expression):
    St = ArrayStack()
    openB = '({['
    closeB = ')}]'
    for each in expression:
        if each in openB:
            St.push(each)
        elif each in closeB:
            b = St.pop()
            if openB.index(b) != closeB.index(each):
                return False
    return True


def reverseFile(filePath='The Adventures of Sherlock Holmes.txt'):
    St = ArrayStack()
    
    with open(filePath, 'r', encoding='utf-8') as ebook:
        for line in ebook:
            St.push(line.rstrip('\n'))

    with open(filePath+"-Rev.txt", 'w') as ebook:
        while (len(St)):
            ebook.write(St.pop() + '\n')

def markupTagMatching(html):
    St = ArrayStack()

    j = html.find('<', 0)
    while j != -1:
        k = html.find('>', j)
        if k == -1:
            return False
        else:
            tag = html[j+1:k]
            if not tag.startswith('/'):
                St.push(tag)
            else:
                if St.is_empty():
                    return False
                elif tag[1:] != St.pop():
                    return False
        j = html.find('<', k)
    
    return St.is_empty()
 


if __name__ == "__main__":
    S = ArrayStack()                # contents: [ ]
    S.push(5)                       # contents: [5]
    S.push(3)                       # contents: [5, 3]
    print(len(S))                   # contents: [5, 3];      outputs 2
    print(S.pop())                  # contents: [5];         outputs 3
    print(S.is_empty())             # contents: [5];         outputs False
    print(S.pop())                  # contents: [ ];         outputs 5
    print(S.is_empty())             # contents: [ ];         outputs True
    S.push(7)                       # contents: [7]
    S.push(9)                       # contents: [7, 9]
    print(S.top())                  # contents: [7, 9];      outputs 9
    S.push(4)                       # contents: [7, 9, 4]
    print(len(S))                   # contents: [7, 9, 4];   outputs 3
    print(S.pop())                  # contents: [7, 9];      outputs 4
    S.push(6)                       # contents: [7, 9, 6]

    # Reverse file using stack
    reverseFile(filePath='The Adventures of Sherlock Holmes.txt')

    # Arithematic exepression validation using stack
    expression = "((1+3)*(3+[4/2]+{3+[4/2]}))"
    expression2 = "(5]+4*4)"
    str = "valid" if validateExpression(expression) else "invalid"
    print("Expression is {0}".format(str))
    str = "valid" if validateExpression(expression2) else "invalid"
    print("Expression is {0}".format(str))
    
    # Match tag in markup language
    html = """<html><head><title>This is a title</title></head><body><p>Hello world!</p></body></html>"""
    html2 = """<html><head><title>This is a title</title><body>Hello world!</p></body></html>"""
    str = "valid" if markupTagMatching(html) else "invalid"
    print("Markup format is {0}".format(str))
    str = "valid" if markupTagMatching(html2) else "invalid"
    print("Markup format is {0}".format(str))