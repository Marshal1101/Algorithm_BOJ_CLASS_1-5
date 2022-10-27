## https://www.acmicpc.net/source/42995709

from sys import stdin
from heapq import *
input = stdin.readline

def solution():
	arr1, arr2 = [], []
	for _ in range(int(input())):
		x = int(input())
		if x:
			if x > 0:
				heappush(arr1, x)
			else:
				heappush(arr2, -x)
		elif arr1 and arr2:
			if abs(arr1[0]) == abs(arr2[0]):
				print(-heappop(arr2))
			elif abs(arr1[0]) < abs(arr2[0]):
				print(heappop(arr1))
			else:
				print(-heappop(arr2))
		elif arr1:
			print(heappop(arr1))
		elif arr2:
			print(-heappop(arr2))
		else:
			print(0)

solution()