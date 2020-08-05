print('please enter the number to be reversed')
n = int(input())
temp = n
rev = 0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10

print('the reversed number is:  ' + str(rev))    
