
	global	_start

	section	.text

_start:
	mov	rcx, rax
	and	rcx, rbx
	not	rcx

	not	rax
	not	rbx
	or	rax, rbx

	cmp	rax, rcx
