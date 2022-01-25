# Bull
# "abcd" = True / "" = False
# [1,2,3] = True / [] = False
# (1,2,3) = True / () = False
# {1,2,3} = True / {} = False
# 1 = True / 0 = False / None = False
a = [1, 2, 3, 4]
while a:
    a.pop()
    print(a)
