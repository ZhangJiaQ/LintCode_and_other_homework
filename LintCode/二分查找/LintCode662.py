Guess Number Game 
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

样例
n = 10, I pick 4 (but you don't know)
Return 4. Correct !

解题思路：二分法

class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        low = 0
        high = n
        while low < high:
            mid = (low+high) // 2
            if Guess.guess(mid) == 0:
                return mid
            if Guess.guess(mid) == -1:
                high = mid - 1
            if Guess.guess(mid) == 1:
                low = mid + 1
                
        if Guess.guess(high) == 0:
            return high