# This program takes two ints from user, prints out larger of the two values
    .data
prompt1: .asciiz "Please enter value: "

    .text
    .align 2
    .globl main
main:
    li $v0, 4           #Prints string
    la $a0, prompt1
    syscall

    li $v0, 5           #Reads the int
    syscall
    move $t0,$v0          #applies value in v0 to t0?

    li $v0, 4           #Prints string
    la $a1, prompt1
    syscall

    li $v0, 5           #Reads the int
    syscall
    move $t1,$v0         #applies value in v0 to t1?

    bge $t0,$t1,addTo     #t0 applies itself to t1 if its bigger. else not?
    #$a0 is int to be printed, so I have to apply the correct int to it
    move $a0,$t1
    li $v0, 1           # set up "print int" system call
    syscall             # execute system call
    jr $ra              # return from main method

addTo:
    li $t1,0          #Make t1 0 to add t0 to it
    add $t1,$t1,$t0     #For some reason, can't get it to go back to main?

    move $a0,$t1
    li $v0, 1           # set up "print int" system call
    syscall             # execute system call
    jr $ra   

