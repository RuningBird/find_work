class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    思路：a^n % b
    (a * b) % p = ((a%p) * (b%p))
    (a * b)^ n % b = 
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 1:
            return a
        if n == 0:
            return a**0 % b
        tmp = self.fastPower(a,b,n//2)
        res = 1
        if n % 2 == 0:
            return ((tmp % b) * (tmp % b) ) % b
        else:
            return (  ( (tmp % b) * (tmp % b) ) * (a % b)  ) % b