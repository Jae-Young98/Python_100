# While
treeHit = 0
while treeHit < 10:
    treeHit += 1  # 파이썬은 ++1 이 안됨
    print("나무를 %d 번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무를 총 %d 번 찍었습니다." % treeHit)

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피는 %d 개 입니다." % coffee)
    if not coffee:  # == coffee == 0:
        print("커피가 매진 되었습니다. 판매를 중지합니다.")
        break  # While문이 true 일지라도 반복문을 빠져 나간다

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue  # While문의 처음으로 돌아감
    print(a)
