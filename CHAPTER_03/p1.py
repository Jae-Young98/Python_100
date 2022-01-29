# if
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

a = 1
b = 3
if a < b:
    print("a는 b보다 작다")
else:
    print("a는 b보다 작다")

if a in [1, 2, 3]:
    print(a, "은 포함되어 있다")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    pass  # 통과한다
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 조건부 표현식
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
message = "success" if score >= 60 else "failure"  # 위의 조건식을 파이썬은 한줄로 요약 가능
print(message)
