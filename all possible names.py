
A = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


file = open("nam.txt","a")

n = 1
name = ""

B= []

def add_alpha():
    #1
    for i in range(0,26):
        a =  A[i] 
        B.append(a)
    #2
    for i in range(26):
        for j in range(26): # eg a+abcd.......z then b+abcd....
            b = A[i] + A[j]
            B.append(b)
    #3
    for i in range(26):
        for j in range(26): # eg a+abcd.......z then b+abcd....
            for k in range(26):
              #  j = A[k]
              #  y = A[i] + j
                c= A[k] + A[i] +A[j]
                B.append(c)
    #4
    for i in range(26):
        for k in range(26): # eg a+abcd.......z then b+abcd....
            for g in range(26):
                for h in range(26):
                    ut= A[h]+ A[g] + A[i] +A[k]
                    B.append(ut)
    #5
    for i in range(26):
        for k in range(26): # eg a+abcd.......z then b+abcd....
            for g in range(26):
                for h in range(26):
                    for l in range(26):
                        ujt= A[l]+A[h]+ A[g] + A[i] +A[k]
                        B.append(ujt)
     #6
    # for i in range(26):
    #     for k in range(26): # eg a+abcd.......z then b+abcd....
    #        for g in range(26):
    #            for h in range(26):
    #                  for l in range(26):
    #                      for m in range(26):
    #                          gujt= A[m]+A[l]+A[h]+ A[g] + A[i] +A[k]
    #                          B.append(gujt)           
    # #7
    # for i in range(26):
    #     for k in range(26): # eg a+abcd.......z then b+abcd....
    #         for g in range(26):
    #             for h in range(26):
    #                 for l in range(26):
    #                     for m in range(26):
    #                         for n in range(26):
    #                             fgujt= A[n]+A[m]+ A[l]+A[h]+ A[g] + A[i] +A[k]
    #                             B.append(fgujt) 

add_alpha()
#print(B) 
no = len(B)
for i in range(no):
   file.write(B[i])
   file.write(" ")

