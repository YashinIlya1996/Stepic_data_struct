class TreeNode:
    def __init__(self, value=0, left=None, right=None, parent=None, height=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

    def print(self, mode='in-order'):
        if mode == 'pre-order':
            print(self.value, end=' ')
        if self.left is not None:
            self.left.print(mode)
        if mode == 'in-order':
            print(self.value, end=' ')
        if self.right is not None:
            self.right.print(mode)
        if mode == 'post-order':
            print(self.value, end=' ')


def main():
    import sys
    sys.stdin = open('input_6.1.txt', 'rt')
    n = int(input())
    nodes = []
    for _ in range(n):
        nodes.append(tuple(map(int, input().split())))
    root = TreeNode(value=nodes[0][0])
    sys.stdin.close()

    def generate_tree(node: TreeNode, index: int):
        node.value = nodes[index][0]
        if nodes[index][1] != -1:
            node.left = TreeNode()
            generate_tree(node.left, nodes[index][1])
        if nodes[index][2] != -1:
            node.right = TreeNode()
            generate_tree(node.right, nodes[index][2])

    generate_tree(root, 0)
    root.print(mode='in-order')
    print()
    root.print(mode='pre-order')
    print()
    root.print(mode='post-order')


if __name__ == '__main__':
    main()
