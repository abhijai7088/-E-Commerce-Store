"""p=int(input("enter the amount"))
if(p<1000):
    print("10% discount")
elif(p>1000 and p<2000):
    print("20% discount")
elif(p>2000 and p<3000):
    print("30% discount")
else:
    print("40% discount")"""

# +ve or -ve number


'''a=int(input())
if(a):
    print("+ve no:")
else:
    print("-ve no:")'''



    # area calculation
'''radius=float(input("Enter the Radius:"))
if (radius>0) :
    print("Calculated Area is : ")
    area=3.14*radius*radius
    print(area)
else:
    print("Area cannot be Calculated!")'''

#integer problem statement
'''
a=int(input())
b=int(input())
c=int(input())
if(a!=b and b!=c and c!=a):
    print("1")
else:
    print("0")'''


#multiply

'''M=int(input())
N=int(input())
if (M%N != 0):
    print(0)
else:
    print(M/N)'''



#prime number or not using while lopp and break

'''n=int(input("enter a no:"))
flag=0
i=2
while(i<n):
    if(n%i==0):
        flag=1
        break
    i=i+1


    
if(flag==1):
     print('not a prime no !')
else:
    print('prime no ')'''




# while loop continue 


'''i=1
while(i<=10):
    print(i)
    i=i+1
    if(i==3):
        continue
   # i=i+1
else:
    print("good bye !")'''


#enter no. is prime or not using break 


'''n=int(input("enter the no.:"))
flag=0
for i in range(2,n):
    
    if (n%i==0):
        flag=1
        break
    i=i+1
if(flag==1):
    print('not prime number')
else:
    print(' prime number')'''

# print the prime number upto N 

'''N=int(input('enter the integer:'))
i=2
flag=0
while(i<=N):
    
    for v in range(2,i):
         if (i%v==0):
             flag=1
             break
    
    if(flag==0):
        print(i,end=' ')
    i=i+1'''


#print prime no from this range 
'''n1=int(input())
n2=int(input())
print()
for num in range(n1,n2+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
'''



#pattern 
'''for  i in range(1,6):
    for j in range(i,6):
        print("*",end=" ")
        i+=1
    print()
'''
'''             # continue and break
for i in range (1,10):
    if i==4:
        break
    else:
        print(i)

print()
print()
               
#continue

for i in range(1,10):
    if i==4:
        continue
    else:
         print(i)  

print()      ''' 

              
                #pass 
                
''' for i in range(1,10):
            if i==4:
                pass
            else:
                print(i)  ''' 




                



# ray want to upload a phota on facebook but has some constrainsts

'''L=int(input())>
N=int(input())
while N>0:
    W,H=input().split()
    W=int(W)
    H=int(H)
    N=N-1
    
    if (W<L or H<L ):
         print("UPLOAD ANOTHER")
    elif(W>L and H>L):
         print("CROP IT")
    

    else:
          print("ACCEPTED")'''




# iterable vs iterator


'''S="HELLO"
I=iter(S)
L=(len(S))
i=0
while L>i:
    print(next(I))
    i=i+1'''







#nested loop 


'''i=1
j=1
while i<=3:
    
    while j<=3:
        
        print(i,'->',j)
        j=j+1
    i=i+1
'''



#pattern prnting
"""
   *
   * *
   * * *
   * * * * 
   """


'''for i in range(0,5):             
    for j in range(0,i):
        print('*',end=' ')
    print()'''


'''
* * * * *
* * * *
* * *
* *
*

for i in range (1,6):
    for j in range(i,6):
        print("*",end=' ')
    print()
'''
        
    
'''1
2 3 
4 5 6 
7 8 9  10 
11 12 13 14 15 




k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end='            ')
        k=k+1
    print()'''





# set in python

'''M={'Ram','shyam','ram','Sohan',-22,88,12}

print(len(M))
print(M)
print(type(M)) '''


#set method in pyhton 


'''S={2,3,4,'Ram','Shyam'}
R=('shantanu','Shubham','Abhishek')
#S.clear()
S.add(R)
S.remove(3)
#S.remove(('Shyam',3))# error
S.discard(5)#no error as 5 is not present in the S set


print(S)
'''
      
      #copy( )  and S1 =S2 difference 

'''S1={1,2,3,4,5,6}
S2=S1

S3=S1.copy()
S2.add(22)

print(S1,'------------')
print(S2,'@@@@@@')




print(S3,'#######')'''


#update()  method
'''S={1,2,3,4,5}
L=['ram','Shyanm','dog']
O=(55,66,88)
S.update(L,O)
print(S)

#output:{1, 2, 3, 4, 5, 'ram', 66, 88, 'dog', 'Shyanm', 55}'''


#differernce()

"""S1={1,2,3,4}
S2={2,4,5,6}
L=[4,5,6]
R=S2.difference(S1)
T=S2.difference(L)
print(R)
print(T)"""

#symmetric_difference_update()
'''S1={1,2,3,4,5,6}
S2={3,4,5,6,7,8}
S1.symmetric_difference_update(S2)
print(S1)
print(S2)
#update in S2 remein same '''


#pop() method in set 
'''S1={1,2,3,4,5,6,7}
S1.pop()
S1.pop()
R=S1.pop()
print(R)
print(S1)'''





#  study for st 2 


#dictionary
'''d={
    "brand":"LG",
    "Model":"Refrigerator",
    "year":20200,
    "year":2020
}
print(d)'''

# function
'''
def simpleIntrest(p,r,t):
    S=p*r*t/100
    print(f"Simple intrest is {S}")
#calling a function
simpleIntrest(S)
'''
#return function
'''def f1(*a):
    sum=0
    for item in a:
        sum+=item
    return sum
a=f1(10,59,56,647,4434,65,5634,)
print(a)

'''

#fibonacci series upto n 
'''def fibonacci(n):
    a,b=0,1
    if n<=0:
        print("Enter a positive number!")
    elif n==1:
        print(f"fibonacci sequence upto {n} :{a}")
    else:
        print(f"fibbonacci sequence upto {n} :{a},{b}", end="")
        for i in range(2,n):
            
            a,b=b,a+b
fibonacci(10)'''
        

        #fibonacci upto n 
'''def fibonacci_upto_n(n):
    # Start with the first two numbers of the Fibonacci sequence
    a, b = 0, 1
    sequence = []
    
    while a <= n:
        sequence.append(a)
        a, b = b, a + b  # Update a and b for the next numbers in the sequence
    
    return sequence

# Example usage
n = 10 # Change this to any number you want
print("Fibonacci sequence up to", n, ":", fibonacci_upto_n(n))
'''


# file handelling
'''import pandas as pd
d={ "Name":['Abhishek','vivek','ramu'],
"age":[112,22,25],
"city":['delhi','meerat','bihar']
}
data=pd.DataFrame(d)
print(data)
'''


# 
'''l=['M','o','N']
print("@".join(l))
'''

# convert matrix 1 d to 2d 
'''import numpy as np

arr=np.array([12,13,14,15,16,17,18,19,10,122,33,22])
data=arr.reshape(3,4)
data2=arr.reshape(4,3)
print(data)
print(data2)'''


# matplotlib
'''import matplotlib.pyplot as plt
import numpy as np
xpoint=np.array([1,2,3,4,5])
ypoint=np.array([10,20,30,40,50])
plt.xlabel("years")
plt.ylabel("sales")
plt.title("line chart")
plt.legend("line")
#plt.bar
plt.scatter(xpoint,ypoint,color='black')
plt.show()'''


#pie chart
'''import matplotlib.pyplot as plt
import numpy as np
mylabels=['Lucknow','noida','delhi','gurgao','mumbai']
X=np.array([58,23,35,51,6])
explodedata=(0.3,0,0,0,0)
plt.pie(X,labels=mylabels,explode=explodedata)
plt.show()
'''
# st 2 pre  

#prime no in range entered by users 



'''P,Q=input("enter the ranges :").split()
P=int(P)
Q=int(Q)
for num in range(P,Q+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
'''


       #reverse a string using sling
'''entered_string=str(input("enter a string to reverse :"))
#using slicing
reversed_string=entered_string[::-1]
print(reversed_string)       '''              
    #using loop
'''input_string=str(input("enter the string: "))
reversed_string=""

for char in input_string:
    reversed_string=char+reversed_string
print(reversed_string)'''



#input list from user and print the second largest no from it
# Taking input from the user
#numbers = list((int, input("Enter a list of integers separated by space: ").split()))

#Checking if the list has at least two unique numbers
'''if len(set(numbers)) < 2:
    print("List does not have enough unique numbers to determine the second largest.")
else:
    # Removing duplicates and sorting in descending order
    unique_numbers = sorted(set(numbers), reverse=True)
    second_largest = unique_numbers[1]  # The second largest is at index 1
    print("The second largest number is:", second_largest)'''


    #remove vowel from the string
'''N=str(input("enter the string: "))
vowel="aeiouAEIOU"
resul_string=''.join([char for char in N if char not in vowel])
print(f"the resulted string is  {resul_string}")
'''



'''import numpy as np
arr = np.array([2,52,1,5,2,54,62,64])
n=np.sort(arr)
print(n)'''
#   dictionary merge
'''dict1 = {"a": 1, "c": 3}
dict2 = {"b": 2, "d": 4}
merged_dict = {**dict1, **dict2}
#sorted_dict = dict(sorted(merged_dict.items()))
print(merged_dict)'''
#read a line by line file in the txt
'''read_file=open("ram.txt","r")
lines=read_file.readlines
for line in lines:
    print(lines)'''
#matplotlib
'''import matplotlib.pyplot as plt
import numpy as np

subjects = ["Math", "Physics", "Chemistry", "Biology"]
marks =np.array([85, 90, 78, 92])

plt.bar(subjects, marks, color='blue')
plt.plot(subjects, marks, color='blue')
explodedata=(0.3,0,0,0)
plt.pie(marks,labels=subjects,explode=explodedata)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()'''


#tuple (index)


'''t=(12,12,13,134,15,13,16,17,18,13,14,13,1,5,16,17,18,13)
S=t.index(13,3,15)
print(S)'''

#tuple sorted with function

'''def sec(el):
    return el[1]
T=((1,12),(13,4),(5,55))
I=sorted(T,reverse=False,key=sec)
print(I)'''
#min,max,sum operation in tuple

'''T=((100,400),(56,300),(516,1))
I=min(T)
M=max(T)
print(I)
print(M)'''


#sting literals

'''
print('D:\new folder\table.txt')
print(r'D:\new folder\table.txt')
S='he"l"lo "thish is the "'
for i in S:
    print(repr(i))
       print(len(i))
    print(len("Hello"))'''


#partition
'''s='this is the best python is the best place'
r=s.rpartition('is')
print(r)'''

#multiple encoding via table
'''FS='abc'
SS='def'
Table=FS.maketrans(FS,SS)
print(Table)'''

#del in list 
'''L=[1,2,3,4,5,6,6,7,89,]
L[3]=[2,3]
del L[3][1]
print(L)'''

#addin an element in list

'''L1=[1,2,3,4,5,6,67,8,9,10]
#L.append((2,3,5))
#add element in the begining 
L1[:0]=[10]
#add elemnet in the middle 
L1[4:5]=[111]
# insert in the lAST 
L1[-1:]=[11111]
print(L1)'''


#matrix using list
L=[[1,2,3,],
[4,5,6],
[7,8,9]]
for i in range(0,3):
    for j in range(3):
      print(L[i][j],end=' ')
    print()