# indexing
a = "Life is too short, You need python"
print(a[::1])  # [::] 이상 : 미만 : 간격 (매우 중요!!)
print(a[-1])  # 역순

number = 10
day = "three"
b = "I ate %d apples. so I was sick for %s days." % (number, day)
print(b)

c = "%0.4f" % 3.421313  # 간격 . 남길 자리 수
print(c)

d = "Hobby"
print(d.count('b'))  # b의 개수
print(d.find('b'))  # index 에서 가장 먼저나오는 b를 찾아 return

e = ",".join("abcd")  # ,기준으로 join
print(e)

g = "Life is too short"
print(g.replace("Life", "Your leg"))  # ""를 ""로 교체

h = "Life is too short"
print(h.split())  # () 기준으로 나눠 리스트화
