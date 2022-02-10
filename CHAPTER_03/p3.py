# for
# for 변수 in 리스트 (or tuple, string):
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]

n = 0
for mark in marks:
    n += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % n)
    else:
        print("%d번 학생은 불합격입니다." % n)

sum = 0
for a in range(1, 11):  # range = 1 <= x < 11
    sum += a
print(sum)

# 이중 for
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")  # end = print 이후에 나올 문자
    print('')
