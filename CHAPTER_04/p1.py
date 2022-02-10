# function
# def 함수명(매개변수):
#   <수행 문장1>
#   <수행 문장2>
# return 리턴 값
from pickle import TRUE
from this import d


def sum(a, b):
    result = a + b
    return result


print(sum(1, 3))


def sum2(a, b):  # 입출력 값, return 값이 없을 수도 있음.
    print("%d, %d의 합은 %d 입니다." % (a, b, a+b))


sum2(3, 5)


def sum_many(*args):
    sum3 = 0
    for i in args:
        sum3 += i
    return sum3


print(sum_many(3, 4, 5, 6, 2347, 2))


def say_myself(name, old, man=TRUE):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("흑재영", 25, TRUE)
