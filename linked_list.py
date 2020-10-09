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

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def get_node(self, position):
        node = self._head
        if position == 0:
            return node
        elif position < 0 or position >= self._length:
            return None
        else:
            for i in range(1, position+1):
                node = node._next
            return node

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._length += 1
        return self

    def add_to_head(self, value):
        new_head = Node(value)
        if self._length:
            new_head._next = self._head
        else:
            self._tail = new_head
        self._head = new_head
        self._length += 1
        return self

    def remove_head(self):
        if not self._head:
            return None
        old_head = self._head
        self._head = old_head._next
        self._length -= 1
        if not self._length:
            self._tail = None
        return old_head

    def remove_tail(self):
        if not self._tail:
            return None
        old_tail=self._tail
        self._length-=1
        if not self._length:
            self._head=None
            self._tail=None
        else:
            self._tail=self.get_node(self._length-1)
            self._tail._next=None
        return old_tail

    @property
    def __len__(self):
        return self._length

# Phase 2

    def contains_value(self, target):
        node = self._head
        while node:
            if node._value is target:
                return True
            node = node._next
        return False

    def insert_value(self, position, value):
        if position < 0 or position > self._length:
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

    def update_value(self, position, value):
        node_to_update = self.get_node(position)
        if node_to_update is not None:
            node_to_update._value = value
            return True
        return False

    def remove_node(self, position):
        if position < 0 or position >= self._length:
            return
        if position == 0:
            self.remove_head()
        if position == self._length - 1:
            return self.remove_tail()
        previous_node = self.get_node(position-1)
        node_to_remove = previous_node._next
        previous_node._next = node_to_remove._next
        self._length -= 1
        return node_to_remove

    def __str__(self):
        if not self._length:
            return "empty list"
        print_me = ""
        node = self._head
        while node:
            print_me+=node._value + ", "
            node = node._next
        return print_me

# Phase 1 Manual Testing:

# # 1. Test Node and LinkedList initialization
node = Node('hello')
print(node)                                     # <__main__.Node object at ...>
print("1.1", node._value)                              # hello
linked_list = LinkedList()
# # <__main__.LinkedList object at ...>
print(linked_list)
string = str(linked_list)
print(string)

# # # 2. Test getting a node by its position
print("1.2", linked_list.get_node(0))                # None

# # # 3. Test adding a node to the list's tail
linked_list.add_to_tail('new tail node')
# # print(linked_list.get_node(0))                # <__main__.Node object at ...>
print("1.3", linked_list.get_node(0)._value)         # `new tail node`

# # # 4. Test adding a node to list's head
linked_list.add_to_head('new head node')
# # print(linked_list.get_node(0))                # <__main__.Node object at ...>
print("1.4a", linked_list.get_node(0)._value)         # `new head node`
print("1.4b", linked_list.get_node(1)._value)         # "new tail node"

# # # 5. Test removing the head node
linked_list.remove_head()
# # `new tail node` because `new head node` has been removed
print("1.5a", linked_list.get_node(0)._value)
# # # `None` because `new head node` has been removed
print("1.5b",linked_list.get_node(1))

# # # 6. Test removing the tail node
print("1.6a", linked_list.get_node(0)._value)         # `new tail node`
linked_list.remove_tail()
print("1.6b", linked_list.get_node(0))                # None

# # # 7. Test returning the list length
print("1.7", linked_list.__len__)                                 # 0

# Phase 2 Manual Testing

# # 1. Test whether the list contains_value a value
#linked_list = LinkedList()
linked_list.add_to_head('new head node')
print("2.1a", linked_list.contains_value('new head node'))      # True
print("2.1b", linked_list.contains_value('App Academy node'))   # False

# # 2. Test inserting a node value into the list at a specific position
linked_list.insert_value(0, 'hello!')
print("2.2a", linked_list.get_node(0)._value)                   # `hello!`
print("2.2b", linked_list.get_node(1)._value)                   # new head

# # 3. Test updating a list node's value at a specific position
linked_list.update_value(0, 'goodbye!')
print("2.3a", linked_list.get_node(0)._value)                   # `goodbye!`
print("2.3b", linked_list.get_node(1)._value)    # new head

# # 4. Test removing a node value from the list at a specific position
# `new head node`
print("2.4a", linked_list.get_node(1)._value)
linked_list.remove_node(1)
print("2.4b", linked_list.get_node(1))                          # None

# # 5. Format the list as a string whenever `print()` is invoked
new_linked_list = LinkedList()
print(new_linked_list)                  # Empty List
new_linked_list.add_to_tail('puppies')
print(new_linked_list)                  # puppies
new_linked_list.add_to_tail('kittens')
print(new_linked_list)                  # puppies, kittens
