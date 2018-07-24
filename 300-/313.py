# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.
#
# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# (4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        ugly = [0]*n
        ugly[0] = 1
        k = len(primes)
        ugly_index = [0] * k
        ugly_temp = [1] * k
        idx = 1
        while idx < n:
            for x in range(k):
                ugly_temp[x] = ugly[ugly_index[x]] * primes[x]
            nint = min(ugly_temp)
            ugly[idx] = nint
            for x in range(k):
                if ugly[ugly_index[x]] * primes[x] == ugly[idx]:
                    ugly_index[x] += 1
            idx += 1
        return ugly[idx - 1]


s = Solution()
print(s.nthSuperUglyNumber(10, [2, 3, 5]))
