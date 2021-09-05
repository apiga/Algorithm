def bellmanFord(graph, start) :
    """ ベルマンフォード法で始点から各頂点への最短距離を求めます。負の閉路がある場合、検出します。最短経路を求めるための配列も作成します。
        計算量 O(|V||E|)

    Args:
        graph (Graph): グラフ
        start (int): 始点

    Returns:
        tuple(bool, list[int], list[int]): 負の閉路があるかどうか, 始点から各頂点への最短距離, 最短経路の各頂点の前の頂点を格納する配列
    """

    global INF

    vCnt = len(graph.graph)

    # 負の閉路があるかどうか
    existNegativeCycle = False

    # 始点から各頂点への最短距離
    distance = list(INF for _ in range(vCnt))
    distance[start] = 0

    # 最短経路の前の頂点
    previous = list(int(-1) for _ in range(vCnt))

    for num in range(vCnt) :
        update = False

        for v in range(vCnt) :
            if distance[v] == INF :
                continue

            for edge in graph.graph[v] :
                if distance[edge.to] > distance[edge.start] + edge.weight :
                    distance[edge.to] = distance[edge.start] + edge.weight
                    previous[edge.to] = edge.start
                    update = True

        if not update :
            break

        if num == vCnt - 1 and update :
            existNegativeCycle = True

    return existNegativeCycle, distance, previous

def makeRoute(previous, start, goal) :
    """ 最短経路の各頂点の前の頂点を格納する配列と始点と終点から、最短経路を作成します。

    Args:
        previous (list[int]): 最短経路の各頂点の前の頂点を格納する配列
        start (int): 始点
        goal (int): 終点

    Returns:
        list[int]: 最短経路
    """
    # 経路
    route = list()

    now = goal

    while now != start :
        route.append(now)
        now = previous[now]

    route.append(start)

    return reversed(route)

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