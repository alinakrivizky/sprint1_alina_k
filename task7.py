def digit_root(num):
    for i in range(1, 99999999):
        if num >= 10:
            digits = str(num)
            num = sum(int(digit) for digit in digits)
    return num
print(digit_root(16))  
print(digit_root(942))  
print(digit_root(132189))
            
