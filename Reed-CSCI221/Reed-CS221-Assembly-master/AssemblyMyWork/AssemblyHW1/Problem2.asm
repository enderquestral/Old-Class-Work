#reads a positive int x from the user, indicating number of values that will be entered. read in x numbers from user. Program should print out the max of those values. return from main. if x is less than or equal to 0, return from main.
#By Hannah
    .text
    .align 2
    .globl main
main:
    li $a0, 0            #read int x
    li $v0, 5
    syscall
    move $t0,$v0        #move n into $t0. t0 still be used for loop.
    li $t7, 0           #establish t7 as 0, use that to hold max
    bgt $t0,$0,loop    #go to loop if positive
    li $v0,10
    syscall
    jr $ra

t2isbiggerthant7:
    la $t7,($t2)
    addi $t0,$t0,-1
    bgt $t0,$0,loop     #if t0 is not 0, continue to loop
    j print

loop:
    li $a0, 0            #read int
    li $v0, 5
    syscall
    move $t2,$v0 #have user input a number into t2
    bgt $t2,$t7,t2isbiggerthant7 #check if that number is larger than largest t7, if so put in t7

    addi $t0,$t0,-1
    bgt $t0,$0,loop     #if t0 is not 0, continue to loop
    j print


print:
    li $v0,1
    la $a0, ($t7)
    syscall

#use jal to call a subroutine
