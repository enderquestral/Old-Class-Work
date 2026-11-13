#reads a positive value n from the user, loops to calculate the sum of 1 to n inclusively. Prints out the sum and returns from main, if user enters non-pos number, program should return from main
#By Hannah
    .text
    .align 2
    .globl main
main:
    li $a0, 0            #read int n
    li $v0, 5
    syscall
    move $t0,$v0        #move n into $t0
    li $a0, 0           #prep a0 to have things added to it
    bge $t0,$0,loop    #go to loop if positive


    li $v0,10
    syscall
loop:
    add $a0,$t0,$a0
    addi $t0,$t0,-1
    bgt $t0,$0,loop
    j print

print:
    li $v0,1
    syscall

#use jal to call a subroutine
