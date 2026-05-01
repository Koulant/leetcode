class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Need a way to check if str in same fwd to bkwd and bkwd to fwd
        # Two pointer approach
        # One pointer at start
        # One pointer at end
        # while left is less than right
        # move left forward, while l < r until it sees an alphanumic char
        # move right backward until alphanumeric char
        # compare chars at l and r indicies
        # if they are equal, continue moving l and r
        # if they are not equal, return false
        l = 0
        r = len(s) - 1 # remember to do -1 when using it as a last index

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            # Finally we have a l and r index that is alphanumeric
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1 # Go to next char to try again
        return True


            


        

            
