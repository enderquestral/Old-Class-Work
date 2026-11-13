#hanheller
#no partner, due to being sick on the lab day

"""Define a function brick_maker that takes a single parameter--- a symbol represented as a string---
and returns a function that's specialized for making a rectangular "brick" , 
that is, a string made up of repeats of that character, of a given width and height"""

""">>> at_brick = brick_maker('@')
>>> dot_brick = brick_maker('.')
>>> print(at_brick(3,2))
@@@
@@@

>>> print(dot_brick(5,1))
.....

>>> print(dot_brick(3,4))
...
...
...
...

>>> at_brick(2,2)
'@@\n@@\n'  

Note that brick_maker is a higher order function. 
When given a symbol it gives back a function, one that happens to be a brick creation function for that symbol.
"""

def brick_maker(symbol):

    def brick_construction(width,height):
        brick_section = ""
        i = 0
        while i < height:
            brick_section += (symbol*width)
            brick_section += "\n"
            i += 1
        return brick_section
        
    return brick_construction

