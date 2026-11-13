def sum_power2(n):
    if n ==0:
        return "1"

    return ( "(" + str(sum_power2(n-1)) + "+" + str(sum_power2(n-1)) + ")")
