''' This function receives a two integers in 'base' representation, and returns the absoulte
value of their difference (also in 'base' representation). '''

def long_absolute_value_of_diff(num1,num2,base):
    orig_num1 = num1
    orig_num2 = num2
    res = 0
    power = 0
    carry = 0
    while num1 > 0 or num2 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        diff = digit1-digit2
        diff = diff-carry
        carry = 0
        if diff < 0:
            carry = carry+1
            diff = diff + base
        cur_power_factor = 10**power
        cur_addition = diff*cur_power_factor
        res = res + cur_addition
        
        power = power + 1
        
        frac_num1 = num1 / 10
        num1 = int(frac_num1)
        frac_num2 = num2 / 10
        num2 = int(frac_num2)
    if carry > 0:
        res = long_absolute_value_of_diff(orig_num2, orig_num1, base)
        
    return res

def short_absolute_value_of_diff(num1,num2,base):
    orig_num1 = num1
    orig_num2 = num2
    res = 0
    power = 0
    carry = 0
    while num1 > 0 or num2 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        diff = (num1 % 10)-(num2 % 10)-carry
        carry = 0
        if diff < 0:
            carry += 1
            diff += base
        res += diff*(10**power)
        power += 1
        
        num1 = int(num1 / 10)
        num2 = int(num2 / 10)
    res = long_absolute_value_of_diff(orig_num2, orig_num1, base) if carry > 0 else res
        
    return res

print(long_absolute_value_of_diff(241,302,5))
print(short_absolute_value_of_diff(241,302,5))