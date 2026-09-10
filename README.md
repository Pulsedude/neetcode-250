# 🎯 NeetCode 250 Solutions (Python)

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![NeetCode 250](https://img.shields.io/badge/Roadmap-NeetCode%20250-blue)](https://neetcode.io/roadmap)

This repository contains my solutions and notes for the **[NeetCode 250](https://neetcode.io/roadmap)** problem set, implemented in Python. Each solution includes different approaches (e.g., brute force vs. optimal) along with time and space complexity analyses.

---

## 📊 Progress Tracker

- [ ] **Arrays & Hashing** (19 / 22)
- [ ] **Two Pointers** (2 / 13)
- [ ] **Sliding Window** (0 / 9)
- [ ] **Stack** (1 / 14)
- [ ] **Binary Search** (0 / 14)
- [ ] **Linked List** (0 / 14)
- [ ] **Trees** (0 / 23)
- [ ] **Tries** (0 / 4)
- [ ] **Heap / Priority Queue** (0 / 12)
- [ ] **Backtracking** (0 / 17)
- [ ] **Graphs** (0 / 21)
- [ ] **Advanced Graphs** (0 / 10)
- [ ] **1-D Dynamic Programming** (0 / 17)
- [ ] **2-D Dynamic Programming** (0 / 16)
- [ ] **Greedy** (0 / 14)
- [ ] **Intervals** (0 / 7)
- [ ] **Math & Geometry** (0 / 13)
- [ ] **Bit Manipulation** (0 / 10)

---


## 📝 Solutions List

### 1. Arrays & Hashing

| # | Problem | Difficulty | Solution | Time Complexity | Space Complexity |
|---|---|---|---|---|---|
| 1 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | [concatenation_of_array.py](./array_and_hashing/concatenation_of_array.py) | $O(n)$ | $O(n)$ |
| 2 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | [contains_duplicate.py](./array_and_hashing/contains_duplicate.py) | $O(n)$ | $O(n)$ |
| 3 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | [valid_anagram.py](./array_and_hashing/valid_anagram.py) | $O(n)$ | $O(1)$ |
| 4 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [two_sum.py](./array_and_hashing/two_sum.py) | $O(n)$ | $O(n)$ |
| 5 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | [longest_common_prefix.py](./array_and_hashing/longest_common_prefix.py) | $O(n \cdot m)$ | $O(1)$ |
| 6 | [Majority Element](https://leetcode.com/problems/majority-element/) | Easy | [majority_element.py](./array_and_hashing/majority_element.py) | $O(n)$ | $O(1)$ |
| 7 | [Design HashSet](https://leetcode.com/problems/design-hashset/) | Easy | [design_hashset.py](./array_and_hashing/design_hashset.py) | $O(1)$ avg | $O(n)$ |
| 8 | [Design HashMap](https://leetcode.com/problems/design-hashmap/) | Easy | [design_hashmap.py](./array_and_hashing/design_hashmap.py) | $O(1)$ avg | $O(n)$ |
| 9 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | [group_anagrams.py](./array_and_hashing/group_anagrams.py) | $O(m \cdot n)$ | $O(m \cdot n)$ |
| 10 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [top_k_frequent_elements.py](./array_and_hashing/top_k_frequent_elements.py) | $O(n)$ | $O(n)$ |
| 11 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | [sort_colors.py](./array_and_hashing/sort_colors.py) | $O(n)$ | $O(1)$ |
| 12 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Medium | [encode_and_decode_strings.py](./array_and_hashing/encode_and_decode_strings.py) | $O(n \cdot m)$ | $O(n + m)$ |
| 13 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | [product_of_array_except_itself.py](./array_and_hashing/product_of_array_except_itself.py) | $O(n)$ | $O(1)$ |
| 14 | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | Medium | [range_sum_query_2d_immutable.py](./array_and_hashing/range_sum_query_2d_immutable.py) | $O(1)$ | $O(1)$ |
| 15 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | [valid_sudoku.py](./array_and_hashing/valid_sudoku.py) | $O(n^2)$ | $O(1)$ |
| 16 | [Sort an Array](https://leetcode.com/problems/sort-an-array/) | Medium | [sort_an_array.py](./array_and_hashing/sort_an_array.py) | $O(n + k)$ | $O(k)$ |
| 17 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | [longest_consecutive_sequence.py](./array_and_hashing/longest_consecutive_sequence.py) | $O(n)$ | $O(n)$ |
| 18 | [Remove Element](https://leetcode.com/problems/remove-element/) | Easy | [remove_element.py](./array_and_hashing/remove_element.py) | $O(n)$ | $O(1)$ |
| 19 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Medium | [best_time_to_buy_and_sell_stock_2.py](./array_and_hashing/best_time_to_buy_and_sell_stock_2.py) | $O(n)$ | $O(1)$ |

### 2. Two Pointers

| # | Problem | Difficulty | Solution | Time Complexity | Space Complexity |
|---|---|---|---|---|---|
| 1 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | [reverse_string.py](./two_pointers/reverse_string.py) | $O(n)$ | $O(1)$ |
| 2 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | [valid_palindrome.py](./two_pointers/valid_palindrome.py) | $O(n)$ | $O(1)$ |

### 4. Stack

| # | Problem | Difficulty | Solution | Time Complexity | Space Complexity |
|---|---|---|---|---|---|
| 1 | [Baseball Game](https://leetcode.com/problems/baseball-game/) | Easy | [baseball_game.py](./stack/baseball_game.py) | $O(n)$ | $O(m)$ |



## 📌 Resources

- [NeetCode Practice (NeetCode 250)](https://neetcode.io/roadmap)
