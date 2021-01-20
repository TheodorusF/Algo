import sys

class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right
            self.height = 1

        def hdiff(self):
            l_hgt = self.left.height if self.left is not None else 0
            r_hgt = self.right.height if self.right is not None else 0
            return r_hgt - l_hgt

        def fixhight(self):
            l_hgt = self.left.height if self.left is not None else 0
            r_hgt = self.right.height if self.right is not None else 0
            self.height = max(l_hgt,r_hgt) + 1



def rotateRight(node):

    tmp = node.left
    node.left = tmp.right
    tmp.right = node
    node.fixhight()
    tmp.fixhight()

    return tmp 


def rotateLeft(node):

    tmp = node.right
    node.right = tmp.left
    tmp.left = node
    node.fixhight()
    tmp.fixhight()

    return tmp 


def balance(node):

    node.fixhight()
    if node.hdiff() == 2:
        if node.right.hdiff() < 0:
            node.right = rotateRight(node.right)
        return rotateLeft(node)
    if node.hdiff() == -2:
        if node.left.hdiff() > 0:
            node.left = rotateLeft(node.left)
        return rotateRight(node)
    return node


def insert(node, key):
    if node is None:
        return Node(key=key)

    if key > node.key:
        node.right = insert(node.right, key)
    elif key < node.key:
        node.left = insert(node.left, key)
    elif key == node.key:
        return node

    return balance(node)


def find(node, key):
    if node is None:
        return False

    if key == node.key:
        return True
    elif key > node.key:
        return find(node.right, key)
    else:
        return find(node.left, key)


def find_min(node):

    if node.left is not None:
        return find_min(node.left)
    else:
        return node


def remove_min(node):

    if node.left is None:
        return node.right
    node.left = remove_min(node.left)

    return balance(node)


def next(node, key):
    if node is None:
        return None

    cur_next = None
    next_node = None
    while node is not None:
        if node.key > key:
            cur_next = node.key
            node = node.left
        elif node.key <= key:
            node = node.right
    
    return cur_next


def prev(node, key):
    if node is None:
        return None

    cur_prev = None
    while node is not None:
        if node.key < key:
            cur_prev = node.key
            node = node.right
        elif node.key >= key:
            node = node.left
    
    return cur_prev


def delete(node, key):
    
    if node is None:
        return node
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    elif key == node.key:
        l = node.left
        r = node.right

        if r is None: 
            return l

        min_node = find_min(r)
        min_node.right = remove_min(r)
        min_node.left = l

        return balance(min_node)

    return balance(node)


def main():

    #fout = open("b.txt", "w")
    #fin = open("a.txt", "r")
    root = None
    #n = int(input())
    for line in sys.stdin:
        comd, num = line.split()
        num = int(num)
        if comd == "insert":
            root = insert(root, num)
        elif comd == "exists":
            sys.stdout.write(str(find(root, num)).lower() + '\n')
        elif comd == "next":
            sys.stdout.write(str(next(root, num)).lower() + '\n')
        elif comd == "prev":
            sys.stdout.write(str(prev(root, num)).lower() + '\n')
        elif comd == "delete":
            root = delete(root, num)
    print(root.key)
    print(root.left.key, ' ', root.right.key)


if __name__ == "__main__":
    main()