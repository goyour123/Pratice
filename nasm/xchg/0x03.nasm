
	global	_start

	section	.text

_start:
	;mov	rax, 100
	;mov	rdx, 60
	;sub	rdx, rax
	;sbb	rcx, rcx
	;and	rcx, rdx
	;add	rax, rcx

	;mov	rax, 60
	;mov	rdx, 100
	sub	rdx, rax
	sbb	rcx, rcx
	and	rcx, rdx
	add	rax, rcx
