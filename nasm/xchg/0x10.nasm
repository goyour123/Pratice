
	global	_start

	section	.text

_start:
	push	rax
	push	rcx
	pop	rax
	pop	rcx

	xor	rax, rcx
	xor	rcx, rax
	xor	rax, rcx

	add	rax, rcx
	sub	rcx, rax
	add	rax, rcx
	neg	rcx

	xchg	rax, rcx
