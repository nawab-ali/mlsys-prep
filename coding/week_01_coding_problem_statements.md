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

> **1. Two Sum** · [LeetCode](https://leetcode.com/problems/two-sum/) · **Easy** ·
> **Pattern:** hash map
>
> **Problem:** Given an array of integers and a target value, return the indices of two different elements whose
> values add up to the target. Assume there is exactly one valid pair. The same array element cannot be used twice.
> The returned indices may be in any order.
>
> **Input:** `nums: list of integers`; `target: integer`<br>
> **Output:** `list of two integer indices`<br>
> **Examples:** `nums = [2, 7, 11, 15]`, `target = 9` -> `[0, 1]`; `nums = [3, 2, 4]`, `target = 6` ->
> `[1, 2]`<br>
> **Constraints:** `2 <= len(nums)`; exactly one valid answer exists; indices must refer to two distinct positions.

<table>
<tr>
<td valign="top">

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []
```

</td>
<td valign="top">

```cpp
vector<int> twoSum(const vector<int>& nums, int target) {
    unordered_map<int, int> seen;
    for (int index = 0; index < nums.size(); ++index) {
        int complement = target - nums[index];
        auto match = seen.find(complement);
        if (match != seen.end()) {
            return {match->second, index};
        }
        seen[nums[index]] = index;
    }
    return {};
}
```

</td>
</tr>
</table>

> **2. Contains Duplicate** · [LeetCode](https://leetcode.com/problems/contains-duplicate/) · **Easy** ·
> **Pattern:** hash set
>
> **Problem:** Given an integer array, determine whether any value appears at least twice. Return `true` if the
> array contains a duplicate value. Return `false` if every value is distinct.
>
> **Input:** `nums: list of integers`<br>
> **Output:** `boolean`<br>
> **Examples:** `nums = [1, 2, 3, 1]` -> `true`; `nums = [1, 2, 3, 4]` -> `false`<br>
> **Constraints:** `1 <= len(nums)`; values may be positive, negative, or zero.

<table>
<tr>
<td valign="top">

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False
```

</td>
<td valign="top">

```cpp
bool containsDuplicate(const vector<int>& nums) {
    unordered_set<int> seen;
    for (int value : nums) {
        if (!seen.insert(value).second) {
            return true;
        }
    }
    return false;
}
```

</td>
</tr>
</table>

> **3. Valid Anagram** · [LeetCode](https://leetcode.com/problems/valid-anagram/) · **Easy** · **Pattern:** hash
> map / character count
>
> **Problem:** Given two strings, determine whether the second string is an anagram of the first string. An anagram
> uses exactly the same characters with exactly the same counts, but the order may differ.
>
> **Input:** `s: string`; `t: string`<br>
> **Output:** `boolean`<br>
> **Examples:** `s = "anagram"`, `t = "nagaram"` -> `true`; `s = "rat"`, `t = "car"` -> `false`<br>
> **Constraints:** strings contain lowercase English letters unless otherwise stated; the two strings may have
> different lengths.

<table>
<tr>
<td valign="top">

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1
    return True
```

</td>
<td valign="top">

```cpp
bool isAnagram(const string& s, const string& t) {
    if (s.size() != t.size()) {
        return false;
    }

    unordered_map<char, int> counts;
    for (char value : s) {
        ++counts[value];
    }

    for (char value : t) {
        auto match = counts.find(value);
        if (match == counts.end() || match->second == 0) {
            return false;
        }
        --match->second;
    }
    return true;
}
```

</td>
</tr>
</table>

> **4. Group Anagrams** · [LeetCode](https://leetcode.com/problems/group-anagrams/) · **Medium** ·
> **Pattern:** hash map
>
> **Problem:** Given a list of strings, group together all strings that are anagrams of each other. Each group should
> contain words with the same character multiset. The order of groups does not matter. The order of words inside
> each group does not matter.
>
> **Input:** `strs: list of strings`<br>
> **Output:** `list of groups, where each group is a list of strings`<br>
> **Examples:** `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]` ->
> `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`; `strs = [""]` -> `[[""]]`<br>
> **Constraints:** input contains one or more strings; strings may be empty; group order is not important.

<table>
<tr>
<td valign="top">

```python
def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
```

</td>
<td valign="top">

```cpp
vector<vector<string>> groupAnagrams(const vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    for (const string& word : strs) {
        string key = word;
        sort(key.begin(), key.end());
        groups[key].push_back(word);
    }

    vector<vector<string>> result;
    for (auto& [key, words] : groups) {
        result.push_back(move(words));
    }
    return result;
}
```

</td>
</tr>
</table>

> **5. Top K Frequent Elements** · [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) · **Medium** ·
> **Pattern:** frequency map, heap, bucket sort
>
> **Problem:** Given an integer array and an integer `k`, return the `k` values that appear most frequently in the
> array. The returned values may be in any order.
>
> **Input:** `nums: list of integers`; `k: integer`<br>
> **Output:** `list of k integers`<br>
> **Examples:** `nums = [1, 1, 1, 2, 2, 3]`, `k = 2` -> `[1, 2]`; `nums = [1]`, `k = 1` -> `[1]`<br>
> **Constraints:** `1 <= k <= number of distinct values in nums`; answer may be returned in any order.

<table>
<tr>
<td valign="top">

```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    frequencies = {}
    for value in nums:
        frequencies[value] = frequencies.get(value, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for value, frequency in frequencies.items():
        buckets[frequency].append(value)

    result = []
    for frequency in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[frequency])
        if len(result) >= k:
            return result[:k]
    return result
```

</td>
<td valign="top">

```cpp
vector<int> topKFrequent(const vector<int>& nums, int k) {
    unordered_map<int, int> frequencies;
    for (int value : nums) {
        ++frequencies[value];
    }

    vector<vector<int>> buckets(nums.size() + 1);
    for (const auto& [value, frequency] : frequencies) {
        buckets[frequency].push_back(value);
    }

    vector<int> result;
    result.reserve(k);
    for (int frequency = buckets.size() - 1; frequency > 0; --frequency) {
        for (int value : buckets[frequency]) {
            result.push_back(value);
            if (result.size() == k) {
                return result;
            }
        }
    }
    return result;
}
```

</td>
</tr>
</table>

> **6. Product of Array Except Self** · [LeetCode](https://leetcode.com/problems/product-of-array-except-self/) ·
> **Medium** · **Pattern:** prefix / suffix
>
> **Problem:** Given an integer array, return a new array where each position contains the product of all input
> elements except the element at that same position. Do not use division. The intended solution should run in linear
> time.
>
> **Input:** `nums: list of integers`<br>
> **Output:** `list of integers`<br>
> **Examples:** `nums = [1, 2, 3, 4]` -> `[24, 12, 8, 6]`; `nums = [-1, 1, 0, -3, 3]` ->
> `[0, 0, 9, 0, 0]`<br>
> **Constraints:** `2 <= len(nums)`; do not use division; target time complexity is `O(n)`.

> **7. Majority Element** · [LeetCode](https://leetcode.com/problems/majority-element/) · **Easy** ·
> **Pattern:** Boyer-Moore voting / hash map
>
> **Problem:** Given an integer array, return the value that appears more than half the time. You may assume that a
> majority element always exists.
>
> **Input:** `nums: list of integers`<br>
> **Output:** `integer`<br>
> **Examples:** `nums = [3, 2, 3]` -> `3`; `nums = [2, 2, 1, 1, 1, 2, 2]` -> `2`<br>
> **Constraints:** `1 <= len(nums)`; a majority element is guaranteed to exist; majority means frequency greater than
> `floor(n / 2)`.

> **8. Missing Number** · [LeetCode](https://leetcode.com/problems/missing-number/) · **Easy** · **Pattern:** math /
> XOR
>
> **Problem:** Given an array containing `n` distinct numbers from the range `[0, n]`, return the one number in that
> range that is missing from the array. The array length is `n`, and the complete range contains `n + 1` values.
>
> **Input:** `nums: list of distinct integers from the range [0, n]`<br>
> **Output:** `integer`<br>
> **Examples:** `nums = [3, 0, 1]` -> `2`; `nums = [0, 1]` -> `2`; `nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]` -> `8`<br>
> **Constraints:** `n == len(nums)`; all values are distinct; all values are in the range `[0, n]`.

> **9. Move Zeroes** · [LeetCode](https://leetcode.com/problems/move-zeroes/) · **Easy** · **Pattern:** array
> pointers
>
> **Problem:** Given an integer array, move every zero to the end of the array while preserving the relative order of
> the non-zero elements. Modify the array in place. Do not create a separate copy of the array as the final result.
>
> **Input:** `nums: list of integers`<br>
> **Output:** `no explicit return value`; `nums` is modified in place<br>
> **Examples:** `nums = [0, 1, 0, 3, 12]` -> `nums = [1, 3, 12, 0, 0]`; `nums = [0]` -> `nums = [0]`<br>
> **Constraints:** `1 <= len(nums)`; relative order of non-zero elements must be preserved; modification must be in
> place.

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
