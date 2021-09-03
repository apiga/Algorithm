import heapq

def dijkstra(graph, start) :
    """ ダイクストラ法で始点から各頂点への最短距離を求めます。最短経路を求めるための配列も作成します。各頂点への最短経路の個数も求めます。
        計算量 O(|E|log|V|)

    Args:
        graph (Graph): グラフ
        start (int): 始点

    Returns:
        tuple(list[int], list[int], list[int]): 始点から各頂点への最短距離, 最短経路の各頂点の前の頂点を格納する配列, 各頂点への最短経路の個数
    """

    global INF

    vCnt = len(graph.graph)

    # 始点から各頂点への最短距離
    distance = list(INF for _ in range(vCnt))
    distance[start] = 0

    # 到達済みの頂点
    used = set()

    # 最短経路の前の頂点
    previous = list(int(-1) for _ in range(vCnt))

    # 最短経路の個数
    count = list(int(0) for _ in range(vCnt))
    count[start] = 1

    # 待ち行列
    reservedQueue = list()
    heapq.heapify(reservedQueue)
    heapq.heappush(reservedQueue, Vertex(start, distance[start]))

    while reservedQueue :
        nowVertex = heapq.heappop(reservedQueue)

        if nowVertex.num in used :
            continue

        used.add(nowVertex.num)

        for edge in graph.graph[nowVertex.num] :
            if distance[edge.to] > distance[edge.start] + edge.weight :
                # 最短距離を更新
                distance[edge.to] = distance[edge.start] + edge.weight

                # 最短経路の前の頂点を更新
                previous[edge.to] = edge.start

                # 最短経路の個数を更新
                count[edge.to] = count[edge.start]

                # 待ち行列に追加
                heapq.heappush(reservedQueue, Vertex(edge.to, distance[edge.start] + edge.weight))

            elif distance[edge.to] == distance[edge.start] + edge.weight :
                # 最短経路の個数を更新
                count[edge.to] += count[edge.start]

    return distance, previous, count

def makeRoot(previous, start, goal) :
    """ 最短経路の各頂点の前の頂点を格納する配列と始点と終点から、最短経路を作成します。

    Args:
        previous (list[int]): 最短経路の各頂点の前の頂点を格納する配列
        start (int): 始点
        goal (int): 終点

    Returns:
        list[int]: 最短経路
    """
    # 経路
    root = list()

    now = goal

    while now != start :
        root.append(now)
        now = previous[now]

    root.append(start)

    return reversed(root)

class Vertex :
    """ 頂点

    Attributes :
        num (int): 頂点番号
        distance (int): 距離
    """
    num = int()
    distance = int()

    def __init__(self, num, distance) :
        self.num = num
        self.distance = distance

    def __lt__(self, other) :
        return self.distance < other.distance

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