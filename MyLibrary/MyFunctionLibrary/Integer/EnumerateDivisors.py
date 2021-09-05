import math

def enumerateDivisors(num) :
    """ 約数を列挙します。
        計算量 O(√N)

    Args:
        num (int): 整数

    Returns:
        list[int]): 約数のリスト
    """

    divisors = list()

    for i in range(1, math.floor(math.sqrt(num)) + 1) :
        if num % i == 0 :
            divisors.append(i)

            if num // i != i :
                divisors.append(num // i)

    return sorted(divisors)