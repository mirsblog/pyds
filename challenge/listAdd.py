class ListNode:
    def __init__(self, x, nxt=None):
         self.val = x
         self.next = nxt

def addTwo(l1, l2):

    if not l1 and not l2:
        return

    c = 0
    r = 0
    l3 = None
    tmp = None

    while True:
        if not l1 and not l2:
            break

        n1 = 0
        if l1:
            n1 = l1.val
            l1 = l1.next

        n2 = 0
        if l2:
            n2 = l2.val
            l2 = l2.next

        # add numbers
        n3 = n1 + n2 + c
        c = n3 // 10
        r = n3 % 10

        # store r in listnode
        node = ListNode(r)
        if l3 is None:
            tmp = node
            l3 = tmp
        else:
            tmp.next = node
        tmp = tmp.next

    if c > 0:
        node = ListNode(c)
        tmp.next = node

    return l3

def printListNode(l):
    while l is not None:
        print(l.val)
        l = l.next

if __name__ == "__main__":
    l1 = ListNode(0)
    l2 = ListNode(0)
    l3 = addTwo(l1, l2)
    printListNode(l3)
