"""
문제
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

입력
첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

출력
첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
"""

# A = int(input())
# B = int(input())
# C = int(input())
# num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# N = A * B * C
# for i in range(len(str(N))):
#     i = int(i)
#     if (i == 0):
#         num[0] += 1
#     if (i == 1):
#         num[1] += 1
#     if (i == 2):
#         num[2] += 1
#     if (i == 3):
#         num[3] += 1
#     if (i == 4):
#         num[4] += 1
#     if (i == 5):
#         num[5] += 1
#     if (i == 6):
#         num[6] += 1
#     if (i == 7):
#         num[7] += 1
#     if (i == 8):
#         num[8] += 1
#     if (i == 9):
#         num[9] += 1
# print(num[0])
# print(num[1])
# print(num[2])
# print(num[3])
# print(num[4])
# print(num[5])
# print(num[6])
# print(num[7])
# print(num[8])
# print(num[9])

""" solve """
A = int(input())
B = int(input())
C = int(input())
num = list(str(A * B * C))

for i in range(10):
    print(result.count(str(i)))