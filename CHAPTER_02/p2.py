# Set 집합 자료형 / data를 다룰떄 사용 / 순서 및 중복이 없다
set1 = set([1, 2, 3])  # == set1 = {1,2,3}

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)  # 교집합 == s1.intersection(s2)
print(s1 | s2)  # 합집합 == s1.union(s2)
print(s1 - s2)  # 차집합 == s1.difference(s2)

s1.add(7)  # 집합에 원소 추가
s1.update([7, 8, 9])  # 원소 여러개 추가
s1.remove(2)  # 원소 제거
print(s1)
