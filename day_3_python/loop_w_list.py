nums = [1, 2, 3, 5, 8, 10]
find = 11
ck = False
idx = 0
for val in nums:
    if find == val:
        print(f"{find} found in the {idx}th index")
        ck = True
        break
    idx += 1
if ck != True:
    print("this number doesnt exist on the list")
