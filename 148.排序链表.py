#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 合并两个有序链表
    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy = ListNode(0)
        temp, temp1, temp2 = dummy, head1, head2
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next, temp1 = temp1, temp1.next
            else:
                temp.next, temp2 = temp2, temp2.next
            temp = temp.next
        # 处理剩余节点
        temp.next = temp1 if temp1 else temp2
        return dummy.next
    
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 特殊情况处理：空链表或只有一个节点
        if not head:
            return head

        length = 0
        node = head
        while node:
            node, length = node.next, length + 1
        
        # 虚拟头节点
        dummy = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummy, dummy.next  
            while curr:
                # 第一个子链表的头节点
                head1 = curr
                # 移动 curr 指针 subLength - 1 步，得到第二个子链表的头节点
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                # 第二个子链表的头节点
                head2 = curr.next
                curr.next = None  # 将第一个子链表与第二个子链表断开
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                    
                # 将两段链表切断，准备合并
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                
                # 合并两个子链表
                merged = self.merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength *= 2
        
        return dummy.next
        
         # 基本情况：链表为空或只有一个节点
        # if not head or not head.next:
        #     return head
        
        # # 第一步：找到链表的中间节点
        # slow, fast = head, head.next
        # while fast and fast.next:
        #     fast, slow = fast.next.next, slow.next
        
        # # 第二步：将链表分为两半
        # mid, slow.next = slow.next, None
        
        # # 第三步：递归排序两半
        # left = self.sortList(head)
        # right = self.sortList(mid)
        
        # # 第四步：合并已排序的两半
        # h = res = ListNode(0) # 哨兵节点
        # while left and right:
        #     if left.val < right.val:
        #         h.next, left = left, left.next
        #     else:
        #         h.next, right = right, right.next
        #     h = h.next
        
        # # 附加剩余节点
        # h.next = left if left else right
        
        # # 第五步：返回合并后的链表
        # return res.next
        
# @lc code=end

