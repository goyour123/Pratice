nasm -f elf64 hello.nasm -o hello.o
ld hello.o -o hello
rm hello.o
