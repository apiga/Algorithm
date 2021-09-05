import math

def eratosthenesSieve(num) :
    """ エラトステネスの篩で素数を列挙します。
        計算量 O(Nlog(log(N)))

    Args:
        num(int): 整数

    Returns:
        list[bool]: 素数かどうかのリスト
    """

    isPrime = list(True for _ in range(num + 1))
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, math.floor(math.sqrt(num)) + 1) :
        if isPrime[i] :
            for j in range(i * 2, num + 1, i) :
                isPrime[j] = False

    return isPrime



