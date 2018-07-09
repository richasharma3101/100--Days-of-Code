arr=[int(x) for  x in input("Enter the number seperated by space= ").strip().split()]
s=set()
for x in range(len(arr)):
    if arr[x] in arr[x+1:]:
       s.add(arr[x])
       break
print(s)
