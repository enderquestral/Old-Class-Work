	.file	"bytesbenchmark.cpp"
	.text
	.section	.text._ZNSt6vectorIiSaIiEE17_M_realloc_insertIJRKiEEEvN9__gnu_cxx17__normal_iteratorIPiS1_EEDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE17_M_realloc_insertIJRKiEEEvN9__gnu_cxx17__normal_iteratorIPiS1_EEDpOT_,comdat
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEE17_M_realloc_insertIJRKiEEEvN9__gnu_cxx17__normal_iteratorIPiS1_EEDpOT_
	.type	_ZNSt6vectorIiSaIiEE17_M_realloc_insertIJRKiEEEvN9__gnu_cxx17__normal_iteratorIPiS1_EEDpOT_, @function
_ZNSt6vectorIiSaIiEE17_M_realloc_insertIJRKiEEEvN9__gnu_cxx17__normal_iteratorIPiS1_EEDpOT_:
.LFB4154:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	movq	%rdx, %r15
	movq	%rsi, %rdx
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	movq	%rdi, %r13
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movq	%rsi, %r12
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$40, %rsp
	.cfi_def_cfa_offset 96
	movq	8(%rdi), %rcx
	movq	(%rdi), %rbp
	movq	%rcx, %rax
	subq	%rbp, %rdx
	subq	%rbp, %rax
	sarq	$2, %rax
	je	.L10
	leaq	(%rax,%rax), %rdi
	movq	$-4, %r14
	cmpq	%rdi, %rax
	jbe	.L17
.L3:
	movq	%r14, %rdi
	movq	%rdx, 16(%rsp)
	movq	%rcx, 8(%rsp)
	call	_Znwm@PLT
	movq	16(%rsp), %rdx
	movq	8(%rsp), %rcx
	movq	%rax, %rbx
	addq	%rax, %r14
.L4:
	movl	(%r15), %eax
	movq	%rcx, %r15
	leaq	4(%rbx,%rdx), %r9
	subq	%r12, %r15
	movl	%eax, (%rbx,%rdx)
	leaq	(%r9,%r15), %rax
	movq	%rax, 8(%rsp)
	cmpq	%rbp, %r12
	je	.L5
	movq	%rbp, %rsi
	movq	%rbx, %rdi
	movq	%r9, 24(%rsp)
	movq	%rcx, 16(%rsp)
	call	memmove@PLT
	movq	16(%rsp), %rcx
	movq	24(%rsp), %r9
	cmpq	%rcx, %r12
	je	.L9
.L6:
	movq	%r15, %rdx
	movq	%r12, %rsi
	movq	%r9, %rdi
	call	memcpy@PLT
.L8:
	testq	%rbp, %rbp
	jne	.L9
.L7:
	movq	%rbx, 16(%rsp)
	movq	16(%rsp), %xmm0
	movq	%r14, 16(%r13)
	movhps	8(%rsp), %xmm0
	movups	%xmm0, 0(%r13)
	addq	$40, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L9:
	.cfi_restore_state
	movq	%rbp, %rdi
	call	_ZdlPv@PLT
	jmp	.L7
	.p2align 4,,10
	.p2align 3
.L17:
	movabsq	$4611686018427387903, %rax
	cmpq	%rax, %rdi
	ja	.L3
	xorl	%r14d, %r14d
	xorl	%ebx, %ebx
	testq	%rdi, %rdi
	je	.L4
	jmp	.L2
	.p2align 4,,10
	.p2align 3
.L5:
	cmpq	%rcx, %r12
	jne	.L6
	jmp	.L8
	.p2align 4,,10
	.p2align 3
.L10:
	movl	$1, %edi
.L2:
	leaq	0(,%rdi,4), %r14
	jmp	.L3
	.cfi_endproc
.LFE4154:
	.size	_ZNSt6vectorIiSaIiEE17_M_realloc_insertIJRKiEEEvN9__gnu_cxx17__normal_iteratorIPiS1_EEDpOT_, .-_ZNSt6vectorIiSaIiEE17_M_realloc_insertIJRKiEEEvN9__gnu_cxx17__normal_iteratorIPiS1_EEDpOT_
	.section	.text._ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE,"axG",@progbits,_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE,comdat
	.align 2
	.p2align 4,,15
	.weak	_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE
	.type	_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE, @function
_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE:
.LFB4155:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rsi, %r14
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$24, %rsp
	.cfi_def_cfa_offset 80
	movslq	4(%rdx), %r15
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	movslq	(%rdx), %rax
	subq	%rax, %r15
	movq	%rax, %rsi
	cmpq	$2147483644, %r15
	ja	.L19
	addq	$1, %r15
	movl	$2147483645, %eax
	xorl	%edx, %edx
	movabsq	$8589934597, %r8
	divq	%r15
	movq	(%r14), %rdx
	imulq	%rax, %r15
	movq	%rax, %r9
	.p2align 4,,10
	.p2align 3
.L20:
	imulq	$16807, %rdx, %rdi
	movq	%rdi, %rax
	movq	%rdi, %rcx
	mulq	%r8
	subq	%rdx, %rcx
	shrq	%rcx
	addq	%rcx, %rdx
	shrq	$30, %rdx
	movq	%rdx, %rcx
	salq	$31, %rcx
	subq	%rdx, %rcx
	subq	%rcx, %rdi
	leaq	-1(%rdi), %rax
	movq	%rdi, %rdx
	cmpq	%rax, %r15
	jbe	.L20
	xorl	%edx, %edx
	movq	%rdi, (%r14)
	divq	%r9
.L21:
	addl	%esi, %eax
	movq	8(%rsp), %rbx
	xorq	%fs:40, %rbx
	jne	.L34
	addq	$24, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L19:
	.cfi_restore_state
	cmpq	$2147483645, %r15
	je	.L22
	movq	%rdx, %r12
	movq	%r15, %rdx
	movq	%rdi, %rbp
	movq	%rsp, %r13
	movabsq	$-9223372028264841207, %rbx
	shrq	%rdx
	movq	%rdx, %rax
	mulq	%rbx
	shrq	$29, %rdx
	movl	%edx, %ebx
.L30:
	movq	%r13, %rdx
	movq	%r14, %rsi
	movq	%rbp, %rdi
	movl	$0, (%rsp)
	movl	%ebx, 4(%rsp)
	call	_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE
	imulq	$16807, (%r14), %rdi
	movslq	%eax, %rsi
	movabsq	$8589934597, %rax
	mulq	%rdi
	movq	%rdi, %rax
	subq	%rdx, %rax
	shrq	%rax
	addq	%rax, %rdx
	shrq	$30, %rdx
	movq	%rdx, %rax
	salq	$31, %rax
	subq	%rdx, %rax
	subq	%rax, %rdi
	movq	%rsi, %rax
	salq	$30, %rax
	movq	%rdi, %rdx
	movq	%rdi, (%r14)
	subq	%rsi, %rax
	subq	$1, %rdx
	addq	%rax, %rax
	addq	%rdx, %rax
	setc	%dl
	movzbl	%dl, %edx
	cmpq	%rax, %r15
	jb	.L30
	testq	%rdx, %rdx
	jne	.L30
	movl	(%r12), %esi
	jmp	.L21
	.p2align 4,,10
	.p2align 3
.L22:
	imulq	$16807, (%r14), %rcx
	movabsq	$8589934597, %rdx
	movq	%rcx, %rax
	mulq	%rdx
	movq	%rcx, %rax
	subq	%rdx, %rax
	shrq	%rax
	addq	%rdx, %rax
	shrq	$30, %rax
	movq	%rax, %rdx
	salq	$31, %rdx
	subq	%rax, %rdx
	subq	%rdx, %rcx
	movq	%rcx, %rax
	movq	%rcx, (%r14)
	subq	$1, %rax
	jmp	.L21
.L34:
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE4155:
	.size	_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE, .-_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE
	.text
	.p2align 4,,15
	.globl	_Z11init_bufferiRSt26linear_congruential_engineImLm16807ELm0ELm2147483647EERSt6vectorIiSaIiEE
	.type	_Z11init_bufferiRSt26linear_congruential_engineImLm16807ELm0ELm2147483647EERSt6vectorIiSaIiEE, @function
_Z11init_bufferiRSt26linear_congruential_engineImLm16807ELm0ELm2147483647EERSt6vectorIiSaIiEE:
.LFB3688:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	leal	-1(%rdi), %ebp
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$88, %rsp
	.cfi_def_cfa_offset 144
	movl	%edi, 28(%rsp)
	movq	%rdx, 32(%rsp)
	movq	%fs:40, %rbx
	movq	%rbx, 72(%rsp)
	xorl	%ebx, %ebx
	movl	$0, 56(%rsp)
	movl	%ebp, 60(%rsp)
	movl	$0, 64(%rsp)
	testl	%ebp, %ebp
	jle	.L35
	movq	%rsi, %r12
	xorl	%eax, %eax
	leaq	64(%rsp), %rbx
	movq	%rdx, %r13
	jmp	.L40
	.p2align 4,,10
	.p2align 3
.L65:
	movl	%eax, (%rsi)
	movl	64(%rsp), %eax
	addq	$4, %rsi
	movq	%rsi, 8(%r13)
	addl	$1, %eax
	movl	%eax, 64(%rsp)
	cmpl	%eax, %ebp
	jle	.L64
.L40:
	movq	8(%r13), %rsi
	cmpq	16(%r13), %rsi
	jne	.L65
	movq	%rbx, %rdx
	movq	%r13, %rdi
	call	_ZNSt6vectorIiSaIiEE17_M_realloc_insertIJRKiEEEvN9__gnu_cxx17__normal_iteratorIPiS1_EEDpOT_
	movl	64(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 64(%rsp)
	cmpl	%eax, %ebp
	jg	.L40
	.p2align 4,,10
	.p2align 3
.L64:
	movl	28(%rsp), %eax
	leaq	56(%rsp), %r13
	movq	%r12, %r14
	movq	$0, 16(%rsp)
	movabsq	$8589934597, %rbp
	movq	16(%rsp), %rbx
	subl	$2, %eax
	movq	%rax, 40(%rsp)
	leaq	64(%rsp), %rax
	movq	%rax, (%rsp)
	.p2align 4,,10
	.p2align 3
.L50:
	movq	%r13, %rdx
	movq	%r14, %rsi
	movq	%r13, %rdi
	movl	%ebx, %r12d
	call	_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE
	movl	28(%rsp), %esi
	cltd
	subl	%ebx, %esi
	idivl	%esi
	movl	%esi, 12(%rsp)
	movl	%edx, 24(%rsp)
	addl	%ebx, %edx
	movl	%edx, %eax
	cmpl	%ebx, %edx
	jne	.L41
	movl	56(%rsp), %esi
	.p2align 4,,10
	.p2align 3
.L49:
	movslq	60(%rsp), %rcx
	movslq	%esi, %rax
	subq	%rax, %rcx
	movq	%rcx, %r15
	cmpq	$2147483644, %rcx
	ja	.L42
	leaq	1(%rcx), %rcx
	movl	$2147483645, %eax
	xorl	%edx, %edx
	movq	(%r14), %rdi
	divq	%rcx
	imulq	%rax, %rcx
	movq	%rax, %r9
	.p2align 4,,10
	.p2align 3
.L43:
	imulq	$16807, %rdi, %r8
	movq	%r8, %rax
	movq	%r8, %rdi
	mulq	%rbp
	subq	%rdx, %rdi
	shrq	%rdi
	addq	%rdx, %rdi
	shrq	$30, %rdi
	movq	%rdi, %rax
	salq	$31, %rax
	subq	%rdi, %rax
	movq	%r8, %rdi
	subq	%rax, %rdi
	leaq	-1(%rdi), %rax
	cmpq	%rax, %rcx
	jbe	.L43
	xorl	%edx, %edx
	movq	%rdi, (%r14)
	divq	%r9
.L44:
	addl	%esi, %eax
	cltd
	idivl	12(%rsp)
	leal	(%rdx,%r12), %eax
	cmpl	%edx, 24(%rsp)
	je	.L49
.L41:
	movq	32(%rsp), %rbx
	cltq
	movq	(%rbx), %rdx
	movq	16(%rsp), %rbx
	leaq	(%rdx,%rax,4), %rax
	leaq	(%rdx,%rbx,4), %rdx
	movl	(%rax), %esi
	movl	(%rdx), %ecx
	movl	%esi, (%rdx)
	movl	%ecx, (%rax)
	leaq	1(%rbx), %rax
	cmpq	%rbx, 40(%rsp)
	je	.L35
	movq	%rax, 16(%rsp)
	movq	%rax, %rbx
	jmp	.L50
	.p2align 4,,10
	.p2align 3
.L35:
	movq	72(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L66
	addq	$88, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L42:
	.cfi_restore_state
	cmpq	$2147483645, %rcx
	je	.L45
	movabsq	$-9223372028264841207, %rax
	movq	%rcx, %rdx
	shrq	%rdx
	mulq	%rdx
	shrq	$29, %rdx
	movl	%edx, %ebx
.L58:
	movq	(%rsp), %rdx
	movq	%r14, %rsi
	movq	%r13, %rdi
	movl	%ebx, 68(%rsp)
	movl	$0, 64(%rsp)
	call	_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE
	imulq	$16807, (%r14), %rsi
	movslq	%eax, %rcx
	movq	%rsi, %rax
	mulq	%rbp
	movq	%rsi, %rax
	subq	%rdx, %rax
	shrq	%rax
	addq	%rax, %rdx
	shrq	$30, %rdx
	movq	%rdx, %rax
	salq	$31, %rax
	subq	%rdx, %rax
	subq	%rax, %rsi
	movq	%rcx, %rax
	salq	$30, %rax
	movq	%rsi, %rdx
	movq	%rsi, (%r14)
	subq	%rcx, %rax
	subq	$1, %rdx
	addq	%rax, %rax
	addq	%rax, %rdx
	setc	%al
	movzbl	%al, %eax
	cmpq	%rdx, %r15
	jb	.L58
	testq	%rax, %rax
	jne	.L58
	movq	%rdx, %rax
	movl	56(%rsp), %esi
	jmp	.L44
	.p2align 4,,10
	.p2align 3
.L45:
	imulq	$16807, (%r14), %rcx
	movq	%rcx, %rax
	mulq	%rbp
	movq	%rcx, %rax
	subq	%rdx, %rax
	shrq	%rax
	addq	%rdx, %rax
	shrq	$30, %rax
	movq	%rax, %rdx
	salq	$31, %rdx
	subq	%rax, %rdx
	subq	%rdx, %rcx
	movq	%rcx, %rax
	movq	%rcx, (%r14)
	subq	$1, %rax
	jmp	.L44
.L66:
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE3688:
	.size	_Z11init_bufferiRSt26linear_congruential_engineImLm16807ELm0ELm2147483647EERSt6vectorIiSaIiEE, .-_Z11init_bufferiRSt26linear_congruential_engineImLm16807ELm0ELm2147483647EERSt6vectorIiSaIiEE
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"# Bytes:"
.LC1:
	.string	"      "
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC2:
	.string	"Time of one byte (nanoseconds): \n"
	.section	.text.unlikely,"ax",@progbits
.LCOLDB4:
	.section	.text.startup,"ax",@progbits
.LHOTB4:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB3689:
	.cfi_startproc
	.cfi_personality 0x9b,DW.ref.__gxx_personality_v0
	.cfi_lsda 0x1b,.LLSDA3689
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	movl	$8, %edx
	leaq	.LC0(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	movabsq	$8589934597, %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$104, %rsp
	.cfi_def_cfa_offset 160
	movq	%fs:40, %rax
	movq	%rax, 88(%rsp)
	xorl	%eax, %eax
	leaq	40(%rsp), %r12
.LEHB0:
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l@PLT
	movl	$6, %edx
	leaq	.LC1(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l@PLT
	leaq	.LC2(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
.LEHE0:
	leaq	64(%rsp), %rax
	pxor	%xmm0, %xmm0
	movq	$0, 80(%rsp)
	movq	$1, 40(%rsp)
	movl	$10, 16(%rsp)
	movq	%rax, 24(%rsp)
	movaps	%xmm0, 64(%rsp)
	.p2align 4,,10
	.p2align 3
.L88:
	pxor	%xmm1, %xmm1
	movsd	.LC3(%rip), %xmm0
	cvtsi2sd	16(%rsp), %xmm1
	call	pow@PLT
	movq	24(%rsp), %rdx
	movq	%r12, %rsi
	cvttsd2si	%xmm0, %eax
	movl	%eax, %edi
	movl	%eax, %ebx
	movl	%eax, 20(%rsp)
.LEHB1:
	call	_Z11init_bufferiRSt26linear_congruential_engineImLm16807ELm0ELm2147483647EERSt6vectorIiSaIiEE
	movslq	TESTING_SIZE(%rip), %rdi
	leal	-1(%rbx), %r8d
	movb	$97, 39(%rsp)
	movl	$0, 48(%rsp)
	movl	%r8d, 52(%rsp)
	testl	%edi, %edi
	jle	.L68
	leaq	48(%rsp), %rax
	xorl	%esi, %esi
	leaq	56(%rsp), %r14
	xorl	%r15d, %r15d
	movq	%rax, 8(%rsp)
	.p2align 4,,10
	.p2align 3
.L77:
	movslq	%r8d, %r8
	movslq	%esi, %rax
	subq	%rax, %r8
	movq	%r8, %r13
	cmpq	$2147483644, %r8
	ja	.L69
	leaq	1(%r8), %r8
	movl	$2147483645, %eax
	xorl	%edx, %edx
	movq	40(%rsp), %rcx
	divq	%r8
	imulq	%rax, %r8
	movq	%rax, %r9
	.p2align 4,,10
	.p2align 3
.L70:
	imulq	$16807, %rcx, %r10
	movq	%r10, %rax
	movq	%r10, %rcx
	mulq	%rbp
	subq	%rdx, %rcx
	shrq	%rcx
	addq	%rdx, %rcx
	shrq	$30, %rcx
	movq	%rcx, %rax
	salq	$31, %rax
	subq	%rcx, %rax
	movq	%r10, %rcx
	subq	%rax, %rcx
	leaq	-1(%rcx), %rax
	cmpq	%rax, %r8
	jbe	.L70
	xorl	%edx, %edx
	movq	%rcx, 40(%rsp)
	divq	%r9
.L71:
	movq	64(%rsp), %rdx
	addl	%esi, %eax
	addl	$1, %r15d
	cltq
	movl	(%rdx,%rax,4), %eax
	movb	%al, 39(%rsp)
	movzbl	39(%rsp), %eax
	cmpl	%edi, %r15d
	jge	.L76
	movl	52(%rsp), %r8d
	jmp	.L77
	.p2align 4,,10
	.p2align 3
.L69:
	cmpq	$2147483645, %r8
	je	.L72
	movabsq	$-9223372028264841207, %rax
	movq	%r8, %rdx
	shrq	%rdx
	mulq	%rdx
	shrq	$29, %rdx
	movl	%edx, %ebx
.L109:
	movq	8(%rsp), %rdi
	movq	%r14, %rdx
	movq	%r12, %rsi
	movl	%ebx, 60(%rsp)
	movl	$0, 56(%rsp)
	call	_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE
	imulq	$16807, 40(%rsp), %rdi
	movl	%eax, %esi
	movq	%rdi, %rax
	movq	%rdi, %rcx
	mulq	%rbp
	subq	%rdx, %rcx
	shrq	%rcx
	addq	%rdx, %rcx
	movslq	%esi, %rdx
	shrq	$30, %rcx
	movq	%rcx, %rax
	salq	$31, %rax
	subq	%rcx, %rax
	subq	%rax, %rdi
	movq	%rdx, %rax
	salq	$30, %rax
	movq	%rdi, %rcx
	movq	%rdi, 40(%rsp)
	subq	%rdx, %rax
	leaq	-1(%rdi), %rdx
	addq	%rax, %rax
	addq	%rdx, %rax
	setc	%dl
	movzbl	%dl, %edx
	cmpq	%rax, %r13
	jb	.L109
	testq	%rdx, %rdx
	jne	.L109
	movl	48(%rsp), %esi
	movslq	TESTING_SIZE(%rip), %rdi
	jmp	.L71
	.p2align 4,,10
	.p2align 3
.L72:
	imulq	$16807, 40(%rsp), %r8
	movq	%r8, %rax
	movq	%r8, %rcx
	mulq	%rbp
	subq	%rdx, %rcx
	shrq	%rcx
	addq	%rdx, %rcx
	shrq	$30, %rcx
	movq	%rcx, %rax
	salq	$31, %rax
	subq	%rcx, %rax
	movq	%r8, %rcx
	subq	%rax, %rcx
	movq	%rcx, 40(%rsp)
	leaq	-1(%rcx), %rax
	jmp	.L71
	.p2align 4,,10
	.p2align 3
.L68:
	movq	40(%rsp), %rcx
	.p2align 4,,10
	.p2align 3
.L76:
	imulq	$16807, %rcx, %rcx
	movq	%rcx, %rax
	mulq	%rbp
	movq	%rcx, %rax
	subq	%rdx, %rax
	shrq	%rax
	addq	%rax, %rdx
	shrq	$30, %rdx
	movq	%rdx, %rax
	salq	$31, %rax
	subq	%rdx, %rax
	subq	%rax, %rcx
	movabsq	$2305843009213693950, %rax
	movq	%rcx, 40(%rsp)
	cmpq	%rax, %rdi
	ja	.L78
	salq	$2, %rdi
	call	_Znam@PLT
	movslq	TESTING_SIZE(%rip), %rdi
	movq	%rax, %r13
	call	_Znam@PLT
	movq	%rax, %r14
	movl	TESTING_SIZE(%rip), %eax
	xorl	%r15d, %r15d
	leaq	48(%rsp), %rbx
	testl	%eax, %eax
	jle	.L83
	.p2align 4,,10
	.p2align 3
.L80:
	movq	%rbx, %rdx
	movq	%r12, %rsi
	movq	%rbx, %rdi
	call	_ZNSt24uniform_int_distributionIiEclISt26linear_congruential_engineImLm16807ELm0ELm2147483647EEEEiRT_RKNS0_10param_typeE
	movl	%eax, 0(%r13,%r15,4)
	addq	$1, %r15
	cmpl	%r15d, TESTING_SIZE(%rip)
	jg	.L80
.L83:
	call	_ZNSt6chrono3_V212system_clock3nowEv@PLT
	movl	TESTING_SIZE(%rip), %edx
	movq	%rax, %r15
	testl	%edx, %edx
	jle	.L125
	movq	64(%rsp), %rcx
	xorl	%eax, %eax
	xorl	%ebx, %ebx
	.p2align 4,,10
	.p2align 3
.L84:
	addl	$1, %eax
	movslq	(%rcx,%rbx,4), %rbx
	cmpl	%edx, %eax
	jne	.L84
.L81:
	call	_ZNSt6chrono3_V212system_clock3nowEv@PLT
	pxor	%xmm0, %xmm0
	pxor	%xmm1, %xmm1
	movl	20(%rsp), %esi
	subq	%r15, %rax
	cvtsi2sd	TESTING_SIZE(%rip), %xmm1
	leaq	_ZSt4cout(%rip), %rdi
	cvtsi2sdq	%rax, %xmm0
	divsd	%xmm1, %xmm0
	movsd	%xmm0, 8(%rsp)
	call	_ZNSolsEi@PLT
	movl	$6, %edx
	leaq	.LC1(%rip), %rsi
	movq	%rax, %rdi
	movq	%rax, %r15
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l@PLT
	movsd	8(%rsp), %xmm0
	movq	%r15, %rdi
	call	_ZNSo9_M_insertIdEERSoT_@PLT
	movl	%ebx, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	movl	$6, %edx
	leaq	.LC1(%rip), %rsi
	movq	%rax, %rdi
	movq	%rax, %rbx
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l@PLT
	leaq	56(%rsp), %rsi
	movl	$1, %edx
	movq	%rbx, %rdi
	movb	$10, 56(%rsp)
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l@PLT
.LEHE1:
	movq	64(%rsp), %rax
	cmpq	72(%rsp), %rax
	je	.L85
	movq	%rax, 72(%rsp)
.L85:
	movq	%r13, %rdi
	call	_ZdaPv@PLT
	movq	%r14, %rdi
	call	_ZdaPv@PLT
	addl	$1, 16(%rsp)
	movl	16(%rsp), %eax
	cmpl	$27, %eax
	jne	.L88
	movq	64(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L89
	call	_ZdlPv@PLT
.L89:
	xorl	%eax, %eax
	movq	88(%rsp), %rbx
	xorq	%fs:40, %rbx
	jne	.L126
	addq	$104, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L125:
	.cfi_restore_state
	xorl	%ebx, %ebx
	jmp	.L81
.L126:
	call	__stack_chk_fail@PLT
.L116:
	jmp	.L117
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA3689:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE3689-.LLSDACSB3689
.LLSDACSB3689:
	.uleb128 .LEHB0-.LFB3689
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB3689
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L116-.LFB3689
	.uleb128 0
.LLSDACSE3689:
	.section	.text.startup
	.cfi_endproc
	.section	.text.unlikely
	.cfi_startproc
	.cfi_personality 0x9b,DW.ref.__gxx_personality_v0
	.cfi_lsda 0x1b,.LLSDAC3689
	.type	main.cold.32, @function
main.cold.32:
.LFSB3689:
.L78:
	.cfi_def_cfa_offset 160
	.cfi_offset 3, -56
	.cfi_offset 6, -48
	.cfi_offset 12, -40
	.cfi_offset 13, -32
	.cfi_offset 14, -24
	.cfi_offset 15, -16
.LEHB2:
	call	__cxa_throw_bad_array_new_length@PLT
.LEHE2:
.L95:
.L117:
	movq	64(%rsp), %rdi
	movq	%rax, %rbx
	testq	%rdi, %rdi
	je	.L91
	call	_ZdlPv@PLT
.L91:
	movq	%rbx, %rdi
.LEHB3:
	call	_Unwind_Resume@PLT
.LEHE3:
	.cfi_endproc
.LFE3689:
	.section	.gcc_except_table
.LLSDAC3689:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSEC3689-.LLSDACSBC3689
.LLSDACSBC3689:
	.uleb128 .LEHB2-.LCOLDB4
	.uleb128 .LEHE2-.LEHB2
	.uleb128 .L95-.LCOLDB4
	.uleb128 0
	.uleb128 .LEHB3-.LCOLDB4
	.uleb128 .LEHE3-.LEHB3
	.uleb128 0
	.uleb128 0
.LLSDACSEC3689:
	.section	.text.unlikely
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
	.size	main.cold.32, .-main.cold.32
.LCOLDE4:
	.section	.text.startup
.LHOTE4:
	.p2align 4,,15
	.type	_GLOBAL__sub_I_TESTING_SIZE, @function
_GLOBAL__sub_I_TESTING_SIZE:
.LFB4463:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	leaq	_ZStL8__ioinit(%rip), %rdi
	call	_ZNSt8ios_base4InitC1Ev@PLT
	movq	_ZNSt8ios_base4InitD1Ev@GOTPCREL(%rip), %rdi
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	leaq	__dso_handle(%rip), %rdx
	leaq	_ZStL8__ioinit(%rip), %rsi
	jmp	__cxa_atexit@PLT
	.cfi_endproc
.LFE4463:
	.size	_GLOBAL__sub_I_TESTING_SIZE, .-_GLOBAL__sub_I_TESTING_SIZE
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_TESTING_SIZE
	.globl	TESTING_SIZE
	.data
	.align 4
	.type	TESTING_SIZE, @object
	.size	TESTING_SIZE, 4
TESTING_SIZE:
	.long	1000
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC3:
	.long	0
	.long	1073741824
	.hidden	DW.ref.__gxx_personality_v0
	.weak	DW.ref.__gxx_personality_v0
	.section	.data.rel.local.DW.ref.__gxx_personality_v0,"awG",@progbits,DW.ref.__gxx_personality_v0,comdat
	.align 8
	.type	DW.ref.__gxx_personality_v0, @object
	.size	DW.ref.__gxx_personality_v0, 8
DW.ref.__gxx_personality_v0:
	.quad	__gxx_personality_v0
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 8.3.0-6ubuntu1~18.04.1) 8.3.0"
	.section	.note.GNU-stack,"",@progbits
