class Solution:
    def lengthOfMaxWord(self, s: str) -> int:
        count = 0
        sum_str =0

        for i,v in enumerate(s):
            if v != " ":
                count +=1
            if v == " " or i == len(s)-1:
                if count > sum_str:
                    sum_str = count
                count = 0
        return sum_str