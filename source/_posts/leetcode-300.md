---
title: 300. Longest Increasing Subsequence
date: 2021-07-15 17:22:52
tags: dynamic programming
catagories: leetcode
---

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

<!--more -->

A **subsequence** is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`.

 

**Example 1:**

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Example 2:**

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3:**

```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

 

**Constraints:**

- `1 <= nums.length <= 2500`
- `-104 <= nums[i] <= 104`

 

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## solution 
This question is kind of hard and bothered me for days. As first, I try to solve it with memoization and DFS, which just use a DP array `dp[i][j]`, to note down the longest subsequence at ith element of the array with the maximun value of j. It seems to have a complexity of O(n^2), but finally MLE and cause stack overflow.


```Java
class Solution {
    int dp[][];
    int min = -10001;
    int delta = 10001;
    int num[];
    public int lengthOfLIS(int[] nums) {
        dp = new int[nums.length][30000];
        num = nums;
        for(int[] d : dp) {
            Arrays.fill(d, -1);
        }
        
        return dfs(0, min);
    }

    private int dfs(int curr, int currMax) {
        if(curr >= num.length) return 0;
        if(dp[curr][currMax + delta] != -1) return dp[curr][currMax + delta];
        if(num[curr] <= currMax) {
            return dp[curr][currMax + delta] = dfs(curr + 1, currMax);
        } else {
            return dp[curr][currMax + delta] = Math.max(dfs(curr + 1, currMax), dfs(curr + 1, num[curr]) + 1);
        }
    }
}

```  


Then I tried to solve it directly by dynamic programming. I found that it is sufficient to use only one dimension array `dp[i]`, to indicate the maximum length of the subsequence with max value i. Also, for an element `nums[i]`, it will only influence the `dp[i]` that `i > nums[i]`. And this state comes from the maximum of the states `dp[i]` that `i < nums[i]`. Therefore, I come out the DP function that `dp[nums[i]] = max(dp[0 ~ nums[i-1]]) + 1`. This has a complexity of `O(n * m)`, where n is the length of the array, and m is the range of the value. If we use better data structure to `findMax`, the complexity can be reduced to `O(nlogm)`.


``` Java
class Solution {
    int dp[];
    int min = Integer.MIN_VALUE;
    int delta = 10000;
    int range = 20003;
    public int lengthOfLIS(int[] nums) {
        dp = new int[range];
        for(int i = 0; i < nums.length; i++) {
            dp[nums[i] + delta] = findMax(nums[i] + delta) + 1;
        }
        return findMax(range);
    }

    private int findMax(int upper) {
        int max = min;
        for(int i = 0; i < upper; i++) {
            max = Math.max(dp[i], max);
        }
        return max;
    }
    
}
```

However, the best solution does not depend on the range of the input. This is in fact can be solved by greedy. We need to maintain an increasing subsequence. When we meet an new element, we consider to use it to subsitute one of the element in our current subsequence to make it longer. 

The normal `O(n^2)` solution is like this
```Java
    class Solution {
        public int lengthOfLIS(int[] nums) {
            int []dp=new int[nums.length];
            Arrays.fill(dp,1);
            for(int i=1;i<nums.length;i++){
                for(int j=0;j<i;j++){
                    if(nums[j]<nums[i]){
                        dp[i]=Math.max(dp[i],dp[j]+1);
                    }
                }
            }
            int max=0;
            for(int i=0;i<dp.length;i++){
                max=Math.max(max,dp[i]);
            }
            return max;
        }
    }
```

`O(nlog(n))` code 
```Java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int size = 0;
        for(int i = 0; i < nums.length; i++) {
            int index = Arrays.binarySearch(dp,0, size, nums[i]); 
            if(index < 0) {
                index = -index - 1;
            } 
            if(index == size) {
                size++;
            }
            dp[index] = nums[i];
            
        }
        return size;
    }
}

```
