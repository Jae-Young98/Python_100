# input output
a = input("숫자를 입력하세요 : ")

print(a)

# file r = read, w = write, a = add

f = open("새파일.txt", 'w', encoding="UTF-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("새파일.txt", 'r', encoding="UTF-8")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

f = open("새파일.txt", 'r', encoding="UTF-8")
data = f.read()  # 파일을 모두 불러옴
print(data)
f.close()

f = open("새파일.txt", 'a', encoding="UTF-8")  # write는 모두 삭제하고 새로 씀
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
