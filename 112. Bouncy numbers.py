import math


def is_bouncy(nums):
    """A function that returns true if a number is bouncy"""
    nums = str(nums)  # Convert number to string
    (lg, rg) = (0, 0)
    for i in range(len(nums) - 1):
        if int(nums[i]) > int(nums[i + 1]):  # check if left is greater than right digit and increment lg
            lg += 1
        elif int(nums[i]) == int(nums[i + 1]):  # do nothing if the pair of digit selected are equal
            pass
        else:
            rg += 1  # if this loop is entered, right is greater, increment rg
    return lg != 0 and rg != 0  # if there are mixed increments, the number is bouncy


def bounce_ratio(upto):
    bouncy = len([i for i in range(100, upto + 1) if is_bouncy(i)])
    return bouncy / upto  # Return the ration of bouncy / total nos (up to 100, the numbers are not counted)


def timer(func, *args):
    """Timer function to check the execution time"""
    import time
    s = time.time_ns()
    func(args[0])
    e = time.time_ns()
    with open('logs.txt', mode="a") as file:
        file.write(f"Took {(e - s) / 10 ** 9:.2f} seconds to compute.\n\n")
    print(f"Took {(e - s) / 10 ** 9:.2f} seconds to compute.")


def main(factor):
    # We start at 100 though we have knowledge that 21780 returns 0.9. We could start here to speed
    # but it doesnot make a big difference, given the way our function is modeled.
    (start, upper_limit, lower_limit, i) = (100, 0, 0, 1)
    ratio = bounce_ratio(start)

    while ratio != 0.99:  # if the ratio is 0.99, end
        if ratio < 0.99:  # if the ratio is greater than 0.99
            lower_limit = start  # set the start value as the new lower limit
            # This is the slow loop where we calculate the upper limit adding mean of lower and upper to start
            if upper_limit != 0:
                p = int(abs((upper_limit - lower_limit) / 2))
                start = lower_limit + p
            # This is the speed loop where we quickly ramp the start value by multiplying with factor
            else:
                start = int(start * factor)
        else:
            upper_limit = start
            # if the start value returns a ratio > 0.99, we decrement
            start = upper_limit - int((upper_limit - lower_limit) / 2)

        ratio = bounce_ratio(start)
        string = f"{i} Ratio: {ratio:.8f}\tStart: {start}\tLower: {lower_limit}" \
                 f"\tUpper: {upper_limit}\tFactor: {factor}\n"
        with open('logs.txt', mode="a") as file:
            file.write(string)
        print(string, end="")
        i += 1
    print(f"The value is {start}")


timer(main, 8)

# We find that a factor of 8 returns the fastest result for the values 2 to 16 (both inclusive)
# hence use 8 for the best computation time ( 16 computation steps vs >25 for other values) 
