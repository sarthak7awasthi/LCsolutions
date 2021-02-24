# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        Dict={}
        curr=head
        
        while curr!=None:
            if Dict.get(curr):
                return True
            else:
                Dict[curr]=1
            curr=curr.next
        return False