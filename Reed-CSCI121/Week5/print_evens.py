#hanheller

is_even = (lambda x: x%2 == 0)

def conditional_print(test):
    
    def printing_procedure(x):
            if test(x):
                print(x)
#            else:
#                return
    return printing_procedure

print_evens = conditional_print(is_even)

