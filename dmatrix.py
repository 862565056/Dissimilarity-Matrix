#!/usr/bin/env python
# coding: utf-8
import numpy as np
n=int(input("Enter the number of Objects:"))
m=int((input("Enter the number of Attributes")))
z=5

def NominalORBinary(a,d,cnum):
    for i in range(n):
        for j in range(n):
            if i==j:
                d[cnum][i][j]=0
            if a[i][cnum]==a[j][cnum]:
                d[cnum][i][j]=0
            else:
                d[cnum][i][j]=1
    return d

def Numeric(a,d,cnum):
    max=np.amax(a,axis=0)[cnum]
    min=np.amin(a,axis=0)[cnum]
    denominator=max-min
    for i in range(n):
        for j in range(n):
            if i==j:
                d[cnum][i][j]=0
            d[cnum][i][j]=abs(a[i][cnum]-a[j][cnum])/denominator
    return d
    
def Ordinal(a,d,cnum):
    temp=[]
    for i in range(n):
        temp.append((a[i][cnum]-1)/(z-1))
    #print(a)
    for i in range(n):
        for j in range(n):
            if i==j:
                d[cnum][i][j]=0
            
            else:
                d[cnum][i][j]=np.linalg.norm(temp[i]-temp[j])
    return d
    
def DissimilarityMatrix(d,D):
    temp=0
    for i in range(n):
        
        for j in range(n):
            if i==j:
                D[i][j]=0
            for k in range(m):
                temp+=(d[k][i][j])
            D[i][j]=temp/m
            temp=0
    return D
def Similar(D):
    min=999
    x=0
    y=0
    for i in range(n):
        
            for j in range(n):
            
             if(i!=j):
                 if D[i][j]<min:
                     min=D[i][j]
                     x=i
                     y=j
    return min,x,y
                               
a=np.zeros((n,m))
d=np.zeros((m,n,n))
D=np.zeros((n,n))

dict={"Y":1,"N":0}

for i in range(n):
    print("Enter the details of Object "+chr(ord('A')+i));
    
    for j in range(m):
       entry=input()
       if entry in dict.keys():
            entry=dict[entry]
       a[i][j]=entry

print(a)

attribute_type=[]
for i in range(m):
    attribute_type.append(input("Enter Attribute "+str(i+1)+" Type:"))

for i in range(m):
    if attribute_type[i]=='Numeric':
        d=Numeric(a,d,i)
    elif attribute_type[i]=='Nominal':
        d=NominalORBinary(a,d,i)
    elif attribute_type[i]=='Binary':
        d=NominalORBinary(a,d,i)
    elif attribute_type[i]=='Ordinal':
        d=Ordinal(a,d,i)


print("Individual Dissimilirity Matrices are:")
print(d)

D=DissimilarityMatrix(d,D)
print("Mixed Attribute Dissimilirity Matrix:")
print(D)

value,x,y = Similar(D)
print("Objects "+str(x+1)+" and ",str(y+1)," are the most similar objects with the dissimilarity value of "+str(value))
