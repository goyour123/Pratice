
	global	_start

	section	.text

_start:
	call	.skip
	db	'hello world!', 0
.skip:
	call	print_str
	add	rsp, 8
