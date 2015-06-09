import lib.LinkedList as ll

linked_list = ll.LinkedList()

for i in range(0, 10, 2):
    linked_list.insert(i)

print linked_list

linked_list.reverse()

print linked_list