Assignment 24 and Assignment 25
-----------------------------------------
ASSIGNMENT 24
# # Q1
# # l1=[1,2,3,4,5]
# # print(sum(l1))
# #---------------------------------
# # Q2
# # l1=[1,2,3,4,5]
# # avg=sum(l1)/len(l1)
# # print(avg)
# #-------------------------------------------------------
# #Q3.
# l1=[1,2,3,4,5]
# # l2=[]
# # for e in l1:
# #     l2.append(e**2)
# # print(l2)
# #or
# l2=[e**2 for e in l1]
# print(l2)
# #Q4.-----------------------------------------------------
# # l1=[1,2,3,4,5]
# # # l1.sort(reverse=True)
# # # print(l1)
 
# # for i in range(0,len(l1)-1):
# #     temp=0
# #     for j in range(i+1,len(l1)):
# #         if l1[i]<l1[j]:
# #             temp=l1[i]
# #             l1[i]=l1[j]
# #             l1[j]=temp
# #             # l1[i]=l1[i]+l1[j]
# #             # l1[j]=l1[i]-l1[j]
# #             # l1[i]=l1[i]-l1[j]

# # print(l1)

#Q5.-----------------------------------------------------------
# l1=[5,6,7,8]
# l2=[]
# i=1
# for e in l1:
#     if i%2==0:
#         l2.append(e)
#     i+=1
# print(l2)
# l2=[l1[i] for i in range(0,4) if i%2==0] if with 0 based indexing
# print(l2)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ASSIGNMENT 25
# Q1.
# N=int(input("Enter a number"))
# l1=[2*i for i in range(1,N+1)] 
# print(l1)
# -----------------------------------------
# Q2.
# a,b=-1,1
# l1=[]
# while N:
#     c=a+b
#     l1.append(c)
#     a,b=b,c
#     N-=1
# print(l1)
# l1=[]
# for i in range(0,N):
#     c=a+b
#     l1.append(c)
#     a,b=b,c
# print(l1)
# ------------------------------------------
# Q4. 
# l1=[
#     [int(e) for e in input("Enter a number").split(',')],
#     [int(e) for e in input("Enter a number").split(',')],
#     [int(e) for e in input("Enter a number").split(',')]
# ]
# l2=[
#     [int(e) for e in input("Enter a number").split(',')],
#     [int(e) for e in input("Enter a number").split(',')],
#     [int(e) for e in input("Enter a number").split(',')]
# ]
# l3=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(0,3):
#     for j in range(0,3):
#         l3[i][j]=l1[i][j]+l2[i][j]
# print(l3)
# -------------------------------------------
# Q5.
# l1=[1,2,3,4,0,-1,-2,-3,-4]
# l2=[]
# l3=[]
# for e in l1:
#     if e>0:
#         l2.append(e)
#     else:
#         l3.append(e)
# print(l2)
# print(l3)
# --------------------------------------------
# Q3.
# x=2
# l1=[]
# while N:
#     for i in range(2,x):
#         if x%i==0:
#             break
#     else:
#         l1.append(x)
#         N-=1
#     x+=1
# print(l1)
















