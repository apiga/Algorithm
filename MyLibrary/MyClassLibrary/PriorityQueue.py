import collections
import heapq

class PriorityQueue :
    """ 優先度つきキュー

    Attribute :
        len (int): 現在の要素の個数
        queue (list[int]): キュー
        numCount (dict[int, int]): キューに入っている数字とその個数を管理する辞書
        deleteCount (dict[int, int]): 削除状態を記録する辞書
        reverse (bool): 最大値を取り出すかどうか
    """

    def __init__(self, initList = None, reverse = False) :
        self.len = 0
        self.queue = list()
        self.numCount = collections.defaultdict(lambda : int(0))
        self.deleteCount = collections.defaultdict(lambda : int(0))
        self.reverse = reverse
        if initList :
            for num in initList :
                if self.reverse :
                    self.numCount[-num] += 1
                    heapq.heappush(self.queue, -num)
                else :
                    self.numCount[num] += 1
                    heapq.heappush(self.queue, num)
                self.len += 1

    def __len__(self) :
        return self.len

    def remove(self, num) :
        """ キューの要素を削除します。
            計算量 O(log(N))
        Args:
            num (int): 削除したい要素
        """
        if self.reverse :
            if self.numCount[-num] - self.deleteCount[-num] > 0 :
                self.deleteCount[-num] += 1
        else :
            if self.numCount[num] - self.deleteCount[num] > 0:
                self.deleteCount[num] += 1

        self.len -= 1

    def enqueue(self, num) :
        """ キューに要素を追加します。
            計算量 O(log(N))

        Args:
            num (int): 追加したい要素
        """
        if self.reverse :
            self.numCount[-num] += 1
            heapq.heappush(self.queue, -num)
        else :
            self.numCount[num] += 1
            heapq.heappush(self.queue, num)

        self.len += 1

    def dequeue(self) :
        """ キューから最小値（最大値）を取り出します。
            計算量 O(log(N))

        Returns:
            int: 最小値（最大値）
        """
        if self.len == 0 :
            return "empty"

        self.refresh()

        self.numCount[self.queue[0]] -= 1
        if self.reverse :
            self.len -= 1
            return -heapq.heappop(self.queue)
        else :
            self.len -= 1
            return heapq.heappop(self.queue)

    def getHead(self) :
        """ キューの最小値（最大値）を取得します。
            計算量 O(1)

        Returns:
            int: 最小値（最大値）
        """
        if self.len == 0 :
            return "empty"

        self.refresh()

        if self.reverse :
            return -self.queue[0]
        else :
            return self.queue[0]

    def refresh(self) :
        """ 削除状態を反映します。
        """
        while True :
            if self.deleteCount[self.queue[0]] > 0 :
                self.deleteCount[self.queue[0]] -= 1
                self.numCount[self.queue[0]] -= 1
                heapq.heappop(self.queue)
            else :
                return