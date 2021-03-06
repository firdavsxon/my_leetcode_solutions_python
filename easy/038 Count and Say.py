"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
You can do so recursively, in other words from the previous member read off the digits,
counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1",
"2" can be read as "12" which means frequency = 1 and value = 2, the same way "1"
is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
"""


class Solution:
	def countAndSay(self, n: int) -> str:

		if n == 1:
			return '1'
		base = '1'
		for i in range(2, n + 1):
			ind = 0
			cur_char = base[0]
			cur_counter = 0
			next_base = []

			while ind < len(base):
				if base[ind] == cur_char:
					cur_counter += 1
				else:
					next_base.append(str(cur_counter))
					next_base.append(cur_char)

					cur_char = base[ind]
					cur_counter = 1

				ind += 1

			next_base.append(str(cur_counter))
			next_base.append(cur_char)
			base = ''.join(next_base)

		return base

	def countAndSay1(self, n: int) -> str:
		a = 1
		b = ''
		s = "1"
		while n - 1:
			s = s + str(0)
			for i in range(len(s) - 1):
				if s[i] == s[i + 1]:
					a += 1
				else:
					b += str(a) + s[i]
					a = 1
			s = b
			n -= 1
			b = ''
		return s

test = Solution()
print(test.countAndSay1(6))
