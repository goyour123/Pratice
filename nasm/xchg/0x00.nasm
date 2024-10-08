
	global	_start

	section	.text

_start:
	xor	eax, eax
	lea	rbx, [0]
	;mov	rcx, 5
	loop	$
	mov	rdx, 0
	and	esi, 0
	sub	edi, edi
	push	0
	pop	rbp	
