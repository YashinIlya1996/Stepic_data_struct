class TreeNode:
    answer = []

    def __init__(self, value=0, left=None, right=None, parent=None, height=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

    def generate_in_order(self):
        if self.left is not None:
            self.left.generate_in_order()
        TreeNode.answer.append(self.value)
        if self.right is not None:
            self.right.generate_in_order()


def main():
    import sys
    sys.setrecursionlimit(10000)
    # sys.stdin = open('input_6.2.txt', 'rt')
    n = int(input())
    nodes = []
    for _ in range(n):
        nodes.append(tuple(map(int, input().split())))
    # sys.stdin.close()

    def generate_tree(node: TreeNode, index: int):
        node.value = nodes[index][0]
        if nodes[index][1] != -1:
            node.left = TreeNode()
            generate_tree(node.left, nodes[index][1])
        if nodes[index][2] != -1:
            node.right = TreeNode()
            generate_tree(node.right, nodes[index][2])

    answer = 'CORRECT'
    if nodes:
        root = TreeNode(value=nodes[0][0])
        generate_tree(root, 0)
        root.generate_in_order()
        answer_list = TreeNode.answer

        for ind, val in enumerate(answer_list[1:]):
            if val <= answer_list[ind]:
                answer = 'INCORRECT'
                break
    print(answer)


if __name__ == '__main__':
    main()
