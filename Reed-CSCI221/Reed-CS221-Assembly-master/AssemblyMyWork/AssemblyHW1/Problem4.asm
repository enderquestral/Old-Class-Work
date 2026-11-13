#have global int array named arr, as well as global int num. num = # of entries in arr. Should have helper function named numEvens that takes 2 arguments: address of int arr, #of elements in arr argument, passing it the addresses of arr and value of num, printing out number returned by numevens before returning. Num evens should return the number of elements in the arr that are even, which main function should call and then print out the number returned by numEvens.
#By Hannah
    .data
num:  .word 5 #I tried to make arr:.word 0:num, but it errored... I also tried to init arr as all 0s and have the user input values, but it did Not Work.

arr:  .word 123, 3, 234, 141, -2256 #a total of 2 even ints  
    .text
    .align 2
    .globl main

main:
    lw $t0, arr       #t0 stores RAM location of arr, since that will take much data
    lw $s1, num         #s1 stores RAM location of num
    li $s2, 0            #s2 will be the counter for how much a thing has looped
    li $s3, 0            #s3 is what will store the output numEvens gives 

    jal numEvens

   
    move $a0,$s3
    li $v0, 1           # set up "print int" system call
    syscall             # execute system call

    li $v0,10
    syscall             # return from main method

#loop:   #THINGS WILL NOT BE PUT INTO arr
#    la $t7, arr       #t7 is pointer to arr
#    move $t1, $s2      #index into arr at s2
#    mul $t2,$t1,4       #t2 is offset into arr
#    add $t3,$t2,$t7     #t3 points to arr at t7
#    li $v0,5            #read int from user
#    syscall
#    move $t4,$v0        #assign a value to be placed into arr at point
#    sw $t4,0($t3)       #make the assignment OH BOYO
#    addi $s2,$s2,1
#    blt $s2,$s1,loop #if s2 <num, continue looping
#    jr $ra

numEvens:

    #t0 is pointer to arr
    #s2 is index into arr at val of s2, but not in base 4. t1 is s2 but in base four
    #load index at spot s2 in arr into t6
    la $t7, arr
    li $t1,1
    li $t2,0
    li $t3,0
    li $t4,0

    mul $t1,$t1,$s2
    mul $t2,$t1,4       #t2 is offset into arr
    add $t3,$t2,$t7     #t3 points to arr at t2
    mul $t1,$t1,4
    
    lw $t0, ($t3)#make t0 actually increment?

    move $t6,$t0 #GET THE VALUE FINALLY  
    

    addi $s2,$s2,1 
    ble $s2,$s1,evenorodd #if s2 <=num, continue looping

    jr $ra

evenorodd:
    li $t9, 2   #t9 is divisor, make it divide things by two
    div $t6,$t9          #divide, have to store remainder to check if its zero
    mfhi $t9             #save remainder in t9

    beq $t9, $0, itseven   #Does it have a remainder other than 0? it is odd
    
    j numEvens
itseven:
    addi $s3,$s3,1      #increment s3
    j numEvens