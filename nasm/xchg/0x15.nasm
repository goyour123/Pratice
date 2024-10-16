
	global	_start

	section	.text

_start:
	;mov	rax, -9
	mov	rdx, 0xffffffff80000000
	add	rax, rdx
	xor	rax, rdx
