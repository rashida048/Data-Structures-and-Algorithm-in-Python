
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode('Drinks')
hot = TreeNode('hot')
cold = TreeNode('cold')

newBT.leftChild = hot
newBT.rightChild = cold

tea = TreeNode('tea')
coffee = TreeNode('coffee')

hot.leftChild = tea
hot.rightChild= coffee

#print(newBT.data)

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

#preOrderTraversal(newBT)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

#inOrderTraversal(newBT)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

import QueueLinkedList as queue

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not (customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if (root.value.leftChild is not None):
            customQueue.enqueue(root.value.leftChild)

        if (root.value.rightChild is not None):
            customQueue.enqueue(root.value.rightChild)
    
#levelOrderTraversal(newBT)


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return 
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not (customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value.data == nodeValue:
            return "Success!"
        if (root.value.leftChild is not None):
            customQueue.enqueue(root.value.leftChild)

        if (root.value.rightChild is not None):
            customQueue.enqueue(root.value.rightChild)
    return "Not Found"

        
#print(searchBT(newBT, "cola"))

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not (customQueue.isEmpty()):
        root = customQueue.dequeue()
        if (root.value.leftChild is not None):
            customQueue.enqueue(root.value.leftChild)
        else:
            root.value.leftChild = newNode
            return "Success!"
        
        if (root.value.rightChild is not None):
            customQueue.enqueue(root.value.rightChild)
        else:
            root.value.rightChild = newNode
            return "Success!"

#new = TreeNode("cola")
#insertNodeBT(newBT, new)
#levelOrderTraversal(newBT)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

#print(getDeepestNode(newBT))

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return 
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value.data == node:
            dNode = getDeepestNode(rootNode)
            root.value.data = dNode.data
            deleteDeepestNode(rootNode, dNode)
            return "The node has been successfully deleted!"
        if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
        if (root.value.rightChild is not None):
            customQueue.enqueue(root.value.rightChild)
    return "Failed!"

#deleteNodeBT(newBT, "tea")
#deleteDeepestNode(newBT, 'tea')
#levelOrderTraversal(newBT)

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted!"

























    