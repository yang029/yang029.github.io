---
title: 403. Frog Jump
date: 2021-07-07 17:20:14
tags: dynamic programming
catagories: leetcode
---

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of `stones`' positions (in units) in sorted **ascending order**, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be `1` unit.

If the frog's last jump was `k` units, its next jump must be either `k - 1`, `k`, or `k + 1` units. The frog can only jump in the forward direction.

 

**Example 1:**

```
Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
```

**Example 2:**

```
Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
```

 

**Constraints:**

- `2 <= stones.length <= 2000`
- `0 <= stones[i] <= 231 - 1`
- `stones[0] == 0`

## solution

This question does not worth a **Hard** tag. My thought is quite simple. First, we have an array of sets called `dp[]` to store all possible steps that can reach stone i. We then tranverse through the array of `stones`. For every stone i tranversed through, we can find all other stones that can be reached from stone i and update the `dp` array. Finally, we check if `dp[stones.length - 1]` is reached and return hthe answer.

So in my first version of answer, I write this answer. It tranverse through the stones array and then find if any element in the stones array can be reached from current position. This version is in `O(n^3)` time complexity, which definitely leads to a TLE.
``` Java
class Solution {
    public boolean canCross(int[] stones) {
        Set<Integer> dp[] = new HashSet[stones.length];
        for(int i = 0; i < dp.length; i++) {
            dp[i] = new HashSet<>();
        }
        if(stones[1] != 1) {
            return false;
        }
        dp[1].add(1);
        for(int i = 1; i < stones.length; i++) {
            for(int j = i + 1; j < stones.length; j++) {
                for(int val : dp[i]) {
                    if(val + stones[i] == stones[j]) {
                        dp[j].add(val);
                    } else if(val + stones[i] + 1 == stones[j]) {
                        dp[j].add(val + 1);
                    } else if(val + stones[i] - 1 == stones[j]) {
                        dp[j].add(val - 1);
                    }
                }
            }
        }
        return !dp[stones.length - 1].isEmpty();
    }
}
```
so I update my code a bit to a O(n^2) solution, which utilizes a HashMap to check if a stone can be reached from current position and passed all tests. I also noticed the existence of the DFS solution.  Since DFS does not need to calculate every possible condition, it may lead to a shorter runtime.  

```Java
class Solution {
    public boolean canCross(int[] stones) {
        Set<Integer> dp[] = new HashSet[stones.length];
        for(int i = 0; i < dp.length; i++) {
            dp[i] = new HashSet<>();
        }
        if(stones[1] != 1) {
            return false;
        }
        dp[1].add(1);
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 1; i < stones.length; i++) {
            map.put(stones[i], i);
        }

        for(int i = 1; i < stones.length; i++) {
            for (int val : dp[i]) {
                if (map.containsKey(val + stones[i])) {
                    dp[map.get(val + stones[i])].add(val);
                }
                if (map.containsKey(val + stones[i] + 1)) {
                    dp[map.get(val + stones[i] + 1)].add(val + 1);
                }
                if (map.containsKey(val + stones[i] - 1) && map.get(val + stones[i] - 1) > i) {
                    dp[map.get(val + stones[i] - 1)].add(val - 1);
                }
            }
        }
        return !dp[stones.length - 1].isEmpty();
    }
}
```