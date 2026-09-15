# Week 2 Coding Problem Statements

Week 2 focuses on two pointers and sliding window problems.

Use this file to understand each problem before implementing it in both Python
and C++.

Do not write solutions in this file.

## Week 2 problem list

| # | Problem | Difficulty | Pattern |
| ---: | --- | --- | --- |
| 10 | Valid Palindrome | Easy | Two pointers |
| 11 | Two Sum II - Input Array Is Sorted | Medium | Two pointers |
| 12 | 3Sum | Medium | Sort + two pointers |
| 13 | Container With Most Water | Medium | Two pointers |
| 14 | Squares of a Sorted Array | Easy | Two pointers |
| 15 | Best Time to Buy and Sell Stock | Easy | Sliding window |
| 16 | Longest Substring Without Repeating Characters | Medium | Sliding window |
| 17 | Permutation in String | Medium | Sliding window |

## 10. Valid Palindrome

Source:

- LeetCode: https://leetcode.com/problems/valid-palindrome/

Difficulty: Easy

Pattern: two pointers

### Problem

Given a string, determine whether it is a palindrome after ignoring all
non-alphanumeric characters and ignoring case.

A palindrome reads the same forward and backward after this normalization.

### Input

```text
s: string
```

### Output

```text
boolean
```

### Example 1

Input:

```text
s = "A man, a plan, a canal: Panama"
```

Output:

```text
true
```

Explanation:

```text
After normalization, the string is "amanaplanacanalpanama".
This reads the same forward and backward.
```

### Example 2

Input:

```text
s = "race a car"
```

Output:

```text
false
```

### Example 3

Input:

```text
s = " "
```

Output:

```text
true
```

### Constraints

```text
the string may contain letters, digits, spaces, and punctuation
comparison is case-insensitive
non-alphanumeric characters are ignored
```

## 11. Two Sum II - Input Array Is Sorted

Source:

- LeetCode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Difficulty: Medium

Pattern: two pointers

### Problem

Given a sorted array of integers and a target value, return the 1-based indices
of two numbers whose sum equals the target.

The input array is sorted in non-decreasing order.

Assume exactly one valid pair exists.

The same element cannot be used twice.

### Input

```text
numbers: sorted list of integers
target: integer
```

### Output

```text
list of two 1-based indices
```

### Example 1

Input:

```text
numbers = [2, 7, 11, 15]
target = 9
```

Output:

```text
[1, 2]
```

### Example 2

Input:

```text
numbers = [2, 3, 4]
target = 6
```

Output:

```text
[1, 3]
```

### Example 3

Input:

```text
numbers = [-1, 0]
target = -1
```

Output:

```text
[1, 2]
```

### Constraints

```text
2 <= len(numbers)
numbers is sorted in non-decreasing order
exactly one valid answer exists
return 1-based indices
```

## 12. 3Sum

Source:

- LeetCode: https://leetcode.com/problems/3sum/

Difficulty: Medium

Pattern: sorting + two pointers

### Problem

Given an integer array, return all unique triplets whose values sum to zero.

Each triplet should contain three different array positions.

The output must not contain duplicate triplets.

The order of triplets does not matter.

The order of values inside a triplet does not matter.

### Input

```text
nums: list of integers
```

### Output

```text
list of integer triplets
```

### Example 1

Input:

```text
nums = [-1, 0, 1, 2, -1, -4]
```

One valid output:

```text
[[-1, -1, 2], [-1, 0, 1]]
```

### Example 2

Input:

```text
nums = [0, 1, 1]
```

Output:

```text
[]
```

### Example 3

Input:

```text
nums = [0, 0, 0]
```

Output:

```text
[[0, 0, 0]]
```

### Constraints

```text
triplets must use three distinct indices
duplicate triplets must be removed
array may contain positive, negative, and zero values
```

## 13. Container With Most Water

Source:

- LeetCode: https://leetcode.com/problems/container-with-most-water/

Difficulty: Medium

Pattern: two pointers

### Problem

You are given an array of non-negative integers where each value represents the
height of a vertical line.

Choose two lines so that, together with the x-axis, they form a container.

Return the maximum amount of water the container can hold.

The width is the distance between the two chosen indices.

The height of the container is limited by the shorter of the two lines.

### Input

```text
height: list of non-negative integers
```

### Output

```text
integer
```

### Example 1

Input:

```text
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```

Output:

```text
49
```

### Example 2

Input:

```text
height = [1, 1]
```

Output:

```text
1
```

### Constraints

```text
2 <= len(height)
heights are non-negative
choose exactly two different indices
```

## 14. Squares of a Sorted Array

Source:

- LeetCode: https://leetcode.com/problems/squares-of-a-sorted-array/

Difficulty: Easy

Pattern: two pointers

### Problem

Given a sorted integer array, return a new array containing the squares of each
number, also sorted in non-decreasing order.

The input may contain negative numbers, so the largest square may come from
either end of the array.

### Input

```text
nums: sorted list of integers
```

### Output

```text
sorted list of squared integers
```

### Example 1

Input:

```text
nums = [-4, -1, 0, 3, 10]
```

Output:

```text
[0, 1, 9, 16, 100]
```

### Example 2

Input:

```text
nums = [-7, -3, 2, 3, 11]
```

Output:

```text
[4, 9, 9, 49, 121]
```

### Constraints

```text
nums is sorted in non-decreasing order
nums may contain negative, zero, and positive values
return a new sorted array
```

## 15. Best Time to Buy and Sell Stock

Source:

- LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Difficulty: Easy

Pattern: sliding window / running minimum

### Problem

Given a list of daily stock prices, choose one day to buy and a later day to
sell.

Return the maximum profit possible.

If no profitable transaction is possible, return zero.

You may complete at most one buy and one sell transaction.

### Input

```text
prices: list of integers
```

### Output

```text
integer
```

### Example 1

Input:

```text
prices = [7, 1, 5, 3, 6, 4]
```

Output:

```text
5
```

Explanation:

```text
Buy at price 1 and sell later at price 6.
```

### Example 2

Input:

```text
prices = [7, 6, 4, 3, 1]
```

Output:

```text
0
```

### Constraints

```text
1 <= len(prices)
buy day must occur before sell day
return zero if no profit is possible
```

## 16. Longest Substring Without Repeating Characters

Source:

- LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Difficulty: Medium

Pattern: sliding window

### Problem

Given a string, return the length of the longest substring that contains no
repeated characters.

A substring must be contiguous.

### Input

```text
s: string
```

### Output

```text
integer
```

### Example 1

Input:

```text
s = "abcabcbb"
```

Output:

```text
3
```

Explanation:

```text
One longest substring without repeated characters is "abc".
```

### Example 2

Input:

```text
s = "bbbbb"
```

Output:

```text
1
```

### Example 3

Input:

```text
s = "pwwkew"
```

Output:

```text
3
```

Explanation:

```text
One longest valid substring is "wke".
```

### Constraints

```text
s may be empty
characters may include letters, digits, symbols, or spaces
substring means contiguous characters
```

## 17. Permutation in String

Source:

- LeetCode: https://leetcode.com/problems/permutation-in-string/

Difficulty: Medium

Pattern: sliding window / character counts

### Problem

Given two strings `s1` and `s2`, determine whether any substring of `s2` is a
permutation of `s1`.

Return `true` if such a substring exists.

Return `false` otherwise.

A permutation uses the same characters with the same counts, but may be in a
different order.

### Input

```text
s1: string
s2: string
```

### Output

```text
boolean
```

### Example 1

Input:

```text
s1 = "ab"
s2 = "eidbaooo"
```

Output:

```text
true
```

Explanation:

```text
The substring "ba" is a permutation of "ab".
```

### Example 2

Input:

```text
s1 = "ab"
s2 = "eidboaoo"
```

Output:

```text
false
```

### Constraints

```text
s1 and s2 contain lowercase English letters unless otherwise stated
the matching substring must be contiguous
the substring length must equal len(s1)
```

## Week 2 implementation checklist

For each problem:

- implement the Python solution,
- implement the C++ solution,
- state time complexity,
- state space complexity,
- test the given examples,
- add at least one edge case,
- explain the pointer or window invariant out loud.

## Week 2 edge cases to remember

| Problem | Edge case |
| --- | --- |
| Valid Palindrome | string has only spaces or punctuation |
| Two Sum II | target uses first and last values |
| 3Sum | many duplicate values |
| Container With Most Water | only two lines |
| Squares of a Sorted Array | all values are negative |
| Best Time to Buy and Sell Stock | prices only decrease |
| Longest Substring Without Repeating Characters | empty string |
| Permutation in String | `s1` is longer than `s2` |

## Week 2 pattern summary

Two pointers are useful when:

- the input is sorted,
- you need to compare values from both ends,
- you can move one pointer based on a monotonic condition,
- you want to avoid nested loops.

Sliding window is useful when:

- the answer depends on a contiguous subarray or substring,
- the window can expand and shrink,
- the algorithm maintains counts, sums, or a validity condition,
- each element enters and leaves the window a small number of times.
