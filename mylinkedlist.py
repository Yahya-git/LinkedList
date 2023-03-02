

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next

    def compare(self, input):
        while self.head !=None and input.head !=None:
            if self.head.value == input.head.value:
                self.head=self.head.next
                input.head=input.head.next
                return True
            else:
                return False

    def search(self, value):
        current = self.head
        while(current != None):
            if current.value == value:
                return current.value
            current = current.next
        return False

    def sort(self):
        current = self.head
        if current is None:
                return
        while(current != None):
            index = current.next
            while(index != None):
                if current.value > index.value:
                    temp = current.value
                    current.value = index.value
                    index.value = temp
                index = index.next
            current = current.next
        

    def size(self):
        count = 0
        current = self.head
        while (current):
            count += 1
            current = current.next
        return count

    # def midpoint(self, head):
    #     current = head
    #     length = self.size()
    #     mid = length//2
    #     while mid != 0:
    #         current = current.next
    #         mid -= 1
    #     return current
    
    def getMiddle(self, head):
        if (head == None):
            return head
 
        slow = head
        fast = head
 
        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
             
        return slow

    def mergeSort(self, head):
        if head == None or head.next == None:
            return head

        middle = self.getMiddle(head)
        nexttomiddle = middle.next
        middle.next = None

        left = self.mergeSort(head)
        right = self.mergeSort(nexttomiddle)

        sortedlist = self.mergeSorted(left, right)
        return sortedlist
    
    def mergeSorted(self, left, right):
        result = None
        if left == None:
            return right
        if right == None:
            return left
        
        if left.value <= right.value:
            result = left
            result.next = self.mergeSorted(left.next, right)
        else:
            result = right
            result.next = self.mergeSorted(left, right.next)
        return result

    def insertAtStart(self, value):
        current = self.head
        new = Node(value)
        new.next=current
        self.head=new

    def insertAtEnd(self, value):
        new = Node(value)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new
        else:
            self.head = new

    def insertAt(self,prev,value):
        if prev is None:
            return False
        
        new = Node(value)
        new.next = prev.next
        prev.next = new

    def deleteAtStart(self):
        self.head = self.head.next

    def deleteAtEnd(self):
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next

        temp.next = None

    def deleteAt(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

linkedlist1=linkedlist()

linkedlist1.insertAtEnd(99)
linkedlist1.insertAtEnd(88)
linkedlist1.insertAtEnd(77)
linkedlist1.insertAtEnd(66)
linkedlist1.insertAtEnd(55)
linkedlist1.insertAtEnd(44)
linkedlist1.insertAtEnd(33)
linkedlist1.insertAtEnd(22)
linkedlist1.insertAtEnd(11)
linkedlist1.insertAtEnd(00)
# linkedlist1.insertAtStart(123)
# linkedlist1.insertAt(linkedlist1.head.next.next,456)

linkedlist2=linkedlist()

linkedlist2.insertAtEnd(99)
linkedlist2.insertAtEnd(88)
linkedlist2.insertAtEnd(77)
linkedlist2.insertAtEnd(66)
linkedlist2.insertAtEnd(55)
linkedlist2.insertAtEnd(44)
linkedlist2.insertAtEnd(33)
linkedlist2.insertAtEnd(22)
linkedlist2.insertAtEnd(11)
linkedlist2.insertAtEnd(00)
# linkedlist2.insertAtStart(123)
# linkedlist2.insertAt(linkedlist2.head.next.next,456)

linkedlist1.deleteAtEnd()
linkedlist1.deleteAtStart()
linkedlist1.deleteAt(0)

print("Found:", linkedlist1.search(99))
print("Found:", linkedlist2.search(100))

linkedlist1.sort()
linkedlist1.head = linkedlist1.mergeSort(linkedlist1.head)
linkedlist2.sort()
linkedlist2.head = linkedlist2.mergeSort(linkedlist2.head)

linkedlist1.display()
linkedlist2.display()

print("Size:", linkedlist1.size())
print("Midpoint:", linkedlist1.getMiddle(linkedlist1.head))
print("Do linked lists match:", linkedlist1.compare(linkedlist2))