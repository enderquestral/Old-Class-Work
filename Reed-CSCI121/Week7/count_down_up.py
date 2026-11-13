#partner: hanheller
#partner: thomsonc
def count_down_up(n):
    print(n)
    if n >1:
        count_down_up(n-1)
        print(n)