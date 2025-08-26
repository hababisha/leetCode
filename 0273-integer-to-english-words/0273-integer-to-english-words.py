class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0 :
            return "Zero"
        
        number_words = {    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
                            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
                            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
                            19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
                            50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety" }

        scale_words = {  1:"Thousand", 2:"Million", 3:"Billion" }

        def thousands(n):
            answer = []
            while n:
                if n >= 100:
                    t = n//100
                    answer.append(number_words[t])
                    answer.append("Hundred")
                    n = n % 100
                elif n >= 20:
                    t = (n//10) * 10
                    answer.append(number_words[t])
                    n = n % 10
                elif n > 0:
                    answer.append(number_words[n])
                    break
            
            return " ".join(answer)
        
        res = []
        while num:
            cur = num % 1000
            res.append(thousands(cur))
            num = num // 1000
        
        final = ""
        for i in reversed(range(1, len(res))):
            if res[i]:
                s = res[i] + " " + scale_words[i] + " " 
                final += s
        
        final += res[0]

        return final.strip()
        
