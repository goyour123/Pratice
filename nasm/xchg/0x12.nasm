
	global	_start

	section	.text

_start:
	mov	rcx, rdx
	and	rdx, rax
	or	rax, rcx
	add 	rax, rdx
