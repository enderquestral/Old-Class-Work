# This program prints the value of variable x to the console.
    .data
x:  .word   7           # global variable x has value 7
    .text
    .align 2
    .globl main
main:
    addi $sp, $sp, -4   # grow the stack
    sw $ra, 0($sp)      # store the return address onto the stack
    la $t0, x           # load address
    lw $a0, 0($t0)      # get value stored at that address
    li $v0, 1           # set up "print int" system call
    syscall             # execute system call
    lw $ra, 0($sp)      # get the return address from the stack
    addi $sp, $sp, 4    # shrink the stack
    jr $ra              # return from main method
