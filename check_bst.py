class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def check(root, min_value, max_value):
    if root is None:
        return True
    if root.data <= min_value or root.data >= max_value:
        return False
    return check(root.left, min_value, root.data) and check(root.right, root.data, max_value)


def checkBST(root):
    return check(root, 0, 10000)


# Enter your code here
if __name__ == '__main__':

    tree = BinarySearchTree()
    t = 2
    arr = [4, 2, 3, 1, 7, 6]

    for i in range(t):
        tree.create(arr[i])

    print(checkBST(tree.root))
