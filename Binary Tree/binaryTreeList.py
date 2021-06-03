
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    #The time complexity is O(1) and space complexity is O(n) because we are ininitalizing n elements.


    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There no node to delete"
        for i in range(1, self.lastUsedIndex):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"

# for deleteNode time complexity is O(n) but space complexity is O(1) 
# because no additional space is required.

    def deleteBT(self):
        self.customList = None
        return "The BT has been successfully deleted"

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")


#print(newBT.searchNode("Cold"))
#newBT.preOrderTraversal(1)
#newBT.postOrderTraversal(1)
#newBT.levelOrderTraversal(1)

#newBT.deleteNode("Tea")

print(newBT.deleteBT())
newBT.levelOrderTraversal(1)

