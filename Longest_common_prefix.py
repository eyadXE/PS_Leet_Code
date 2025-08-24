"""


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.



"""







class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s_first = strs[0]
        longest_str = ""
        iter = 0
        flag = 0
        for i in s_first:
            j = 1
            while j < len(strs):
            
                #print(strs[j] + " " + i + " " + str(iter))
                tmp = strs[j]
                if len(tmp)-1 <iter or tmp[iter] != i:
                    flag=1
                    break
                j += 1
            if flag == 0:
                longest_str += i
                print(longest_str)
            else:
                break

            iter += 1
        return longest_str
        #print("My answer is: " + longest_str)
