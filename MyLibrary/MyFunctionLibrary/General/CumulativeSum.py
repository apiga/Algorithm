def createCumulativeSum(originList):
    """ 累積和の配列を作成します。
        計算量 O(N)

    Args:
        originList (list[int]): 累積和を作りたい配列

    Returns:
        list[int]: 累積和の配列
    """
    cumulativeSumList = list()

    cumulativeSumList.append(0)

    for i in range(len(originList)):
        cumulativeSumList.append(cumulativeSumList[-1] + originList[i])

    return cumulativeSumList