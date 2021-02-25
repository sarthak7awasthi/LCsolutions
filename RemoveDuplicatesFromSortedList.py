# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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