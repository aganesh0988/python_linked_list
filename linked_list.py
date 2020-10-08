"""
============================================================================
Implementation Exercise: Singly Linked List
============================================================================

-------
Phase 1:
-------
1. Node and LinkedList initialization
2. Getting a node by its position
3. Adding a node to the list's tail
4. Adding a node to list's head
5. Removing the head node
6. Removing the tail node
7. Returning the list length

-------
Phase 2:
-------

1. Check whether the list contains_value a value
2. Inserting a node value into the list at a specific position
3. Updating a list node's value at a specific position
4. Removing a node value from the list at a specific position
5. Format the list as a string whenever `print()` is invoked
"""

# Phase 1

# TODO: Implement a Linked List Node class here


class Node:
    # TODO: Set the `_value` `_next` node instance variables
    def __init__(self, value):
        self._value = value
        self._next = None

        # TODO: Implement a Singly Linked List class here


class LinkedList:
    # TODO: Set the `_head` node, `_tail` node, and list `_length` instance variables
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    # TODO: Implement the get_node method here

    def get_node(self, position):
        node = self._head
        if position == 0:
            return node
        elif position >= self._length:
            return None
        else:
            for i in range(1, position):
                node = node._next
            return node

    # TODO: Implement the add_to_tail method here

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._length += 1
        return self

    # TODO: Implement the add_to_head method here

    def add_to_head(self, value):
        new_head = Node(value)
        if self._length:
            new_head._next = self._head
        else:
            self._tail = new_head
        self._head = new_head
        self._length += 1
        return self

    # TODO: Implement the remove_head method here

    def remove_head(self):
        if not self._head:
            return None
        old_head = self._head
        self._head = old_head._next
        self._length -= 1
        if not self._length:
            self._tail = None
        return old_head

    # TODO: Implement the remove_tail method here

    def remove_tail(self):
        if not self._head:
            return
        else:
            node = self._head
            for i in range(1, self._length-1):
                self._tail = node
                node = node._next
            self._length -= 1
            if not self._length:
                self._head = None
            return node

    # TODO: Implement the __len__ method here

    @property
    def __len__(self):
        return self._length

# Phase 2

    # TODO: Implement the contains_value method here
    def contains_value(self, target):
        node = self._head
        while node:
            if node._value is target:
                return True
            node = node._next
        return False

    # TODO: Implement the insert_value method here

    def insert_value(self, position, value):
        if position < 0 or position >= self._length:
            return False
        elif position == 0:
            self.add_to_head(value)
            return True
        elif position is self._length:
            self.add_to_tail(value)
            return True

        new_node = Node(value)
        previous_node = self.get_node(position-1)
        node_to_move = previous_node._next
        previous_node._next = new_node
        new_node._next = node_to_move

    # TODO: Implement the update_value method here

    def update_value(self, position, value):
        if position < 0 or position >= self._length:
            return False
        else:
            self.get_node(position)._value = value
            return True

    # TODO: Implement the remove_node method here
    def remove_node(self, position):
        pass

    # TODO: Implement the __str__ method here
    # def __str__(self):
    #     return 'goodbye'

# Phase 1 Manual Testing:


# # 1. Test Node and LinkedList initialization
# node = Node('hello')
# # print(node)                                     # <__main__.Node object at ...>
# # print(node._value)                              # hello
# linked_list = LinkedList()
# # <__main__.LinkedList object at ...>
# # print(linked_list)
# # string = str(linked_list)
# # print(string)

# # # 2. Test getting a node by its position
# # print(linked_list.get_node(0))                # None

# # # 3. Test adding a node to the list's tail
# linked_list.add_to_tail('new tail node')
# # print(linked_list.get_node(0))                # <__main__.Node object at ...>
# # print(linked_list.get_node(0)._value)         # `new tail node`

# # # 4. Test adding a node to list's head
# linked_list.add_to_head('new head node')
# # print(linked_list.get_node(0))                # <__main__.Node object at ...>
# # print(linked_list.get_node(0)._value)         # `new head node`

# # # 5. Test removing the head node
# linked_list.remove_head()
# # `new tail node` because `new head node` has been removed
# # print(linked_list.get_node(0)._value)
# # # `None` because `new head node` has been removed
# # print(linked_list.get_node(1))

# # # 6. Test removing the tail node
# print(linked_list.get_node(0)._value)         # `new tail node`
# linked_list.remove_tail()
# print(linked_list.get_node(0))                # None

# # # 7. Test returning the list length
# print(linked_list.__len__)                                 # 0

# Phase 2 Manual Testing

# # 1. Test whether the list contains_value a value
linked_list = LinkedList()
linked_list.add_to_head('new head node')
# print(linked_list.contains_value('new head node'))      # True
# print(linked_list.contains_value('App Academy node'))   # False

# # 2. Test inserting a node value into the list at a specific position
linked_list.insert_value(0, 'hello!')
# print(linked_list.get_node(0)._value)                   # `hello!`

# # 3. Test updating a list node's value at a specific position
linked_list.update_value(0, 'goodbye!')
# print(linked_list.get_node(0)._value)                   # `goodbye!`

# # 4. Test removing a node value from the list at a specific position
# print(linked_list.get_node(1)._value)                   # `new head node`
# linked_list.remove_node(1)
# print(linked_list.get_node(1))                          # None

# # 5. Format the list as a string whenever `print()` is invoked
# new_linked_list = LinkedList()
# print(new_linked_list)                  # Empty List
# new_linked_list.add_to_tail('puppies')
# print(new_linked_list)                  # puppies
# new_linked_list.add_to_tail('kittens')
# print(new_linked_list)                  # puppies, kittens
