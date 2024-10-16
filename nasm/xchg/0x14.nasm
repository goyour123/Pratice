
	global	_start

	section	.text

_start:
	mov	rcx, rax
	and	rcx, rdx

	xor	rax, rdx
	shr	rax, 1

	add	rax, rcx

