
	global	_start

	section	.text

_start:
.loop:
	xor	byte [rsi], al
	lodsb
	loop	.loop
