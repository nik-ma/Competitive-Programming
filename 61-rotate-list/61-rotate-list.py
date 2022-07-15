class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        length=0
        dummy=head
        while dummy:
            length+=1
            dummy=dummy.next
        if length==0:
            return head
        k=k%length
        if k==0:
            return head
        pointer=head
        val=length-k
        if val==0:
            return head
        print(val)
        while val>0:
            
            val-=1
            if val==0:
                temp=pointer.next
                pointer.next=None
                pointer=temp
            else:
                pointer=pointer.next
        # return pointer
        pt2=pointer
        while pointer.next:
            pointer=pointer.next
        pointer.next=head
        return pt2