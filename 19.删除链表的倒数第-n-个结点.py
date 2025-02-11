#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # def getLength(head: ListNode) -> int:
        #     length = 0
        #     while head:
        #         length += 1
        #         head = head.next
        #     return length
        
        # length = getLength(head)
        # dummy = ListNode(0, head)
        # cur = dummy
        # for i in range(length - n):
        #     cur = cur.next
        # cur.next = cur.next.next
        
        # return dummy.next
        dummy = ListNode(0, head)
        first = head
        secone = dummy
        for _ in range(n):
            first = first.next
        while first:
            first = first.next
            secone = secone.next
        secone.next = secone.next.next
        return dummy.next
        
# @lc code=end

