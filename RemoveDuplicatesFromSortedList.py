# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# using Dictionary
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr=head
        Dict={}
        while curr!=None:
            if Dict.get(curr.val,0):
                prev.next=curr.next
            else:
                Dict[curr.val]=1
                prev=curr
            curr=curr.next
        return head
        
# without using Dictionary
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        prev=head
        curr=head.next
        while curr!=None:
            if prev.val==curr.val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return head