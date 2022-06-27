def is_bouncy(nums):
    nums = str(nums)
    (lg, rg) = (0, 0)
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            lg += 1
        elif nums[i] == nums[i+1]:
            pass
        else:
            rg += 1
    return lg != 0 and rg != 0

def bounce_ratio(upto):
    bouncy = len([i for i in range(100, upto+1) if is_bouncy(i)])
    return bouncy / upto


start = 21780
ratio = bounce_ratio(start)
factor = 1

while ratio != 0.99:
    if ratio < 0.99:
        start = start + int(start*1.1/factor)
    else:
        start = start - int(start*0.9/factor)
        factor += 1


    print(start)
    print(ratio)
    ratio = bounce_ratio(start)
