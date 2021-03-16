from ListNode import ListNode

class SinglyLinkedList:
    """docstring for SinglyLinkedList"""
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, val):
        self.head = ListNode(val=val, next=self.head)
        self.length += 1

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        curr = self.head
        idx = self.length - 1
        while curr.next:
            if idx == index:
                return curr.val
            curr = curr.next
            idx -= 1
        return curr.val


    def pop(self):
        del_item = self.head
        self.head = self.head.next
        del(del_item)
        self.length -= 1