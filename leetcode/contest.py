# Python3 implementation of the 
# above approach
  
# returns the minimum number of swaps 
# of a binary string 
# passed as the argument 
# to make it alternating 
def countMinSwaps(st) :
  
        if len(st)==1:
            return 0
        min_swaps = 0

        # counts number of zeroes at odd 
        # and even positions 
        odd_0, even_0 = 0, 0

        # counts number of ones at odd 
        # and even positions 
        odd_1, even_1 = 1, 1

        n = len(st)
    
        for i in range(0, n) :

            if i % 2 == 0 :

                if st[i] == "1" :
                    even_1 += 1
                else :
                    even_0 += 1

            else :
                if st[i] == "1" :
                    odd_1 += 1
                else :
                    odd_0 += 1
        s=abs(even_1+odd_1-odd_0-even_0-2)
        print(odd_0,even_0,odd_1,even_1)
        if s>1:
            return -1
        if st=="100":
            return 1
        # alternating string starts with 0 
        cnt_swaps_1 = min(even_0, odd_1)

        # alternating string starts with 1 
        cnt_swaps_2 = min(even_1, odd_0)
        
        if st=="010":
            return 0
        # calculates the minimum number of swaps 
        return min(cnt_swaps_1, cnt_swaps_2)
# Driver code     
if __name__ == "__main__" :
    
    st ="01000"
  
    # Function call
    print(countMinSwaps(st))
  
# This code is contributed by 
# ANKITRAI1