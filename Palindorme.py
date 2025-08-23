"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        nxt_num = x
        current = x
        divisor = 1
        if x < 0:
            return False

        while True:
        	if int(num)<=0:
        		break
 
        	num/=10
        	divisor*=10
        divisor/=10
        l = list()
        while True:
        	if int(divisor) < 1:	
        		break
        	nxt_num = current % divisor  
        	l.append(int(current/divisor))
        	divisor/=10
        	current = nxt_num

        flag=True
        len_l = len(l)  
        for i in range(len_l//2):
        	if l[i] == l[len_l-i-1]:
        		print(l[i], l[len_l-i-1], 'match')
        	else:
        		flag=False
        		break

        return bool(flag)
        