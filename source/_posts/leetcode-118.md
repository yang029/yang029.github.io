---
title: 118. Pascal's Triangle
date: 2021-07-06 16:48:34
tags: dynamic programmming
catagories: leetcode 
---
<br>
<!--more -->

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

 

**Example 1:**

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Example 2:**

```
Input: numRows = 1
Output: [[1]]
```

 

**Constraints:**

- `1 <= numRows <= 30`

## solution
a very very simple DP problem for beginners. We can easily observe from the graph to find that `dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]`, with **the initial conditions** that `dp[0][0] = 1` and `dp[i][i] = dp[i][0] = 1` and therefore solve the problem

## code
```java
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(Arrays.asList(1));
        for(int i = 1; i < numRows; i++) {
            List<Integer> list = new ArrayList<>();
            list.add(1);
            for(int j = 1; j < i; j++) {
                list.add(ans.get(i -1).get(j - 1)+ ans.get(i -1).get(j));
            }
            list.add(1);
            ans.add(list);
        }

        return ans;
    }
}
```