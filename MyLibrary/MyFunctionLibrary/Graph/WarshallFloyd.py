def warshallFloyd(graph) :
    """ ワーシャルフロイド法で全頂点間の最短距離を求めます。負の閉路がある場合、検出します。
        計算量 O(|V|^3)

    Params:
        graph (Graph): グラフ

    Returns:
        tuple(bool, list(list[int]): 負の閉路があるかどうか, 全頂点間の最短距離
    """

    global INF

    vCnt = len(graph.graph)

    # 負の閉路が存在するかどうか
    existNegativeCycle = False

    # 最短経路を格納する配列
    dp = list(list(INF for j in range(vCnt)) for i in range(vCnt))

    for i in range(vCnt) :
        dp[i][i] = 0

    for i in range(vCnt) :
        for edge in graph.graph[i] :
            dp[i][edge.to] = edge.weight

    # k以下の頂点を使用した頂点iから頂点jまでの最短距離
    for k in range(vCnt) :
        for i in range(vCnt) :
            for j in range(vCnt) :
                if dp[i][k] != INF and dp[k][j] != INF:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # もし頂点iから頂点iまでの経路が負であるものがあれば、負の閉路が存在する
    for i in range(vCnt) :
        if dp[i][i] < 0 :
            existNegativeCycle = True

    return existNegativeCycle, dp

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