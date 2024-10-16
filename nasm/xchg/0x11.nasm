
	global	_start

	section	.text

_start:
.loop:
	mov	dl, byte [rsi]
	xor	dl, byte [rdi]
	inc	rsi
	inc	rdi
	or	al, dl
	loop	.loop
