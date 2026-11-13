#partner: hanheller
#partner: garciase

def is_prime(n):

    placeholder = n -1
    if n <= 1:
        return False
    while placeholder != 1 and n != placeholder:
        if n % placeholder == 0:
            return False
        placeholder = placeholder - 1

    return True
