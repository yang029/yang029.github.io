---
title: Weekly Contest 206
date: 2020-09-13 13:18:53
tags:
   - Leetcode Weekly contest
catagories: 
    - Leetcode
---

### 1582. Special Positions in a Binary Matrix

Given a `rows x cols` matrix `mat`, where `mat[i][j]` is either `0` or `1`, return *the number of special positions in `mat`.*

A position `(i,j)` is called **special** if `mat[i][j] == 1` and all other elements in row `i` and column `j` are `0` (rows and columns are **0-indexed**).

 

**Example 1:**

```
Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
```

**Example 2:**

```
Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0,0), (1,1) and (2,2) are special positions. 
```

**Example 3:**

```
Input: mat = [[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]
Output: 2
```

**Example 4:**

```
Input: mat = [[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]]
Output: 3
```

 

**Constraints:**

- `rows == mat.length`
- `cols == mat[i].length`
- `1 <= rows, cols <= 100`
- `mat[i][j]` is `0` or `1`.

### 思路及代码

- 存下和为一（即只有1个1） 的行数
- 存下和为一的列数
- 遍历这些行和列，判断他们的交点是否为1，记录个数

```java
class Solution {
    public int numSpecial(int[][] mat) {
        int ans = 0;
        List<Integer> row = new ArrayList<>();
        List<Integer> col = new ArrayList<>();
        for(int i = 0; i < mat.length; i++) {
            int sum = 0;
            for(int num : mat[i]) {
                sum += num;
            }
            if(sum == 1) {
                row.add(i);
            }
        }
        for(int i = 0; i < mat[0].length; i++) {
            int sum = 0;
            for(int j = 0; j < mat.length; j++) {
                sum += mat[j][i];
            }
            if(sum == 1) {
                col.add(i);
            }
        }
        for(int r : row) {
            for(int c : col) {
                if(mat[r][c] == 1) 
                    ans++;
            }
        }
        return ans;
    }
}
```

### 1583. Count Unhappy Friends

You are given a list of `preferences` for `n` friends, where `n` is always **even**.

For each person `i`, `preferences[i]` contains a list of friends **sorted** in the **order of preference**. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from `0` to `n-1`.

All the friends are divided into pairs. The pairings are given in a list `pairs`, where `pairs[i] = [xi, yi]` denotes `xi` is paired with `yi` and `yi` is paired with `xi`.

However, this pairing may cause some of the friends to be unhappy. A friend `x` is unhappy if `x` is paired with `y` and there exists a friend `u` who is paired with `v` but:

- `x` prefers `u` over `y`, and
- `u` prefers `x` over `v`.

Return *the number of unhappy friends*.


**Example 1:**

```
Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
Output: 2
Explanation:
Friend 1 is unhappy because:
- 1 is paired with 0 but prefers 3 over 0, and
- 3 prefers 1 over 2.
Friend 3 is unhappy because:
- 3 is paired with 2 but prefers 1 over 2, and
- 1 prefers 3 over 0.
Friends 0 and 2 are happy.
```

**Example 2:**

```
Input: n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
Output: 0
Explanation: Both friends 0 and 1 are happy.
```

**Example 3:**

```
Input: n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
Output: 4
```

**Constraints:**

- `2 <= n <= 500`
- `n` is even.
- `preferences.length == n`
- `preferences[i].length == n - 1`
- `0 <= preferences[i][j] <= n - 1`
- `preferences[i]` does not contain `i`.
- All values in `preferences[i]` are unique.
- `pairs.length == n/2`
- `pairs[i].length == 2`
- `xi != yi`
- `0 <= xi, yi <= n - 1`
- Each person is contained in **exactly one** pair.

### 思路及代码

普通的模拟，用了map方便查找对应的pairs

```java
class Solution {
    public int unhappyFriends(int n, int[][] perferences, int[][] pairs) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int[] p : pairs) {
            map.put(p[0], p[1]);
            map.put(p[1], p[0]);
        }
        int ans = 0;
        for(int i = 0; i < n; i++) {
            int k = find(perferences[i], map.get(i));
            for(int j = k - 1; j >= 0; j--) {
                int num = perferences[i][j];
                if(find(perferences[num], map.get(num)) > find(perferences[num], i)) {
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }

    private int find(int[] nums, int num) {
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == num) return i;
        }
        return -1;
    }
}
```

### 1584. Min Cost to Connect All Points

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **Manhattan distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return *the minimum cost to make all points connected.* All points are connected if there is **exactly one** simple path between any two points.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/08/26/d.png)

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

**Example 2:**

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

**Example 3:**

```
Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4
```

**Example 4:**

```
Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000
```

**Example 5:**

```
Input: points = [[0,0]]
Output: 0
```


**Constraints:**

- `1 <= points.length <= 1000`
- `-106 <= xi, yi <= 106`
- All pairs `(xi, yi)` are distinct.

### 思路及代码

裸最小生成树(MST)， 敲了个prim复杂度`O(n^2)`上去就AC了， kruskal`O(n^2logn)`好像也能过

```java
class Solution {
    public int minCostConnectPoints(int[][] points) {
        if(points.length == 1) return 0;
        int[][] dist = new int[points.length][points.length];
        for(int i = 0; i < points.length; i++) {
            for(int j = 0; j < points.length; j++) {
                int dis = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                dist[i][j] = dis;
                dist[j][i] = dis;
            }
        }

        int[] dis = new int[points.length];
        Arrays.fill(dis, Integer.MAX_VALUE);
        dis[0] = 0;
        Set<Integer> set = new HashSet<>();
        int ans = 0;
        for(int a = 0; a < points.length; a++) {
            int cur = -1; 
            int mx = Integer.MAX_VALUE;
            for(int i = 0; i < points.length; i++) {
                if(!set.contains(i) && dis[i] < mx) {
                    cur = i;
                    mx = dis[i];
                }
            }
            set.add(cur);
            for(int i = 0; i < points.length; i++) {
                if(set.contains(i)) continue;
                if(dis[i] > dist[cur][i])
                    dis[i] = dist[cur][i];
            }
        }
        for(int num : dis) {
            ans += num;
        }
        return ans;
    }
}
```

### 5514. Check If String Is Transformable With Substring Sort Operations

Given two strings `s` and `t`, you want to transform string `s` into string `t` using the following operation any number of times:

- Choose a **non-empty** substring in `s` and sort it in-place so the characters are in **ascending order**.

For example, applying the operation on the underlined substring in `"14234"` results in `"12344"`.

Return `true` if *it is possible to transform string `s` into string `t`*. Otherwise, return `false`.

A **substring** is a contiguous sequence of characters within a string.


**Example 1:**

```
Input: s = "84532", t = "34852"
Output: true
Explanation: You can transform s into t using the following sort operations:
"84532" (from index 2 to 3) -> "84352"
"84352" (from index 0 to 2) -> "34852"
```

**Example 2:**

```
Input: s = "34521", t = "23415"
Output: true
Explanation: You can transform s into t using the following sort operations:
"34521" -> "23451"
"23451" -> "23415"
```

**Example 3:**

```
Input: s = "12345", t = "12435"
Output: false
```

**Example 4:**

```
Input: s = "1", t = "2"
Output: false
```

**Constraints:**

- `s.length == t.length`
- `1 <= s.length <= 105`
- `s` and `t` only contain digits from `'0'` to `'9'`.

