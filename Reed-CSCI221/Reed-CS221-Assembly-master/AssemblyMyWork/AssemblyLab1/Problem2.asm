# This program takes two global ints, subtraxts y from x.
    .data
x:  .word   7           # global variable x has value 7
y:  .word   4           # global variable x has value 4
    .text
    .align 2
    .globl main
main:
    la $t0, x           # load address x
    lw $a0, 0($t0)      # get value stored at that address
    la $t1, y           # load address y
    lw $a1, 0($t1)      # get value stored at that address
    sub $a0,$a0,$a1
    li $v0, 1           # set up "print int" system call
    syscall             # execute system call
    jr $ra              # return from main method