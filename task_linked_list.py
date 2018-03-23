class Node(object):
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next = next_node


    def __repr__(self):
        """
        repr()
        """
        return "Node({})".format(self.data)

    @property # метод становиться геттером, обращаемся к data -> получаем значение
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        assert isinstance(next_node, Node)
        self.__next = next_node

    @next_node
    def next_node(self):
        self.__next = None

class LinkedList(object):
    def __init__(self, *values):
        self.__head = None
        self.__tail = None
        self.__length = 0
        for value in values:
            self.add(value)

    def _get(self, index):
        if index >= self.__lenth:
            return None
        current = self.__head
        while index:
            current.next_node
            index -= 1
        return current

    def __len__(self):
        """len(obj)"""
        return self.__length

    def __contains__(self, value):
        for v in self:
            if v == value:
                return True
            return False

    def add(self, value):
        self[None] = value

    def _getitem__(self, index):
        """obj[index]"""
        node = self._get(index)

        if node is None:
            raise IndexError

        return node.data

    def __setitem__(self, index, value):
        """obj[index] = value"""
        node =  Node(value)
        if self.__head is None:
            self.__head = self.__tail = node
        elif index == 0:
            node.next_node = self.__head
            self.__head = node
        elif index >= len(self):
            self.__tail.next_node = node
            self.__tail = node
        else:
            previous = self._get(index - 1)
            node.next_node = previous.next_node
            previous.next_node = node
        self.__length += 1

    def __delitem__(self, index):
        """del obj[index]"""

    def __inter__(self):
        """ должен вернуть итератор """
        return LinkedListIterator(self.__head)

    def __str__(self):
        return str([node for node in self])

class LinkedListIterator(object):
    def __init__(self, head):
        assert isinstance(head, Node)
        self.__current = head

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        value = self.__current.data
        self.__current = self.__current.next_node
        return value
