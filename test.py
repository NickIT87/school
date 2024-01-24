import functools 
  
# initializing list 
lis = [1, 3, 5, 6, 2] 
  
# using reduce to compute sum of list 
print("The sum of the list elements is : ", end="") 
print(functools.reduce(lambda a, b: a+b, lis)) 
  
# using reduce to compute maximum element from list 
print("The maximum element of the list is : ", end="") 
print(functools.reduce(lambda a, b: a if a > b else b, lis)) 

for i in range(1, len(lis)):
    if lis[i] > lis[i-1]:
        print(lis[i])
    else:
        print(lis[i-1])
    
