# Tuple
a = (1, 2, 3)  # List와 비슷하지만, 변경이 불가능함. *fix 되어있음

# Dictionary / 연관 배열(Associative arry) or Hash / Key를 통해 Value를 얻음
dic = {'name': 'Young', 'age': 25}

print(dic['name'])

a = {1: 'a'}
a['name'] = "Unknown"  # 쌍 추가하기
del a[1]  # List와 다르게 해당 Key를 입력해줘야함
print(a)

b = {1: 'a', 2: 'b', 3: 'c'}

print(b.keys())
print(b.values())
print(b.items())  # 새로운 배열 안에 튜플 형태로 Key Value 쌍을 담을 수 있음
print(b.get(4))  # value 얻기 / 없는 key면 none이 출력됨
print(4 in b)
