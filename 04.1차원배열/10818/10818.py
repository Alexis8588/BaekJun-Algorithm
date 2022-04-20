# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

import sys

N = int(input())
arr = []

for i in range(N):
    T = int(input())
    arr.append(T)

max = arr[0]
min = arr[0]
for j in range(len(arr)):
    if (arr[j] > max):
        max = arr[j]
    if (arr[j] < min):
        min = arr[j]
print(f'{min} {max}')

""" solve 1"""
N = sys.stdin.readline() # 이게 숫자를 엔터 치기 전까지 입력하는건가?
Num = list(map(int, input().split()))
max = Num[0]
min = Num[0]
for i in Num:
    if i > max:
        max = i
    if i < min:
        min = i
print(min, max, ned='')

""" solve 2 내장 함수 이용"""
N = sys.stdin.readline()
num_list = list(map(int, input().split()))
print(min(num_list), max(num_list), end='')