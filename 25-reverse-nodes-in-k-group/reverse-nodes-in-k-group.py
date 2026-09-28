class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = head
        for _ in range(k):
            if not a: return head
            a = a.next
        p, q = None, head
        for _ in range(k):
            q.next, q, p = p, q.next, q
        head.next = self.reverseKGroup(q, k)
        return p