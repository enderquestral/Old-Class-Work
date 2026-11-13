#hanheller

"""Write a function def max_of_funcs(f,g) which takes two function parameters, f and g. 
It should return function h, with the property that when given a value x the result of h(x) should be 
the maximum of f(x) and g(x). Note that this function is very different from the function max_of_two`,
 but the two are closely related."""

def max_of_funcs(f,g):
    item1= f
    item2= g

    def h(x):
        if item1(x)>item2(x):
            return item1(x)
        elif item1(x) == item2(x):
            return item1(x)
        else:
            return item2(x)

    return h