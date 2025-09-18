# mylist = [1, 2, 3, 4]
# left = 0
# right = sum(mylist)

# row = []

# for i in mylist:
#     # print(mylist[i] + mylist[i+1]
#     right -= i

#     if right - left > 0:
#         row.append(1)
#     elif right - left < 0:
#         row.append(-1)
#     else:
#         row.append(0)

#     left+=i
# print(row)


# second edition

def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0

def leftrightdiffence(nums):
    left, right = 0, sum(nums)

    result = []

    for num in nums:
        right -= num
        result.append(sign(right - left))
        left += num
    
    return result
