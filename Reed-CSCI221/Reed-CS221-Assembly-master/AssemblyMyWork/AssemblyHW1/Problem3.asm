# This program takes user input char c, and global string str.
#function countOccurrences takes two arguments: address of a string and a character, then returns the number of times that character occurs in the string.
#By Hannah
    .data
str1:   .asciiz "oona the orange goat"            
str3:   .asciiz "input character [press enter]: "
    .text
    .align 2
    .globl main
main:
    la $a0, str3
    syscall
    li $v0,12           #read character c
    syscall
    move $t0,$v0        #place the value of the character in t0
    li $t7,0            #Make t7 the counter, establish as 0
    li $t3,0
    li $t5,0
    la $s1, str1         #make s1 the value of the string
    jal looptofindstrlength #jump to there


    li $v0,10
    syscall             # return from main method

looptofindstrlength:
    lb $t3, 0($s1)
    beq $t3,$0, inbetween #FIX
    addi $s1,$s1,1
    j looptofindstrlength

inbetween:
    la $s2 str1
    sub $t5, $s1, $s2 #t5 now has length of str
    la $s1, str1 
    j countOccurrences


countOccurrences:
    lb $t1, ($s1)   #using s1 as a pointer for the string, load value into t1
    addi $t2,$t2,1 #Make yet another counter, counting through steps of letters
    beq $t0,$t1,addonetovalue #if t1==t0, t7++
    addi $s1,$s1,1 

    blt $t2,$t5, countOccurrences #if t1 < the length of the string, loop
    #print out the value gotten from this, return from main
    li $v0,1
    la $a0, ($t7)
    syscall
    jr $ra

    addonetovalue:
        addi $t7,$t7,1  #increment t7 by 1 if true
        addi $s1,$s1,1
        blt $t2,$t5, countOccurrences #if t1 < the length of the string, loop
        #print out the value gotten from this, return from main
        li $v0,1
        la $a0, ($t7)
        syscall
        jr $ra

