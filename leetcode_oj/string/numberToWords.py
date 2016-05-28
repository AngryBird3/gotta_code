'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Hint:

Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.Show More Hint 
Hide Company Tags Microsoft Facebook
Hide Tags Math String
Hide Similar Problems (M) Integer to Roman
Difficulty: Hard
'''
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"
        places = ["", "Thousand", "Million", "Billion"]
        p = 0
        num_to_words = ""
        while num:
            if num % 1000:
                w = self.three(num % 1000)
                num_to_words = w + places[p] + " " + num_to_words
            num /= 1000
            p += 1
        
        return num_to_words.strip()
        
    def three(self, num, s=""):
        twenty = {  1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
                    8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
                    14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
                    19: "Nineteen"}
        tens = { 1: "One", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty",
                     9: "Ninety" }
        if not num:
            return ""
        elif num < 20:
            return twenty[num] + " "
        elif num < 100:
            return tens[num/10] + " " + self.three(num%10)
        else:
            return twenty[num/100] + " Hundred " + self.three(num % 100)
