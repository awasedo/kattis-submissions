num = int(input())

binary = "{0:b}".format(num)

binary = binary[::-1]

def binary_to_decimal(num):
    b = list(num)
    n = len(list(num))
    decimal = 0
    hold = 0
    i = 0
    exp = n-1
    while (i < n):
        x = int(b[i])
        quot= 2**exp
        hold = x*quot
        i += 1
        exp -= 1
        decimal = decimal + hold
    return(decimal)

print(binary_to_decimal(binary))
