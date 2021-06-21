def circle_area(r):
    return 3.14 * (r ** 2)


def fizzbuzz(n):

    sum = 0
    i = 0

    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            sum += i * 2
        elif i % 5 == 0 or i % 7 == 0:
            None
        else:
            sum += i

    return sum


def count_in_str(pattern, str):
    """counts the number of times the pattern appears in the string
        count_in_str("a", "abcaabc") returns 3
        count_in_str("ab", "abcaabc") return 2"""

    c = 0
    l = len(pattern)
    while len(str) >= l:
        sl = str[:l]
        if pattern == sl:
            c += 1
        str = str[1:]
    return c


def flip_ends(str):
    if str == "" or len(str) == 1:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]


def is_prime(x):

    if x == 0 or x == 1:
        return False

    x = True
    for i in (2, x):
        while x:
            if x % i == 0:
                x = False
        if not x:
            break
    return x


def sum_primes(n):
    "this function computes the sum of all primes up to N, not including N"
    sum = 0
    while n >= 2:
        if is_prime(n):
            sum += n
        n -= 1
    return sum


# start tests
def test_circle_area():
    assert (circle_area(1) == 3.14)
    assert (circle_area(0) == 0)
    assert (circle_area(10) == 314)


def test_fizzbuzz():
    assert (fizzbuzz(1) == 1)
    assert (fizzbuzz(8) == 1 + 2 + 3 + 4 + 6 + 8)  # 5 and 7 are skipped
    assert (fizzbuzz(35) == 490)


def test_count_in_str():
    assert (count_in_str("a", "abcaabc") == 3)
    assert (count_in_str("ab", "abcaabc") == 2)
    assert (count_in_str("abx", "abx") == 1)
    assert (count_in_str("abx", "ab") == 0)


def test_flip_ends():
    assert (flip_ends("") == "")
    assert (flip_ends("a") == "a")
    assert (flip_ends("ab") == "ba")
    assert (flip_ends("abc") == "cba")


def test_is_prime():
    assert (is_prime(1) == False)
    assert (is_prime(2) == True)
    assert (is_prime(3) == True)
    assert (is_prime(5) == True)
    assert (is_prime(9) == False)
    assert (is_prime(14) == False)
    assert (is_prime(17) == True)


def test_sum_primes():
    assert (sum_primes(5) == 5)
    assert (sum_primes(10) == 17)


if __name__ == "__main__":

    test_circle_area()
    test_fizzbuzz()
    test_count_in_str()
    test_flip_ends()
    test_is_prime()
    test_sum_primes()
