# Week 2 Coding Problem Statements

Week 2 focuses on two pointers and sliding window problems.

Use this file to understand each problem before implementing it in both Python
and C++.

Solutions are added below each problem as it is covered.

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

> **10. Valid Palindrome** | [LeetCode][problem-10] | **Easy** | **Pattern:** two pointers
>
> **Problem:** Given a string, determine whether it is a palindrome after ignoring all non-alphanumeric characters and
> ignoring case. A palindrome reads the same forward and backward after this normalization.
>
> **Input:** `s: string`<br>
> **Output:** `boolean`<br>
> **Example 1:** `s = "A man, a plan, a canal: Panama"` -> `true`. After normalization, the string is
> "amanaplanacanalpanama". This reads the same forward and backward.<br>
> **Example 2:** `s = "race a car"` -> `false`<br>
> **Example 3:** `s = " "` -> `true`<br>
> **Constraints:** `1 <= len(s) <= 200000`; `s contains only printable ASCII characters`;
> `comparison is case-insensitive`; `non-alphanumeric characters are ignored`

<table>
<tr>
<td valign="top">

```python
def is_palindrome(s: str) -> bool:
    normalized = "".join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(normalized) - 1
    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left += 1
        right -= 1
    return True
```

</td>
<td valign="top">

```cpp
bool isPalindrome(const string& s) {
    string normalized;
    normalized.reserve(s.size());
    for (unsigned char value : s) {
        if (isalnum(value)) {
            normalized.push_back(static_cast<char>(tolower(value)));
        }
    }

    int left = 0;
    int right = static_cast<int>(normalized.size()) - 1;
    while (left < right) {
        if (normalized[left] != normalized[right]) {
            return false;
        }
        ++left;
        --right;
    }
    return true;
}
```

</td>
</tr>
</table>

**Complexity (both):** `O(n)` time and `O(n)` auxiliary space.

<!-- -->

> **11. Two Sum II - Input Array Is Sorted** | [LeetCode][problem-11] | **Medium** | **Pattern:** two pointers
>
> **Problem:** Given a sorted array of integers and a target value, return the 1-based indices of two numbers whose sum
> equals the target. The input array is sorted in non-decreasing order. Assume exactly one valid pair exists. The same
> element cannot be used twice.
>
> **Input:** `numbers: sorted list of integers`; `target: integer`<br>
> **Output:** `list of two 1-based indices`<br>
> **Example 1:** `numbers = [2, 7, 11, 15]`; `target = 9` -> `[1, 2]`<br>
> **Example 2:** `numbers = [2, 3, 4]`; `target = 6` -> `[1, 3]`<br>
> **Example 3:** `numbers = [-1, 0]`; `target = -1` -> `[1, 2]`<br>
> **Constraints:** `2 <= len(numbers)`; `numbers is sorted in non-decreasing order`; `exactly one valid answer exists`;
> `return 1-based indices`

<table>
<tr>
<td valign="top">

```python
def two_sum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1
    return []
```

</td>
<td valign="top">

```cpp
vector<int> twoSum(const vector<int>& numbers, int target) {
    int left = 0;
    int right = static_cast<int>(numbers.size()) - 1;
    while (left < right) {
        long long total = static_cast<long long>(numbers[left]) + numbers[right];
        if (total == target) {
            return {left + 1, right + 1};
        }
        if (total < target) {
            ++left;
        } else {
            --right;
        }
    }
    return {};
}
```

</td>
</tr>
</table>

**Complexity (both):** `O(n)` time and `O(1)` auxiliary space.

<!-- -->

> **12. 3Sum** | [LeetCode][problem-12] | **Medium** | **Pattern:** sorting + two pointers
>
> **Problem:** Given an integer array, return all unique triplets whose values sum to zero. Each triplet should contain
> three different array positions. The output must not contain duplicate triplets. The order of triplets does not
> matter. The order of values inside a triplet does not matter.
>
> **Input:** `nums: list of integers`<br>
> **Output:** `list of integer triplets`<br>
> **Example 1:** `nums = [-1, 0, 1, 2, -1, -4]` -> `[[-1, -1, 2], [-1, 0, 1]]` (one valid output)<br>
> **Example 2:** `nums = [0, 1, 1]` -> `[]`<br>
> **Example 3:** `nums = [0, 0, 0]` -> `[[0, 0, 0]]`<br>
> **Constraints:** `triplets must use three distinct indices`; `duplicate triplets must be removed`;
> `array may contain positive, negative, and zero values`

<table>
<tr>
<td valign="top">

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    values = sorted(nums)
    result = []
    for first in range(len(values) - 2):
        if values[first] > 0:
            break
        if first > 0 and values[first] == values[first - 1]:
            continue

        left, right = first + 1, len(values) - 1
        while left < right:
            total = values[first] + values[left] + values[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([values[first], values[left], values[right]])
                left += 1
                right -= 1
                while left < right and values[left] == values[left - 1]:
                    left += 1
                while left < right and values[right] == values[right + 1]:
                    right -= 1
    return result
```

</td>
<td valign="top">

```cpp
vector<vector<int>> threeSum(const vector<int>& nums) {
    vector<int> values = nums;
    sort(values.begin(), values.end());
    vector<vector<int>> result;
    int n = static_cast<int>(values.size());
    for (int first = 0; first < n - 2; ++first) {
        if (values[first] > 0) {
            break;
        }
        if (first > 0 && values[first] == values[first - 1]) {
            continue;
        }

        int left = first + 1;
        int right = n - 1;
        while (left < right) {
            long long total = static_cast<long long>(values[first]) + values[left] + values[right];
            if (total < 0) {
                ++left;
            } else if (total > 0) {
                --right;
            } else {
                result.push_back({values[first], values[left], values[right]});
                ++left;
                --right;
                while (left < right && values[left] == values[left - 1]) {
                    ++left;
                }
                while (left < right && values[right] == values[right + 1]) {
                    --right;
                }
            }
        }
    }
    return result;
}
```

</td>
</tr>
</table>

**Complexity (both):** `O(n^2)` time and `O(n)` auxiliary space for the sorted copy, excluding output.
The input is unchanged.

<!-- -->

> **13. Container With Most Water** | [LeetCode][problem-13] | **Medium** | **Pattern:** two pointers
>
> **Problem:** You are given an array of non-negative integers where each value represents the height of a vertical
> line. Choose two lines so that, together with the x-axis, they form a container. Return the maximum amount of water
> the container can hold. The width is the distance between the two chosen indices. The height of the container is
> limited by the shorter of the two lines.
>
> **Input:** `height: list of non-negative integers`<br>
> **Output:** `integer`<br>
> **Example 1:** `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]` -> `49`<br>
> **Example 2:** `height = [1, 1]` -> `1`<br>
> **Constraints:** `2 <= len(height)`; `heights are non-negative`; `choose exactly two different indices`

<table>
<tr>
<td valign="top">

```python
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        best = max(best, area)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return best
```

</td>
<td valign="top">

```cpp
long long maxArea(const vector<int>& height) {
    int left = 0;
    int right = static_cast<int>(height.size()) - 1;
    long long best = 0;
    while (left < right) {
        long long area = static_cast<long long>(min(height[left], height[right])) * (right - left);
        best = max(best, area);
        if (height[left] <= height[right]) {
            ++left;
        } else {
            --right;
        }
    }
    return best;
}
```

</td>
</tr>
</table>

**Complexity (both):** `O(n)` time and `O(1)` auxiliary space.

C++ uses `long long` here and in Problems 14-15 to avoid overflowing products or differences of `int` inputs.

<!-- -->

> **14. Squares of a Sorted Array** | [LeetCode][problem-14] | **Easy** | **Pattern:** two pointers
>
> **Problem:** Given a sorted integer array, return a new array containing the squares of each number, also sorted in
> non-decreasing order. The input may contain negative numbers, so the largest square may come from either end of the
> array.
>
> **Input:** `nums: sorted list of integers`<br>
> **Output:** `sorted list of squared integers`<br>
> **Example 1:** `nums = [-4, -1, 0, 3, 10]` -> `[0, 1, 9, 16, 100]`<br>
> **Example 2:** `nums = [-7, -3, 2, 3, 11]` -> `[4, 9, 9, 49, 121]`<br>
> **Constraints:** `nums is sorted in non-decreasing order`; `nums may contain negative, zero, and positive values`;
> `return a new sorted array`

<table>
<tr>
<td valign="top">

```python
def sorted_squares(nums: list[int]) -> list[int]:
    result = [0] * len(nums)
    left, right = 0, len(nums) - 1
    for write in range(len(nums) - 1, -1, -1):
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]
        if left_square > right_square:
            result[write] = left_square
            left += 1
        else:
            result[write] = right_square
            right -= 1
    return result
```

</td>
<td valign="top">

```cpp
vector<long long> sortedSquares(const vector<int>& nums) {
    int n = static_cast<int>(nums.size());
    vector<long long> result(n);
    int left = 0;
    int right = n - 1;
    for (int write = n - 1; write >= 0; --write) {
        long long leftSquare = static_cast<long long>(nums[left]) * nums[left];
        long long rightSquare = static_cast<long long>(nums[right]) * nums[right];
        if (leftSquare > rightSquare) {
            result[write] = leftSquare;
            ++left;
        } else {
            result[write] = rightSquare;
            --right;
        }
    }
    return result;
}
```

</td>
</tr>
</table>

**Complexity (both):** `O(n)` time and `O(1)` auxiliary space, excluding the `O(n)` output.

<!-- -->

> **15. Best Time to Buy and Sell Stock** | [LeetCode][problem-15] | **Easy** | **Pattern:** sliding window / running
> minimum
>
> **Problem:** Given a list of daily stock prices, choose one day to buy and a later day to sell. Return the maximum
> profit possible. If no profitable transaction is possible, return zero. You may complete at most one buy and one sell
> transaction.
>
> **Input:** `prices: list of integers`<br>
> **Output:** `integer`<br>
> **Example 1:** `prices = [7, 1, 5, 3, 6, 4]` -> `5`. Buy at price 1 and sell later at price 6.<br>
> **Example 2:** `prices = [7, 6, 4, 3, 1]` -> `0`<br>
> **Constraints:** `1 <= len(prices)`; `buy day must occur before sell day`; `return zero if no profit is possible`

<table>
<tr>
<td valign="top">

```python
def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    lowest = prices[0]
    best = 0
    for index in range(1, len(prices)):
        best = max(best, prices[index] - lowest)
        lowest = min(lowest, prices[index])
    return best
```

</td>
<td valign="top">

```cpp
long long maxProfit(const vector<int>& prices) {
    if (prices.empty()) {
        return 0;
    }

    int lowest = prices[0];
    long long best = 0;
    for (int index = 1; index < static_cast<int>(prices.size()); ++index) {
        long long profit = static_cast<long long>(prices[index]) - lowest;
        best = max(best, profit);
        lowest = min(lowest, prices[index]);
    }
    return best;
}
```

</td>
</tr>
</table>

**Complexity (both):** `O(n)` time and `O(1)` auxiliary space.

<!-- -->

> **16. Longest Substring Without Repeating Characters** | [LeetCode][problem-16] | **Medium** | **Pattern:** sliding
> window
>
> **Problem:** Given a string, return the length of the longest substring that contains no repeated characters. A
> substring must be contiguous.
>
> **Input:** `s: string`<br>
> **Output:** `integer`<br>
> **Example 1:** `s = "abcabcbb"` -> `3`. One longest substring without repeated characters is "abc".<br>
> **Example 2:** `s = "bbbbb"` -> `1`<br>
> **Example 3:** `s = "pwwkew"` -> `3`. One longest valid substring is "wke".<br>
> **Constraints:** `s may be empty`; `characters may include letters, digits, symbols, or spaces`;
> `substring means contiguous characters`

<table>
<tr>
<td valign="top">

```python
def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = 0
    best = 0
    for right, char in enumerate(s):
        if char in last_seen:
            left = max(left, last_seen[char] + 1)
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best
```

</td>
<td valign="top">

```cpp
int lengthOfLongestSubstring(const string& s) {
    unordered_map<char, int> lastSeen;
    int left = 0;
    int best = 0;
    for (int right = 0; right < static_cast<int>(s.size()); ++right) {
        auto match = lastSeen.find(s[right]);
        if (match != lastSeen.end()) {
            left = max(left, match->second + 1);
        }
        lastSeen[s[right]] = right;
        best = max(best, right - left + 1);
    }
    return best;
}
```

</td>
</tr>
</table>

**Complexity (both):** `O(n)` expected time and `O(min(n, a))` auxiliary space, where `a` is alphabet size.
The C++ function treats `string` characters as bytes; Python operates on Unicode code points.

<!-- -->

> **17. Permutation in String** | [LeetCode][problem-17] | **Medium** | **Pattern:** sliding window / character counts
>
> **Problem:** Given two strings `s1` and `s2`, determine whether any substring of `s2` is a permutation of `s1`.
> Return `true` if such a substring exists. Return `false` otherwise. A permutation uses the same characters with the
> same counts, but may be in a different order.
>
> **Input:** `s1: string`; `s2: string`<br>
> **Output:** `boolean`<br>
> **Example 1:** `s1 = "ab"`; `s2 = "eidbaooo"` -> `true`. The substring "ba" is a permutation of "ab".<br>
> **Example 2:** `s1 = "ab"`; `s2 = "eidboaoo"` -> `false`<br>
> **Constraints:** `s1 and s2 contain lowercase English letters unless otherwise stated`;
> `the matching substring must be contiguous`; `the substring length must equal len(s1)`

<table>
<tr>
<td valign="top">

```python
def check_inclusion(s1: str, s2: str) -> bool:
    size = len(s1)
    if size > len(s2):
        return False

    required = [0] * 26
    window = [0] * 26
    for index in range(size):
        required[ord(s1[index]) - ord("a")] += 1
        window[ord(s2[index]) - ord("a")] += 1
    if window == required:
        return True

    for right in range(size, len(s2)):
        window[ord(s2[right]) - ord("a")] += 1
        window[ord(s2[right - size]) - ord("a")] -= 1
        if window == required:
            return True
    return False
```

</td>
<td valign="top">

```cpp
bool checkInclusion(const string& s1, const string& s2) {
    if (s1.size() > s2.size()) {
        return false;
    }

    int size = static_cast<int>(s1.size());
    vector<int> required(26, 0);
    vector<int> window(26, 0);
    for (int index = 0; index < size; ++index) {
        ++required[s1[index] - 'a'];
        ++window[s2[index] - 'a'];
    }
    if (window == required) {
        return true;
    }

    for (int right = size; right < static_cast<int>(s2.size()); ++right) {
        ++window[s2[right] - 'a'];
        --window[s2[right - size] - 'a'];
        if (window == required) {
            return true;
        }
    }
    return false;
}
```

</td>
</tr>
</table>

**Complexity (both):** `O(m + n)` time and `O(1)` auxiliary space for the fixed 26-letter alphabet.
Here `m = len(s1)` and `n = len(s2)`; comparing 26 counts per window is constant work.

[problem-10]: https://leetcode.com/problems/valid-palindrome/
[problem-11]: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
[problem-12]: https://leetcode.com/problems/3sum/
[problem-13]: https://leetcode.com/problems/container-with-most-water/
[problem-14]: https://leetcode.com/problems/squares-of-a-sorted-array/
[problem-15]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
[problem-16]: https://leetcode.com/problems/longest-substring-without-repeating-characters/
[problem-17]: https://leetcode.com/problems/permutation-in-string/

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
