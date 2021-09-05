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