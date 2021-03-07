class ListNode:
    """List node for LinkedList"""
    def __init__(self, value=0, nextNode=None):
        """Contain a value and a link on the next Node"""
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    """LinkedList - dynamic type based on ListNode"""
    def __init__(self):
        """Head attribute contain pointer on first node of our linked list"""
        self.head = None
        self.lenght = 0

    def insert(self, value):
        """Insert into first position, head element will be second"""
        self.head = ListNode(value, self.head)
        self.lenght += 1

    def remove_at_index(self, idx):
        """Remove any element from linked list"""
        dummy = ListNode(None, self.head)
        prev, curr = dummy, dummy.next
        check_idx = 0

        while curr:
            print(idx, check_idx)
            if idx == check_idx:
                prev.next = curr.next
                curr.next = None
            check_idx += 1
            prev, curr = curr, curr.next
        

class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextcat = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, cat):
        lastbox = self.head
        while lastbox:
            if cat == lastbox.cat:
                return True
            else:
                lastbox = lastbox.nextcat
        return False

    def addToEnd(self, newcat):
        newbox = Box(newcat)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while lastbox.nextcat:
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox

    def get(self, catIndex):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                return lastbox.cat
            boxIndex = boxIndex + 1
            lastbox = lastbox.nextcat

    def removeBox(self, rmcat):
        headcat = self.head

        if headcat is not None:
            if headcat.cat == rmcat:
                self.head = headcat.nextcat
                headcat = None
                return
        while headcat is not None:
            if headcat.cat == rmcat:
                break
            lastcat = headcat
            headcat = headcat.nextcat
        if headcat == None:
            return
        lastcat.nextcat = headcat.nextcat
        headcat = None