/*
문제
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

출력
첫째 줄에 다음 세 가지 중 하나를 출력한다.

A가 B보다 큰 경우에는 '>'를 출력한다.
A가 B보다 작은 경우에는 '<'를 출력한다.
A와 B가 같은 경우에는 '=='를 출력한다.
제한
-10,000 ≤ A, B ≤ 10,000
*/

#include <stdio.h>

void main()
{
    int num1 = 0;
    int num2 = 0;
    scanf_s("%d", &num1);
    scnaf_s("%d", &num2);
    // scanf의 경우 visual studio에서는 오류가 발생하여 #ddefine N0_SECURE_WARNINGS 를 적어줘야함

    if (num1 > num2) {
        printf(">");
    } else if (num1 < num2) {
        printf("<");
    } else {
        printf("=");
    }
    
    return 0;
}