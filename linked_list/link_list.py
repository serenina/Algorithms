# This file deal with single linked list via the use of nodes

class Node(object):

    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def get_cargo(self):
        return self.cargo

    def get_next(self):
        return self.next

    def set_cargo(self, c):
        self.cargo = c

    def set_next(self, n):
        self.next = n

    def print_nodes(self):
        print self
        if self.next == None:
            print "end of the list"
        else:
            self.get_next().print_nodes()

    def match_item(self, item):
        return self.cargo == item

    def search_item(self, item):
        if self.match_item(item):
            print (item + " found!")
            return self
        else:
            if self.next == None:
                print (item + ' not found!')
            else:
                return self.get_next().search_item(item)



class Loose_list(object):
    def __init__(self):
        self._head = None
        self.count = 0

    # add a new node at the head of the list
    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self._head)
        self._head = new_node
        self.count += 1

    def search(self, search):
        return self._head.search_item(search)

    def print_list(self):
        return self._head.print_nodes()

    # remove all the nodes that contain the requested cargo
    def remove_node(self, cargo):
        current = self._head
        previous = None

        if self.count == 0:
            pass

        if self._head.match_item(cargo):
            self._head = self._head.next

        while current.get_next() != None:
            current = current.get_next()
            if current.match_item(cargo):
                self.count -= 1
                if previous == None:
                    self._head = current.get_next()
                else:
                    previous.set_next(current.get_next())
            else:
                previous = current



