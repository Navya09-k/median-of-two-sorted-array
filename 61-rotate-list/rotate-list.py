class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        n, tail = 1, head
        while tail.next: tail = tail.next; n += 1
        k %= n
        if not k: return head
        tail.next = head
        for _ in range(n-k): tail = tail.next
        head = tail.next
        tail.next = None
        return head