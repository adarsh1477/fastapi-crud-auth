def unique_number(arr):
    ones=000
    twos=000

    for i in arr:
        ones = (ones ^ i) & ~twos
        twos = (twos ^ i) & ~ones

    return ones

print(unique_number([1,2,1,2,3,1,2]))