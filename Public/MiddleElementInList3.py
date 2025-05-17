# Definition of a ListNode for linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Function to find the middle element of an array using slow and fast pointers
def findMiddle(nums):
    slow = 0
    fast = 0
    
    while fast < len(nums) and fast + 1 < len(nums):
        slow += 1
        fast += 2
    
    return nums[slow]

# Function to find the middle element of a linked list using slow and fast pointers
def findMiddleLinkedList(head):
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

# Main function
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Middle element of array:", findMiddle(nums))
    
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print("Middle element of linked list:", findMiddleLinkedList(head))