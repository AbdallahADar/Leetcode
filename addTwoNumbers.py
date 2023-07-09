# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def ListNode_from_list(l):
    head = ll = ListNode(l[0])
    for i in l[1:]:
        ll.next = ListNode(i)
        ll = ll.next
    return head

def list_from_ListNode(l):
    ll = []
    while l != None:
        ll.append(l.val)
        l = l.next
    return ll

def addTwoNumbers_string_trick(l1, l2):
    
    #We convert list to strings aka list of chars. Then we convert string to int and add the two numbers and then we reverse the string and iterate over it to create a listnode.
    
    s1 = ""
    s2 = ""

    while l1 != None:
        s1 = str(l1.val)+s1
        l1 = l1.next
    while l2 != None:
        s2 = str(l2.val)+s2
        l2 = l2.next

    ret = str(int(s1)+int(s2))

    d = ret_list = ListNode(int(ret[-1]))

    for i in ret[::-1][1:]:
        ret_list.next = ListNode(int(i))
        ret_list = ret_list.next

    return d
    

    
    
def addTwoNumbers_lists(l1, l2):
    
    #We convert to list and then pad the lists to be able to zip the lists together. Then we go over each element and then add them to get value and carry over accordingly.
    
    num1 = []
    num2 = []

    while l1 != None:
        num1.append(l1.val)
        l1 = l1.next
    while l2 != None:
        num2.append(l2.val)
        l2 = l2.next

    diff = len(num1) - len(num2)
    if diff > 0:
        num2 = num2 + [0]*diff
    else:
        num1 = num1 + [0]*-diff

    carry = 0
    carry, val = divmod(num1[0]+num2[0]+carry, 10)
    d = ret_list = ListNode(val)

    for i,j in zip(num1[1:],num2[1:]):

        carry, val = divmod(i+j+carry, 10)
        ret_list.next = ListNode(val)
        ret_list = ret_list.next

    if carry != 0:
        ret_list.next = ListNode(carry)
        ret_list = ret_list.next

    return d



def addTwoNumbers_dynamic(l1, l2):

    #We initialize a Linked List with ListNode of val 0 but when returning answer, we skip the first val. We go over the linkedlist and sum or carry over.

    ret = ret_list = ListNode()

    carry = 0

    while l1 or l2:

        #Initialize v1 and v2 with 0 in case the lists are of different size
        v1 = 0
        v2 = 0

        if l1: 
            v1 = l1.val
            l1 = l1.next

        if l2: 
            v2 = l2.val
            l2 = l2.next

        carry, val = divmod(carry + v1 + v2, 10)

        ret_list.next = ListNode(val)
        ret_list = ret_list.next

    if carry != 0:
        ret_list.next = ListNode(carry)
        ret_list = ret_list.next

    return ret.next