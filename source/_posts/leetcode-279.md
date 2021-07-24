---
title: leetcode-279
date: 2021-07-19 16:39:34
tags: dynamic programming
catagories: leetcode
---

## perfect square numbers

<!--more -->


Given an integer `n`, return *the least number of perfect square numbers that sum to* `n`.

A **perfect square** is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, `1`, `4`, `9`, and `16` are perfect squares while `3` and `11` are not.

 

**Example 1:**

```
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
```

**Example 2:**

```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

 

**Constraints:**

- `1 <= n <= 10000`

## Solution

This can be solved in multiple ways:

1. dynamic programming 
  > dp[i] = Math.max(dp[i], dp[i - j * j] + 1)
2. DFS with memorization
```Java
  class Solution {
    int[] dp;
    public int numSquares(int n) {
        dp = new int[n + 1];
        return dfs(n);
    }

    private int dfs(int n) {
        if(dp[n] != 0) return dp[n];
        int val = (int) Math.sqrt(n);
        if(val * val == n) {
            return dp[n] = 1;
        } else {
            int min = 1000;
            for(int i = val; i > 0; i--) {
                min = Math.min(min, dfs(n - i * i));
            }
            return dp[n] = min + 1;
        }
    }
}
```
3. BFS
    > This can be consider as a shortest-path problem. The nodes are square numbers and we need to find the minimun path of which sum is `n`. 
