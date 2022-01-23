# List 하나의 변수에 여러 개의 값을 저장 할 때
a = ["int", "double", "char", "short", "float"]

print(a[1])
print(a[0:3])
a[0:2] = ["change", "hi", "test"]
print(a)
del(a[0])
print(a)
a.append("last")  # 리스트 마지막에 추가
a.sort()  # 정렬
a.reverse()  # 역순정렬
print(a.index("char"))  # 몇 번째 인덱스에 있는가?
a.insert(0, 4)  # n번 째 index에 x를 삽입
a.remove("char")  # 해당 값을 삭제 (여러 개 있을 경우 가장 앞에 있는걸 삭제)
a.extend([2, 3])  # 리스트에 추가

b = ["1", "2", "3", ["4", "5"]]
print(b[3][1])
