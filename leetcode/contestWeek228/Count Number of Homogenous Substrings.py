class Solution:
    def countHomogenous(self, s: str) -> int:
        # Size of the string 
        n = len(s) 

        # Initialize count to 1 
        count = 1
        result = 0

        # Initialize left to 0 and right to 1 
        # to traverse the string 
        left = 0
        right = 1

        while (right < n): 

            # Checking if consecutive 
            # characters are same and 
            # increment the count 
            if (s[left] == s[right]): 
                count += 1

            # When we encounter a 
            # different characters 
            else: 

                # Increment the result 
                result += count * (count + 1) // 2

                # To repeat the whole 
                # process set left equals 
                # right and count variable to 1 
                left = right 
                count = 1

            right += 1
        mode=10**9+7
        # Store the final value of result 
        result += count * (count + 1) // 2
        return result%mode