
	global	_start

	section	.text

_start:
.loop:
	bsf	rcx, rax
	shr	rax, cl
	cmp	rax, 1
	je	.exit_loop
	lea	rax, [rax + 2 * rax + 1]
	jmp	.loop
.exit_loop:
