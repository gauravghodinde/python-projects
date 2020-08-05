print('please enter the number to calculate it\'s cube root')
pro = int(input())

for i in range(1, pro):
    c = i * i
    if (c == pro):
        break
if (i == (pro - 1)):
    Not_Found = pro
    print(Not_Found)
else:
    print(i)
