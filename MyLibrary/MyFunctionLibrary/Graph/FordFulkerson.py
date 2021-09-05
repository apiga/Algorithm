seen = set()

def fordFulkerson(networkFlowGraph, start, end) :
    """ フォード・ファルカーソン法で最大流を求めます。
        計算量 O(F|E|)

    Args:
        networkFlowGraph (NetworkFlowGraph): ネットワークフローグラフ
        start (int): 始点
        end (int): 終点

    Returns:
        int: 最大流
    """
    global INF, seen

    maxFlow = 0

    while True :
        seen = set()

        flow = fordFulkersonDepthFirstSearch(networkFlowGraph, start, end, INF)

        if flow == 0 :
            return maxFlow

        maxFlow += flow

def fordFulkersonDepthFirstSearch(networkFlowGraph, now, end, nowFlow) :
    """ フォード・ファルカーソン法用に、始点から終点までのフローを求めるための深さ優先探索をします。

    Args:
        networkFlowGraph (NetworkFlowGraph): ネットワークフローグラフ
        now (int): 現在地点
        end (int): 終点
        nowFlow (int): 現在の流量

    Returns:
        int: 流量
    """
    global seen
    if now == end :
        return nowFlow

    seen.add(now)

    for edge in networkFlowGraph.graph[now] :
        if edge.to in seen :
            continue

        if edge.capacity == 0 :
            continue

        flow = fordFulkersonDepthFirstSearch(networkFlowGraph, edge.to, end, min(nowFlow, edge.capacity))

        if flow == 0 :
            continue

        networkFlowGraph.runFlow(edge, flow)

        return flow

    return 0


class NetworkFlowGraph :
    """ ネットワークフローグラフ

    Attributes:
        graph: (list[list[Edge]]): グラフ
    """

    def __init__(self, vCnt) :
        self.graph = list(list() for _ in range(vCnt))

    def addEdge(self, start, to, capacity) :
        """ 辺を追加します。対応する後進辺も追加します。

        Args:
            start (int): 始点
            to (int): 終点
            capacity (int): 容量
        """
        newEdge = Edge(start, to, capacity)
        newReverseEdge = Edge(to, start, 0)

        newEdge.setReverseEdge(newReverseEdge)
        newReverseEdge.setReverseEdge(newEdge)

        self.graph[newEdge.start].append(newEdge)
        self.graph[newReverseEdge.start].append(newReverseEdge)

    def runFlow(self, edge, flow) :
        """ 辺にフローを流します。対応する後進辺にもフローを流します。

        Args:
            edge (Edge): 辺
            flow (int): フロー
        """
        edge.capacity -= flow
        edge.reverseEdge.capacity += flow


class Edge :
    """ 辺

    Attributes:
        start (int): 始点
        to (int): 終点
        capacity (int): 容量
    """
    start = int()
    to = int()
    capacity = int()

    def __init__(self, start, to, capacity) :
        self.start = start
        self.to = to
        self.capacity = capacity

    def setReverseEdge(self, reverseEdge) :
        """ 対応する後進辺をセットします。

        Args:
            reverseEdge (Edge): 対応する後進辺
        """
        self.reverseEdge = reverseEdge