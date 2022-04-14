class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = len(a) if len(a) >= len(b) else len(b)
        i=1
        save=0
        result ='' 
        while i <= max_len or save >0:
            item_a = a[-i] if i <= len(a) else 0
            item_b = b[-i] if i <= len(b)  else 0
            total = int(item_a) + int(item_b) + int(save)
            save=0
            if total == 0:
                result = '0' + result
            elif total == 1:
                result = '1'  + result
            elif total == 2:
                result = '0'  + result
                save=1
            elif total == 3:
                result = '1'  + result
                save=1
            i +=1
        return result
        
        