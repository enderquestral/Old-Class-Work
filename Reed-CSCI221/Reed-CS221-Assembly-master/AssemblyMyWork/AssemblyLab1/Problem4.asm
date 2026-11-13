# This program read in two positive integers, a and b, from the user and
# prints a * b.
    .text
    .align 2
    .globl main
main:
    li $a0,0
    li   $v0, 5          # set up reading of first int
    syscall
    move $t0, $v0        # store first int, a, into $t0
    blt  $t0, $0, done   # go to done if a not positive
    beq  $t0, $0, print  #If t0=0, go to print...

    li   $v0, 5          # set up reading of second int
    syscall
    move $t1, $v0        # store second int, b, into $t1
    blt  $t1, $0, done   # go to done if b not positive
    beq  $t1, $0, print  #If t1=0, go to print...
    la $t2, ($t1)        #Copy value of t1, to use for loop
    li $a0,0
    j loop
loop :
    sub $t2,$t2,1        #Subtracts t2 by 1
    add  $a0, $t0, $a0
    bgt $t2,$0,loop      #If t2 is not <0, loop more
    j print              #t2 is in negatives, go to print

print:
    li   $v0, 1       # set up "print int" system call
    syscall           # execute system call

done:
    jr   $ra          # return from main method
