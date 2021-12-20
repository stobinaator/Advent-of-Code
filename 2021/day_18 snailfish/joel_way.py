from dataclasses import dataclass
from typing import Optional, Union, Iterator, Tuple, List
import json


@dataclass
class Node:
    side: Optional[str] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    value: Optional[int] = None
    depth: int = 0
    parent: Optional["Node"] = None

    @property
    def is_pair(self):
        return self.left and self.right

    @property
    def is_value(self):
        return self.value is not None

    def root(self) -> "Node":
        node = self
        while node.parent:
            node = node.parent
        return node

    def magnitude(self) -> int:
        if self.is_pair:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()
        else:
            return self.value

    @staticmethod
    def parse(array: Union[list, int], parent: "Node" = None) -> "Node":
        """[9,[8,7]]"""
        depth = parent.depth + 1 if parent else 0
        if isinstance(array, int):
            return Node(value=array, parent=parent, depth=depth)
        node = Node(parent=parent, depth=depth)
        node.left = Node.parse(array[0], node)
        node.left.side = "left"
        node.right = Node.parse(array[1], node)
        node.right.side = "right"
        return node


def traverse(node: Node) -> Iterator[Node]:
    if node.is_pair:
        yield from traverse(node.left)
        yield node
        yield from traverse(node.right)
    else:
        yield node


def surrounding_value_nodes(node: Node) -> Tuple[Node, Node]:
    prev = None
    next = None
    target_seen = False

    for n in traverse(node.root()):
        if n == node:
            target_seen = True
        if n.is_value and n.depth <= node.depth:
            if not target_seen:
                prev = n
            else:
                next = n
                break

    return prev, next


def explode(node: Node) -> None:
    assert node.is_pair
    assert node.left.is_value
    assert node.right.is_value

    prev, next = surrounding_value_nodes(node)
    if prev:
        prev.value += node.left.value
    if next:
        next.value += node.right.value
    node.value = 0
    node.left.parent = None
    node.left = None
    node.right.parent = None
    node.right = None


def split(node: Node):
    assert node.is_value
    value = node.value
    l, r = (value // 2, value // 2) if value % 2 == 0 else (value // 2, value // 2 + 1)
    node.value = None
    node.left = Node(value=l, parent=node, depth=node.depth + 1)
    node.right = Node(value=r, parent=node, depth=node.depth + 1)


def reduce(root: Node) -> None:
    keep_going = True
    while keep_going:
        keep_going = False

        for node in traverse(root):
            if node.is_pair and node.depth >= 4:
                explode(node)
                keep_going = True
                break
            elif node.is_value and node.value >= 10:
                split(node)
                keep_going = True
                break


assert Node.parse([[[[5, 0], [7, 4]], [5, 5]], [6, 6]]).magnitude() == 1137


def add(left: Node, right: Node) -> Node:
    root = Node(left=left, right=right)
    for n in traverse(root):
        n.depth += 1
    root.depth = 0
    return root


def add_and_reduce(left: Node, right: Node) -> Node:
    root = add(left, right)
    reduce(root)
    return root


def do_homework(nodes: List[Node]) -> int:
    print(nodes)
    prev = add_and_reduce(nodes[0], nodes[1])
    for node in nodes[2:]:
        prev = add_and_reduce(prev, node)
    return prev.magnitude()


def do_homework_from_raw(raw: str) -> int:
    lines = raw.splitlines()
    nodes = [Node.parse(json.loads(line) for line in lines)]
    return do_homework(nodes)


RAW = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
# print(do_homework_from_raw(RAW))
