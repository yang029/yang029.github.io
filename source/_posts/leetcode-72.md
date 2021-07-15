---
title: 72. Edit Distance
tags:
  - leetcode
  - dynamic programming
date: 2021-07-05 16:43:24
catagories: leetcode
---


Given two strings `word1` and `word2`, return *the minimum number of operations required to convert `word1` to `word2`*.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

 

**Example 1:**

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

**Example 2:**

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

 

**Constraints:**

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## solution
simple DP problem. We can construct a DP array dp[i][j] indicating the steps it takes to transform `word1[0 ~ i]` to `word2[0 ~ j]`, then `dp[word1.length()][word2.length()]` should be the answer. 

**Then what about DP function?** 
- Obviously, if `word1[i] == word2[j]`, then `dp[i][j] = dp[i - 1][j - 1]`
- Otherwise, we need to consider the following transformations: 
  - remove one character to word1 --> `bbc bb` to `bb bb`, which means `1 + dp[i - 1][j]`
  - add one character to word1 (so we only need to consider `word1[0 ~ i]` -> `word2[0 ~ j-1]`. i.e. `bb bbc` to `bbc bbc`, which is `1 + dp[i][j - 1]`
  - replace one character in word1, so we only need to compare `word1[0 ~ i-1]` -> `word2[0 ~ j-1]`, i.e. `bbd bbc` to `bbc bbc`, which is `1 + dp[i - 1][j - 1]`  
  
  So, to sum up, ` dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i][j - 1], dp[i - 1][j]))`  
- As for initialization, it must take n steps to transfrom a length 0 word to a length n word, so `dp[i][0] = i` `dp[0][j] = j`
### Perconditions

- the order of the operations does not matter (no relations among manipulations)
  
### Code
``` Java
class Solution {
    public int minDistance(String word1, String word2) {
        if(word1.length() == 0) {
            return word2.length();
        }
        
        if(word2.length() == 0) {
            return word1.length();
        }
        int[][] dp = new int[word1.length() + 1][word2.length() + 1];
        for(int i = 0; i < dp.length; i++) {
            dp[i][0] = i;
        }
        
        for(int j = 0; j < dp[0].length; j++) {
            dp[0][j] = j;
        }
        
        for(int i = 1; i < dp.length; i++) {
            for(int j = 1; j < dp[0].length; j++) {
                if(word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i][j - 1], dp[i - 1][j]));
                }
                
                
                
            }
        }
        
        return dp[dp.length - 1][dp[0].length - 1];
    }
}
```
