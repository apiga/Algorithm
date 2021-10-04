class BinaryIndexedTree:
    """ BinaryIndexedTree

    Attributes:
        size (int): 木のサイズ
        tree (list[int]): 木
        depth (int): 深さ
    """

    def __init__(self, n):
        self.size = n
        # 1-indexedで管理する。0は使わない。
        self.tree = list(int(0) for _ in range(n + 1))
        self.depth = n.bit_length()

    def add(self, index, weight):
        """ 値を加算します。
            計算量 O(log(N))

        Args:
            index (int): 加算する番号
            weight (int): 加算する値
        """
        while index <= self.size:
            self.tree[index] += weight
            index += index & -index

    def sum(self, index):
        """ 番号までの累積和を取得します。
            計算量 O(log(N))

        Args:
            index (int): 累積和を知りたい番号

        Returns:
            int: 累積和
        """

        sum_ = 0

        while index > 0:
            sum_ += self.tree[index]
            index -= index & -index

        return sum_

    def lowerBound(self, weight):
        """ 累積和の二分探索をします。
            計算量 O(log(N))
        Args:
            weight: 検索したい値

        Returns:
            int: 検索したい値以上になる最小のindex
            int: 直前までの累積和
        """
        sum_ = 0
        post = 0
        for i in range(self.depth, -1, -1):
            middle = post + (1 << i)
            if middle <= self.size and sum_ + self.tree[middle] < weight:
                sum_ += self.tree[middle]
                post += 1 << i
        return post + 1, sum_