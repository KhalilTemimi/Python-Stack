class Node():
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
class DList():
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_front(self,val):
        if self.head == None:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
            print(f"A new node with the value ({self.tail.value}) just added to the front")
        else:
            DList.add_before(self,self.head.value,val)
        return self
    def add_to_back(self,val):
        if self.tail == None:
            DList.add_to_front(self,val)
        else:
            new_node = Node(val)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            print(f"A new node with the value ({self.tail.value}) just added to the back")
        return self
    def add_before(self,position,val):
        new_node = Node(val)
        runner = self.head
        while runner.value != position:
            runner = runner.next
        if runner.prev == None:
            new_node.next = runner
            runner.prev = new_node
            self.head = new_node
        else:
            new_node.next = runner
            new_node.prev = runner.prev
            runner.prev.next = new_node
            runner.prev = new_node
        print(f"A new node with the value ({new_node.value}) was added before ({position})")
        return self
    def add_after(self,position,val):
        new_node = Node(val)
        runner = self.head
        while runner.value != position:
            runner = runner.next
        if runner.next == None:
            new_node.prev = runner
            runner.next = new_node
            self.tail = new_node
        else:
            new_node.prev = runner
            new_node.next = runner.next
            runner.next.prev = new_node
            runner.next = new_node
        print(f"A new node with the value ({new_node.value}) was added after ({position})")
        return self
    def delete_node(self,val):
        runner = self.head
        while runner != None:
            if runner.value == val:
                if runner.prev == None:
                    self.head = runner.next
                    runner.next.prev = None
                    print(f"the first node with the value ({runner.value}) was deleted!")
                elif runner.next == None:
                    self.tail = runner.prev
                    runner.prev.next = None
                    print(f"the last node with the value ({runner.value}) was deleted!")
                else:
                    runner.prev.next = runner.next
                    runner.next.prev = runner.prev
                    print(f"the middle node with the value ({runner.value}) was deleted!")
            runner = runner.next
        return self

    def print_value(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

list1 = DList()
list1.add_to_back(5).add_to_back(6).add_before(5,4).add_after(6,7).add_to_front(1).delete_node(1).print_value()