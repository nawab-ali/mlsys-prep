# Week 1 Coding Problem Statements

Week 1 focuses on arrays, hashing, and basic string problems.

Use this file to understand what each problem asks for before implementing it
in both Python and C++.

Do not write solutions in this file.

## Week 1 problem list

| # | Problem | Difficulty | Pattern |
| ---: | --- | --- | --- |
| 1 | Two Sum | Easy | Hash map |
| 2 | Contains Duplicate | Easy | Hash set |
| 3 | Valid Anagram | Easy | Hash map |
| 4 | Group Anagrams | Medium | Hash map |
| 5 | Top K Frequent Elements | Medium | Heap / bucket |
| 6 | Product of Array Except Self | Medium | Prefix / suffix |
| 7 | Majority Element | Easy | Boyer-Moore |
| 8 | Missing Number | Easy | Math / XOR |
| 9 | Move Zeroes | Easy | Array pointers |

## 1. Two Sum

Source:

- LeetCode: https://leetcode.com/problems/two-sum/

Difficulty: Easy

Pattern: hash map

### Problem

Given an array of integers and a target value, return the indices of two
different elements whose values add up to the target.

Assume there is exactly one valid pair.

The same array element cannot be used twice.

The returned indices may be in any order.

### Input

```text
nums: list of integers
target: integer
```

### Output

```text
list of two integer indices
```

### Example 1

Input:

```text
nums = [2, 7, 11, 15]
target = 9
```

Output:

```text
[0, 1]
```

### Example 2

Input:

```text
nums = [3, 2, 4]
target = 6
```

Output:

```text
[1, 2]
```

### Constraints

```text
2 <= len(nums)
exactly one valid answer exists
indices must refer to two distinct positions
```

## 2. Contains Duplicate

Source:

- LeetCode: https://leetcode.com/problems/contains-duplicate/

Difficulty: Easy

Pattern: hash set

### Problem

Given an integer array, determine whether any value appears at least twice.

Return `true` if the array contains a duplicate value.

Return `false` if every value is distinct.

### Input

```text
nums: list of integers
```

### Output

```text
boolean
```

### Example 1

Input:

```text
nums = [1, 2, 3, 1]
```

Output:

```text
true
```

### Example 2

Input:

```text
nums = [1, 2, 3, 4]
```

Output:

```text
false
```

### Constraints

```text
1 <= len(nums)
values may be positive, negative, or zero
```

## 3. Valid Anagram

Source:

- LeetCode: https://leetcode.com/problems/valid-anagram/

Difficulty: Easy

Pattern: hash map / character count

### Problem

Given two strings, determine whether the second string is an anagram of the
first string.

An anagram uses exactly the same characters with exactly the same counts, but
the order may differ.

### Input

```text
s: string
t: string
```

### Output

```text
boolean
```

### Example 1

Input:

```text
s = "anagram"
t = "nagaram"
```

Output:

```text
true
```

### Example 2

Input:

```text
s = "rat"
t = "car"
```

Output:

```text
false
```

### Constraints

```text
strings contain lowercase English letters unless otherwise stated
the two strings may have different lengths
```

## 4. Group Anagrams

Source:

- LeetCode: https://leetcode.com/problems/group-anagrams/

Difficulty: Medium

Pattern: hash map

### Problem

Given a list of strings, group together all strings that are anagrams of each
other.

Each group should contain words with the same character multiset.

The order of groups does not matter.

The order of words inside each group does not matter.

### Input

```text
strs: list of strings
```

### Output

```text
list of groups, where each group is a list of strings
```

### Example 1

Input:

```text
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

One valid output:

```text
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

### Example 2

Input:

```text
strs = [""]
```

Output:

```text
[[""]]
```

### Constraints

```text
input contains one or more strings
strings may be empty
group order is not important
```

## 5. Top K Frequent Elements

Source:

- LeetCode: https://leetcode.com/problems/top-k-frequent-elements/

Difficulty: Medium

Pattern: frequency map, heap, bucket sort

### Problem

Given an integer array and an integer `k`, return the `k` values that appear
most frequently in the array.

The returned values may be in any order.

### Input

```text
nums: list of integers
k: integer
```

### Output

```text
list of k integers
```

### Example 1

Input:

```text
nums = [1, 1, 1, 2, 2, 3]
k = 2
```

Output:

```text
[1, 2]
```

### Example 2

Input:

```text
nums = [1]
k = 1
```

Output:

```text
[1]
```

### Constraints

```text
1 <= k <= number of distinct values in nums
answer may be returned in any order
```

## 6. Product of Array Except Self

Source:

- LeetCode: https://leetcode.com/problems/product-of-array-except-self/

Difficulty: Medium

Pattern: prefix / suffix

### Problem

Given an integer array, return a new array where each position contains the
product of all input elements except the element at that same position.

Do not use division.

The intended solution should run in linear time.

### Input

```text
nums: list of integers
```

### Output

```text
list of integers
```

### Example 1

Input:

```text
nums = [1, 2, 3, 4]
```

Output:

```text
[24, 12, 8, 6]
```

### Example 2

Input:

```text
nums = [-1, 1, 0, -3, 3]
```

Output:

```text
[0, 0, 9, 0, 0]
```

### Constraints

```text
2 <= len(nums)
do not use division
target time complexity is O(n)
```

## 7. Majority Element

Source:

- LeetCode: https://leetcode.com/problems/majority-element/

Difficulty: Easy

Pattern: Boyer-Moore voting / hash map

### Problem

Given an integer array, return the value that appears more than half the time.

You may assume that a majority element always exists.

### Input

```text
nums: list of integers
```

### Output

```text
integer
```

### Example 1

Input:

```text
nums = [3, 2, 3]
```

Output:

```text
3
```

### Example 2

Input:

```text
nums = [2, 2, 1, 1, 1, 2, 2]
```

Output:

```text
2
```

### Constraints

```text
1 <= len(nums)
a majority element is guaranteed to exist
majority means frequency greater than floor(n / 2)
```

## 8. Missing Number

Source:

- LeetCode: https://leetcode.com/problems/missing-number/

Difficulty: Easy

Pattern: math / XOR

### Problem

Given an array containing `n` distinct numbers from the range `[0, n]`, return
the one number in that range that is missing from the array.

The array length is `n`, and the complete range contains `n + 1` values.

### Input

```text
nums: list of distinct integers from the range [0, n]
```

### Output

```text
integer
```

### Example 1

Input:

```text
nums = [3, 0, 1]
```

Output:

```text
2
```

### Example 2

Input:

```text
nums = [0, 1]
```

Output:

```text
2
```

### Example 3

Input:

```text
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
```

Output:

```text
8
```

### Constraints

```text
n == len(nums)
all values are distinct
all values are in the range [0, n]
```

## 9. Move Zeroes

Source:

- LeetCode: https://leetcode.com/problems/move-zeroes/

Difficulty: Easy

Pattern: array pointers

### Problem

Given an integer array, move every zero to the end of the array while preserving
the relative order of the non-zero elements.

Modify the array in place.

Do not create a separate copy of the array as the final result.

### Input

```text
nums: list of integers
```

### Output

```text
no explicit return value
nums is modified in place
```

### Example 1

Input:

```text
nums = [0, 1, 0, 3, 12]
```

After modification:

```text
nums = [1, 3, 12, 0, 0]
```

### Example 2

Input:

```text
nums = [0]
```

After modification:

```text
nums = [0]
```

### Constraints

```text
1 <= len(nums)
relative order of non-zero elements must be preserved
modification must be in place
```

## Week 1 implementation checklist

For each problem:

- implement the Python solution,
- implement the C++ solution,
- state time complexity,
- state space complexity,
- test the given examples,
- add at least one edge case,
- explain the pattern out loud.

## Week 1 edge cases to remember

| Problem | Edge case |
| --- | --- |
| Two Sum | pair uses duplicate values at different indices |
| Contains Duplicate | empty or single-element array |
| Valid Anagram | different string lengths |
| Group Anagrams | empty string |
| Top K Frequent Elements | k equals number of distinct values |
| Product of Array Except Self | input contains zero |
| Majority Element | array length one |
| Missing Number | missing value is 0 or n |
| Move Zeroes | all zeros or no zeros |
