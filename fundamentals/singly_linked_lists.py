class SLnode():
    def __init__(self,val):
        self.value = val
        self.next = None
class SList():
    def __init__(self):
        self.head = None
    def add_to_front(self,val):
        new_node = SLnode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def add_to_back(self,val):
        runner = self.head
        new_node = SLnode(val)
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def print_value(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    def remove_from_front(self):
        runner = self.head
        self.head = runner.next
        return (f"The first value ({runner.value}) was deleted !")
    def remove_from_back(self):
        runner = self.head
        while (runner.next != None):
            previous_runner = runner
            runner = runner.next
        previous_runner.next = None
        return (f"The last value ({runner.value}) was deleted !")
    def remove_val(self,val):
        if (val == self.head.value):
            msg = SList.remove_from_front(self)
            return msg
        runner = self.head
        while (runner.next != None):
            if (val == runner.value):
                previous_runner.next = runner.next
                return(f"The value in the middle ({runner.value}) was deleted !")
            previous_runner = runner
            runner = runner.next
        if (val == runner.value):
            msg = SList.remove_from_back(self)
            return msg
    def length_list(self):
        count = 0
        node = self.head
        while (node != None):
            count += 1
            node = node.next
        return count
    def insert_at(self,val,n):
        new_node = SLnode(val)
        length = SList.length_list(self)
        runner = self.head
        if (n == 0):
            new_node.next = self.head
            self.head = new_node
            return self
        elif (n == length):
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node
            return self
        count = 0
        while (runner.next != None):
            if (n == count):
                previous_runner.next = new_node
                new_node.next = runner
            previous_runner = runner
            runner = runner.next
            count += 1


my_list = SList()
my_list.add_to_front("Khalil").add_to_front("Welcome").add_to_front("Hi").add_to_back("You are the BOSS").print_value()
# first_value = my_list.remove_from_front()
# print(first_value)
# last_value = my_list.remove_from_back()
# print(last_value)
# my_list.print_value()
# p = my_list.remove_val("Welcome")
# print(p)
my_list.insert_at("middle",2)
my_list.print_value()
