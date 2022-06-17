from math import sqrt
A = [0]*8
B = [0]*10
С = [0]*10
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

print("Введите по цифре восьмизначный идентификационный код")
for i in range(8):
    A[i] = int(input())
    
B[0]= A[0] + (A[7]//A[4]) + 2*A[1]
B[1]= A[1]+A[3]
B[2]= abs(fac(A[2]) - A[3])
B[3]= A[3] % A[6]
B[4]= A[0]//A[1]
B[5]= A[2]//A[3]
B[6]= ((A[4]**A[0])+A[3])//A[7]
B[7]= A[5]-A[1]
B[8]= abs(A[6]-A[3])+A[1]
B[9]= abs((i+1)-A[7])*(A[1]+A[4])


С[0]= round(A[0] + sqrt(A[6]))
С[1]= round(sqrt(A[5])+A[4])
С[2]= A[1]+(A[5]%A[7])
С[3]= A[6]//A[3]+A[4]
С[4]= abs((A[2]**A[7])-A[5])
С[5]= (i+1)-A[1]
С[6]= (A[3]**2)-С[4]+A[4]
С[7]= round(A[1]*С[1]+A[0])
С[8]= A[4]+A[1]+(A[6]%A[3])
С[9]= round(fac(A[3])//С[0]-A[2])


print('№:')
print(B)
print('PIN:')
print(С)
