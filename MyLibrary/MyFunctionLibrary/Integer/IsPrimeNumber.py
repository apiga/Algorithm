import math

def isPrimeNumber(num) :
    """ 素数かどうかを判定します。
        計算量 O(√N)

    Args:
        num (int): 整数

    Returns:
        bool: 素数かどうか
    """
    if num == 1 :
        return False

    for i in range(2, math.floor(math.sqrt(num)) + 1) :
        if num % i == 0 :
            return False

    return True