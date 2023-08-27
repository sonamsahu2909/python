# 1. output : 1 2 3 4 5
# i=1
# while i<6:
#     print(i,end=" ")
#     i+=1 

# 2.odd number (1 3 5 7 9)
# i= 1
# while i<10:
#     print(i,end=" ")
#     i+=2

# 3 even number (0,2,4,6,8)
# i= 0
# while i<10:
#     print(i,end=" ")
#     i+=2

# 4.  10 to 1
# i= 10
# while i>=1:
#     print(i,end=" ")
#     i-=1

# 5. 1000 100 10 1
# i= 1000
# while i>=1:
#     print(int(i),end=" ")
#     i = i/10

# 6. 1,10,100,1000
# i= 1
# while i<=1000:
#     print(int(i),end=" ")
#     i = i*10

# 7. 2,4,8,10,14,16,20,22 
# i= 2
# while i<=22:
#     print(i,end=" ")
#     i = i+2
#     print(i,end=" ")
#     i = i+4

# 8. 1 ,1 ,1 ,2 ,4 ,8 ,3 ,9 ,27 ,4 ,16 ,64 ,5 ,25 ,125
# i= 1
# while i<=5:
#     print(i,end=" ")
#     s = i**2
#     print(s,end=" ")
#     c = i**3
#     print(c,end=" ")
#     i+=1

# 9. 10 ,15 ,12 ,17 ,14 ,19 ,16 ,21 ,
# i= 10
# while i<=16:
#     print(i,end=" ")
#     s = i**2
#     print(s,end=" ")
#     c = i**3
#     print(c,end=" ")
#     i+=1

i,n=1,5
while n>0:
    if(n%i==0):
         print(i , end=',')
    i=i+1
print()
   