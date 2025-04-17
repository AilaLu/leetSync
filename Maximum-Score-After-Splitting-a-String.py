class Solution:
    #calculate all the ones in the s.
    #iterate through the s, count the zeros on the left, and update the max score.
    def maxScore(self, s: str) -> int:
        one_count = 0
        zero_count = 0
        max_score = one_count


        for num in s:
            if num == "1": one_count += 1

        for i in range(len(s)-1): 
            if s[i] == "0": zero_count += 1
            elif s[i] == "1": one_count -= 1
            max_score = max(max_score, one_count+zero_count)


        return  max_score
        