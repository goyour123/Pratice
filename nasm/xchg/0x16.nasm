
	global	_start

	section	.text

_start:
	xor	rax, rbx
	xor	rbx, rcx
	mov	rsi, rax
	add	rsi, rbx
	cmovc	rax, rbx
	xor	rax, rbx
	cmp	rax, rdi
