# define the Node class for linked list nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# define the merge_sorted_lists function to merge two sorted linked lists
def merge_sorted_lists(head1, head2):
    # base cases: one or both lists are empty
    if not head1:
        return head2
    if not head2:
        return head1
    
    # recursive case: compare head nodes and merge the remaining nodes
    if head1.data < head2.data:
        head1.next = merge_sorted_lists(head1.next, head2)
        return head1
    else:
        head2.next = merge_sorted_lists(head1, head2.next)
        return head2

# create the first sorted linked list: 1 -> 3 -> 5 -> 7
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)

# create the second sorted linked list: 2 -> 4 -> 6 -> 8
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)

# merge the two sorted linked lists
merged_head = merge_sorted_lists(head1, head2)

# print the merged linked list
current_node = merged_head
while current_node:
    print(current_node.data, end=' ')
    current_node = current_node.next
