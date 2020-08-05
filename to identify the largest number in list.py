list=[]
a=0
print('enter the number\'s and when completed enter \'exit\'in the same way')
print()
while True:
    print('please enter the numbers ' + str(a+1))
    name = input()
    if(name =='exit'):
             print('thank u')
             print()
             break
    else:
        list = list +[name]
        a=a+1
print('this is your entered list: ',list)
max = list[0]
for i in range(len(list)):
    if max < list[i]:
        max = list[i]

print('the largest number in list is:  ' + str(max))
        
