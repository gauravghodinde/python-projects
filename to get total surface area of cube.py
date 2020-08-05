#to get total surface area of cube
print()
print('enter the length of the cube\nif total surface area is available\nand u want length enter \'area\'')
Sarea=input()
if (Sarea=='area'):
    print('enter total surface area')
    sa=int(input())
    pro=sa//6
    for i in range(1,pro):
        b = i*i
        if(b==pro):
         break
    print('the length of the cube is',i)
else:
    Sarea=float(Sarea)
    surface=6*Sarea*Sarea
    print('total surface area of cube is',surface)
