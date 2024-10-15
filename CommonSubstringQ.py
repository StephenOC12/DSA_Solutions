# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')
_multiplier = 263
_prime = 1000000007

def precompute_hashes(string):
	length = len(string)
	hashes = [0] * (length + 1)
	for i in range(1, length + 1):
		hashes[i] = (hashes[i - 1] * _multiplier + ord(string[i - 1])) % _prime
	return hashes

def hash_func(hashes, start, length):
	y = pow(_multiplier, length, _prime)
	hash_value = (hashes[start + length] - y * hashes[start]) % _prime
	return hash_value

def get_common_substring(s_hashes, t_hashes, length):
	hash_dict = {}
	for i in range(len(s_hashes) - length):
		hash_value = hash_func(s_hashes, i, length)
		if hash_value not in hash_dict:
			hash_dict[hash_value] = i
	for j in range(len(t_hashes) - length):
		hash_value = hash_func(t_hashes, j, length)
		if hash_value in hash_dict:
			return hash_dict[hash_value], j
	return -1, -1

def solve(s, t):
	s_hashes = precompute_hashes(s)
	t_hashes = precompute_hashes(t)
	left, right = 0, min(len(s), len(t)) + 1
	while right - left > 1:
		mid = (left + right) // 2
		i, j = get_common_substring(s_hashes, t_hashes, mid)
		if i != -1 and j != -1:
			left = mid
		else:
			right = mid
	i, j = get_common_substring(s_hashes, t_hashes, left)
	return Answer(i, j, left)

for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)