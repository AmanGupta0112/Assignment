n = int(input("Enter the length of 1st array :"))
m = int(input("Enter the length of 2nd array :"))

arr1 = []
arr2 = []

print("Enter 1st array elements:")
for i in range(n):
    ele = int(input())
    arr1.append(ele)

print("\nEnter 2st array elements:")
for i in range(m):
    ele = int(input())
    arr2.append(ele)


l1 = len(arr1)
l2 = len(arr2)

new_ls = []

for r in range(l1):
    ls = []
    for a in range(l2):
        if arr1[r] == arr2[a]:
                ls.append(arr2[a])
                if r < l1-1 and a < l2-1:
                    r += 1
                    a += 1
                    if arr1[r] != arr2[a]:
                        break

    tp = tuple(ls)
    new_ls.append(tp)
max = []
for i in new_ls:
    if len(max) < len(i):
        max = i

print(max)
