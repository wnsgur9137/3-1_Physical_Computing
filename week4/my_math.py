def power(base, expo):
    """
    거듭제곱 함수
    :param base: 밑
    :param expo: 지수
    :return: 계산 결과 값
    """
    result = 1
    for k in range(expo):
        result = result * base
    return result

def square(n):
    """
    제곱 함수
    :param n: 정수 1개
    :return: 제곱한 결과
    """
    return n*n

def fibo_recursion(n):
    """
    피보나치 수열 함수
    f(n) f(n-1) + f(n-2)
    f(1) = 1
    f(2) = 1
    :param n:
    :return:
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)

def factorial_loop(n):
    """
    팩토리얼 함수 by 반복문
    """
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result