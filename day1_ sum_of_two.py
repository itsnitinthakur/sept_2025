nums =[2,7,9,11,13]
target = 9
h= {}
for i, num in enumerate(nums):
    
    n= target - num
    print(n)
    if n not in h:
        h[num] = i
    else:
        print ([h[n], i])
    print(h)