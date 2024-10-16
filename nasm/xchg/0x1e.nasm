
	global	_start

	section	.text

_start:
	cmp	al, 0x0a
	sbb	al, 0x69
	das
