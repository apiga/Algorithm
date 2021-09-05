def kruskal(graph) :
    """ クラスカル法で最小全域木の重みを求めます。
    計算量 O(|E|log|V|)

    Args:
        graph (Graph): グラフ

    Returns:
        int: 最小全域木の重み
    """
    vCnt = len(graph.graph)

    edges = list()
    for i in range(vCnt) :
        for edge in graph.graph[i] :
            edges.append(edge)

    edges.sort(key = lambda e : e.weight)

    unionFindTree = UnionFindTree(vCnt)

    totalWeight = 0

    for edge in edges :
        if unionFindTree.isSameTree(edge.start, edge.to) :
            continue

        unionFindTree.unite(edge.start, edge.to)

        totalWeight += edge.weight

    return totalWeight

class UnionFindTree:
    """ UnionFind木

    Attributes:
        parentList (list[int]): 親の情報
        belongGroupSize (list[int]): 属するグループのサイズ
    """

    def __init__(self, nodeNum):
        self.parentList = list(int(-1) for _ in range(nodeNum))
        self.belongGroupSize = list(int(1) for _ in range(nodeNum))

    def findRoot(self, target):
        """ 頂点が所属するグループの根を取得します。

        Args:
            target (int): 根を取得したい頂点

        Returns:
            int: 根
        """
        parent = self.parentList[target]

        if parent == -1:
            return target
        else:
            rootParent = self.findRoot(parent)
            self.parentList[target] = rootParent

            return rootParent

    def isSameTree(self, firstNode, secondNode):
        """ 2つの頂点が同じグループに属しているか判定します。
            計算量 O(α(N))

        Args:
            firstNode (int): 1つ目の頂点
            secondNode (int): 2つ目の頂点

        Returns:
            bool: 2つの頂点が同じグループに属しているかどうか
        """
        return self.findRoot(firstNode) == self.findRoot(secondNode)

    def unite(self, firstNode, secondNode):
        """ 2つの頂点が所属するグループを結合します。
            計算量 O(α(N))

        Args:
            firstNode (int): 1つめの頂点
            secondNode (int): 2つめの頂点

        Returns:
            bool: 結合したかどうか
        """
        firstNodeRoot = self.findRoot(firstNode)
        secondNodeRoot = self.findRoot(secondNode)

        if firstNodeRoot == secondNodeRoot:
            return False

        if self.belongGroupSize[firstNode] < self.belongGroupSize[secondNode]:
            firstNodeRoot, secondNodeRoot = secondNodeRoot, firstNodeRoot

        self.parentList[secondNodeRoot] = firstNodeRoot
        self.belongGroupSize[firstNodeRoot] += self.belongGroupSize[secondNodeRoot]

        return True

    def getBelongGroupSize(self, node):
        """ 頂点が所属しているグループのサイズを返します。
            計算量 O(1)

        Args:
            node (int): 頂点

        Returns:
            int: 頂点が所属しているグループのサイズ
        """
        return self.belongGroupSize[self.findRoot(node)]

    def getAllRoot(self):
        """ すべての根を返します。
            計算量 O(N)

        Returns:
            list[int]: すべての根
        """
        rootList = list()

        for node, parent in enumerate(self.parentList) :
            if parent == -1 :
                rootList.append(node)

        return rootList

class Graph :
    """ グラフ

    Attributes:
        graph (list[list[Edge]): グラフ
    """
    def __init__(self, vCnt) :
        self.graph = list(list() for _ in range(vCnt))

    def addEdge(self, start, to, weight) :
        """ 辺を追加します。

        Args:
            start (int): 始点
            to (int): 終点
            weight (int): 重み
        """
        self.graph[start].append(Edge(start, to, weight))

class Edge :
    """ 辺

    Attributes:
        start (int): 辺の始点
        to (int): 辺の終点
        weight (int): 辺の重み
    """
    start = int()
    to = int()
    weight = int()

    def __init__(self, start, to, weight) :
        self.start = start
        self.to = to
        self.weight = weight